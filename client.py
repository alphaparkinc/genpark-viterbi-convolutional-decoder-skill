"""Convolutional Encoder and Viterbi Trellis Decoder Engine.
100% Python Standard Library.
"""

class ViterbiConvolutionalCodec:
    """Rate 1/2 K=3 Convolutional Codec with Viterbi decoding."""
    @staticmethod
    def encode(bits):
        s1, s2 = 0, 0
        encoded = []
        for b in bits:
            y1 = b ^ s1 ^ s2
            y2 = b ^ s2
            encoded.extend([y1, y2])
            s2 = s1
            s1 = b
        return encoded

    @staticmethod
    def decode(encoded_bits):
        transitions = {}
        for s in range(4):
            s1 = (s >> 1) & 1
            s2 = s & 1
            for b in [0, 1]:
                next_s = (b << 1) | s1
                y1 = b ^ s1 ^ s2
                y2 = b ^ s2
                transitions[(s, b)] = (next_s, (y1, y2))

        metrics = {0: 0, 1: float("inf"), 2: float("inf"), 3: float("inf")}
        paths = {s: [] for s in range(4)}

        for t in range(0, len(encoded_bits), 2):
            r1, r2 = encoded_bits[t], encoded_bits[t + 1]
            new_metrics = {s: float("inf") for s in range(4)}
            new_paths = {s: [] for s in range(4)}

            for s in range(4):
                if metrics[s] == float("inf"):
                    continue
                for b in [0, 1]:
                    next_s, (y1, y2) = transitions[(s, b)]
                    dist = (r1 ^ y1) + (r2 ^ y2)
                    candidate_cost = metrics[s] + dist
                    if candidate_cost < new_metrics[next_s]:
                        new_metrics[next_s] = candidate_cost
                        new_paths[next_s] = paths[s] + [b]

            metrics = new_metrics
            paths = new_paths

        best_state = min(metrics, key=metrics.get)
        return paths[best_state]
