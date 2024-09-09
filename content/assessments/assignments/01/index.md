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

## Q01

**Points**: 6

Why is the quality of sequencing data typically lower at the end of a read in Sanger sequencing?

??? success "Solution"

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

## Q02

**Points**: 6

What is the purpose of adding adapters to DNA fragments in Illumina sequencing?

??? success "Solution"
    Adapters are short oligonucleotide sequences added to DNA fragments during Illumina sequencing library preparation.

    !!! note "Key purpose"
        Adapters contain sequences complementary to oligonucleotides on the Illumina flow cell surface.
        This allows DNA fragments to bind to the flow cell and form clusters.

    They serve several other crucial purposes.

    1. **Priming for sequencing**: Adapters include primer binding sites for both forward and reverse sequencing reactions.
    2. **Index/barcode sequences**: Adapters often contain unique index sequences that allow for multiplexing&mdash;running multiple samples in a single sequencing lane.
    3. **Bridge amplification**: Adapter sequences facilitate bridge amplification, which generates clonal clusters of each DNA fragment on the flow cell surface.
    4. **Sequencing initiation**: The adapter sequences provide a known starting point for the sequencing reaction.

## Q03

**Points**: 4

Compare and contrast the principles behind Sanger sequencing and Illumina sequencing.
How does each method overcome the challenge of determining the order of nucleotides in a DNA strand?
In your answer, consider the strengths and limitations of each approach.

??? success "Solution"

    **Sanger Sequencing:**

    - **Principle**: Based on the selective incorporation of chain-terminating dideoxynucleotides (ddNTPs) by DNA polymerase during in vitro DNA replication.
    - **Method**:
        - Uses a single-stranded DNA template, a DNA primer, DNA polymerase, normal deoxynucleotides (dNTPs), and modified nucleotides (ddNTPs) that terminate DNA strand elongation.
        - Resulting DNA fragments are separated by size using capillary electrophoresis.
    - **Determining sequence:**
        - Nucleotide order is determined by the length of DNA fragments produced when chain termination occurs.
        - The fragments are separated by size, and the terminal ddNTP of each fragment indicates the nucleotide at that position.
        - The sequence is read from the shortest to the longest fragment.
    - **Strengths:**
        - High accuracy for long reads (up to ~900 base pairs).
        - Good for sequencing specific genes or DNA regions.
        - Still considered the "gold standard" for validation of other sequencing methods.
    - **Limitations:**
        - Low throughput compared to next-generation methods.
        - Higher cost per base compared to Illumina sequencing.
        - Difficulty in sequencing low-complexity regions or regions with extreme GC content.

    **Illumina Sequencing:**

    - **Principle**: Uses sequencing by synthesis (SBS) technology, where fluorescently labeled nucleotides are detected as they are incorporated into growing DNA strands.
    - **Method**:
        - DNA is fragmented and adapters are ligated to both ends of the fragments.
        - Fragments are amplified on a flow cell surface, creating clusters.
        - Sequencing occurs in cycles, where a single labeled nucleotide is added, detected, and then the label is cleaved off before the next cycle.
    - **Determining sequence:**
        - Nucleotide order is determined by detecting the specific fluorescent signal emitted when each base is incorporated.
        - Millions of clusters are sequenced simultaneously, with each cluster representing a single DNA fragment.
        - The sequence of each cluster is built up one base at a time over multiple cycles.
    - **Strengths:**
        - Very high throughput, capable of sequencing millions of fragments simultaneously.
        - Cost-effective for large-scale sequencing projects.
        - Highly accurate due to the depth of coverage (each base is sequenced multiple times).
        - Versatile, can be used for whole genome sequencing, transcriptomics, and more.
    - **Limitations:**
        - Shorter read lengths (typically 150-300 base pairs) compared to Sanger sequencing.
        - Higher error rates in homopolymer regions.
        - More complex data analysis required due to the large volume of data generated.

    **Crucial Differences:**

    -   **Scale and Throughput**: Illumina sequencing is massively parallel, allowing for much higher throughput than Sanger sequencing.
    -   **Read Length**: Sanger produces longer individual reads compared to Illumina.
    -   **Methodology**: Sanger uses chain termination, while Illumina uses sequencing by synthesis.
    -   **Application**: Sanger is better for targeted sequencing of specific genes, while Illumina is preferred for whole genome or exome sequencing.

    **Subtle Differences:**

    -   **Sample Preparation**: Illumina requires more complex library preparation, including adapter ligation and amplification.
    -   **Error Profiles**: Each method has different types of sequencing errors. Sanger tends to have higher error rates at the beginning and end of reads, while Illumina can struggle with GC-rich regions.
    -   **Data Analysis**: Illumina sequencing requires more sophisticated bioinformatics tools for data processing and analysis.
    -   **Cost Structure**: While Illumina is more cost-effective for large-scale projects, Sanger can be more economical for sequencing small numbers of samples or specific regions.
    -   **Sensitivity**: Illumina can detect low-frequency variants more easily due to its high depth of coverage, which is more challenging with Sanger sequencing.

## Q04

**Points**: 5

In Sanger sequencing, the ratio of dideoxynucleotides (ddNTPs) to deoxynucleotides (dNTPs) is crucial for successful sequencing.
Explain why this ratio is essential and predict what might happen if:

1.  The concentration of ddNTPs is too high;
2.  The concentration of ddNTPs is too low.

## Q05

**Points**: 4

Illumina sequencing uses "bridge amplification" to create clusters of identical DNA fragments.
Describe how this process works and explain why it's necessary for the Illumina sequencing method.
How does this compare to the amplification process in Sanger sequencing?

## Q06

**Points**: 4

You are designing primers for a Sanger sequencing experiment.
The region you want to sequence contains an important single nucleotide polymorphism (SNP) at position 90 from the start of your sequence of interest.
Given what you know about the typical quality of Sanger sequencing reads at different positions, where would you design your sequencing primer to bind?
Explain your reasoning.

## Q07

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

## Q08

**Points**: 4

In Illumina sequencing, adapters are ligated to DNA fragments before sequencing.

-   Explain the role of these adapters in the sequencing process.
-   How might errors in adapter ligation affect the sequencing results and downstream data analysis?
-   Describe how the design of these adapters helps prevent the formation of adapter dimers.

## Q09

**Points**: 5

Compare the structure of a typical surfactant to a phospholipid.
How do these structural differences contribute to the surfactant's ability to lyse cells?
Explain why increasing the concentration of surfactants in a lysis buffer might not always lead to better DNA yield.
What potential problems could arise from using too much surfactant?
