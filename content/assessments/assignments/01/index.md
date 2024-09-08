<h1 align="center">
A01
</h1>

<p style="text-align: center;">
    <object hspace="50">
        <strong>Due</strong></a>: Sep 5, 2024 by 11:59 p.m.
    </object>
    <object hspace="50">
        <strong>Points</strong></a>: 40
    </object>
</p>

Please submit your answers as a PDF to gradescope.

## Problem 1

**Points**: 6

Why is the quality of sequencing data typically lower at the end of a read in Sanger sequencing?

??? note "Solution"

    The quality of sequencing data in Sanger sequencing tends to decrease towards the end of a read due to several factors related to the nature of the sequencing process. This phenomenon is primarily attributed to the decreasing population of longer DNA fragments. Here's a detailed explanation:

    1. Probability of ddNTP incorporation:
        - To obtain longer fragments, we need to avoid incorporating a dideoxynucleotide (ddNTP) until the very end of the sequence.
        - As the length of the fragment increases, the probability of not incorporating a ddNTP at any previous position decreases.
        - This results in fewer long fragments compared to shorter ones, leading to weaker signals for longer sequences.
    2. Concentration ratio of dNTPs to ddNTPs:
        - While we maintain a low concentration of ddNTPs relative to dNTPs to promote the synthesis of longer fragments, the cumulative probability of ddNTP incorporation still increases with length.
        - This leads to a gradual decrease in the population of fragments as their length grows.
    3. Mass and mobility differences:
        - As DNA fragments increase in length, the relative mass difference between fragments of consecutive lengths decreases.
        - For example, the mass difference between a 99-mer and a 100-mer is proportionally smaller than the difference between a 9-mer and a 10-mer.
        - This results in poorer separation of longer fragments during electrophoresis, contributing to decreased resolution and quality of signals for longer reads.
    4. Signal-to-noise ratio:
        - Due to the factors mentioned above, the signal intensity for longer fragments is lower.
        - This leads to a decreased signal-to-noise ratio for longer reads, making it more difficult to accurately determine the base calls at the end of a sequence.

    Some students might suggest that the depletion of ddNTPs is responsible for the lower quality of longer reads.
    However, this is not correct.
    It's important to clarify that:

    - The reaction mixture contains an excess of both dNTPs and ddNTPs.
    - The concentrations of these nucleotides are not significantly depleted during the sequencing reaction.
    - The relative concentrations of dNTPs and ddNTPs remain essentially constant throughout the process.

## Problem 2

**Points**: 6

What is the purpose of adding adapters to DNA fragments in Illumina sequencing?

## Problem 3

**Points**: 4

Compare and contrast the principles behind Sanger sequencing and Illumina sequencing.
How does each method overcome the challenge of determining the order of nucleotides in a DNA strand?
In your answer, consider the strengths and limitations of each approach.

## Problem 4

**Points**: 5

In Sanger sequencing, the ratio of dideoxynucleotides (ddNTPs) to deoxynucleotides (dNTPs) is crucial for successful sequencing.
Explain why this ratio is essential and predict what might happen if:

1.  The concentration of ddNTPs is too high;
2.  The concentration of ddNTPs is too low.

## Problem 5

**Points**: 4

Illumina sequencing uses "bridge amplification" to create clusters of identical DNA fragments.
Describe how this process works and explain why it's necessary for the Illumina sequencing method.
How does this compare to the amplification process in Sanger sequencing?

## Problem 6

**Points**: 4

You are designing primers for a Sanger sequencing experiment.
The region you want to sequence contains an important single nucleotide polymorphism (SNP) at position 90 from the start of your sequence of interest.
Given what you know about the typical quality of Sanger sequencing reads at different positions, where would you design your sequencing primer to bind?
Explain your reasoning.

## Problem 7

**Points**: 2

You are conducting a Sanger sequencing experiment on a gene of interest isolated from a wild plant population.
Upon examining the chromatogram, you notice that multiple peaks frequently overlap at several positions, making base calling difficult.
This pattern persists even when you repeat the sequencing with newly designed primers.
Further investigation reveals that the plant samples were collected from an area known for its high biodiversity and the presence of closely related species.

What is one possible molecular or genomic explanation for the overlapping peaks observed in your chromatogram?
Describe how it could lead to the pattern in the sequencing results.

!!! note "Clarification"

    In this scenario, we are working with plant samples collected from a wild population in an area known for high biodiversity.
    This means we're not dealing with lab-grown, genetically identical plants, but rather with plants that have natural genetic variation.

    When we say we're sequencing "a gene of interest isolated from a wild plant population," we're typically working with DNA extracted from a single plant specimen.
    However, this single specimen can contain genetic material from multiple closely related organisms due to various biological phenomena.

    Sanger sequencing typically starts with many copies of a specific DNA region (our "gene of interest").
    These copies are created through PCR amplification of the extracted DNA.
    The sequencing reaction is then performed on this amplified DNA.

    The chromatogram represents the sequencing results from all the DNA molecules present in your sample. If there are multiple versions of the gene present, they will all be sequenced simultaneously, resulting in overlapping peaks.

## Problem 8

**Points**: 4

In Illumina sequencing, adapters are ligated to DNA fragments before sequencing.

-   Explain the role of these adapters in the sequencing process.
-   How might errors in adapter ligation affect the sequencing results and downstream data analysis?
-   Describe how the design of these adapters helps prevent the formation of adapter dimers.

## Problem 9

**Points**: 5

Compare the structure of a typical surfactant to a phospholipid.
How do these structural differences contribute to the surfactant's ability to lyse cells?
Explain why increasing the concentration of surfactants in a lysis buffer might not always lead to better DNA yield.
What potential problems could arise from using too much surfactant?
