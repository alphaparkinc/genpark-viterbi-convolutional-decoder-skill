from client import ViterbiConvolutionalCodec

bits = [1, 0, 1, 1, 0, 0]
enc = ViterbiConvolutionalCodec.encode(bits)
print(f"Original Bits: {bits}")
print(f"Encoded Convolutional Symbols: {enc}")

# Inject error
noisy = list(enc)
noisy[2] ^= 1
dec = ViterbiConvolutionalCodec.decode(noisy)
print(f"Decoded Output via Viterbi: {dec}")
