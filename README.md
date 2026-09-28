# genpark-viterbi-convolutional-decoder-skill

Agent Skill implementing the **Viterbi Trellis Algorithm** for maximum-likelihood decoding of rate 1/2 constraint-length $K=3$ convolutional codes over noisy communication channels.

## Architectural Overview
```mermaid
flowchart TD
    Input["Noisy Symbol Pairs (r1, r2)"] --> Trellis["Construct 4-State Trellis Diagram"]
    Trellis --> Branch["Calculate Branch Metrics (Hamming Distance)"]
    Branch --> ACS["Add-Compare-Select State Path Metrics"]
    ACS --> Prune["Prune Suboptimal Survivor Paths"]
    Prune --> Backtrack["Backtrack Minimum-Metric Path"]
    Backtrack --> Decoded["Recovered Source Bitstream"]
```
