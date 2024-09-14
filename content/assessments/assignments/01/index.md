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

??? success "Solution"

    The optimal ratio of ddNTPs to dNTPs in Sanger sequencing is critical for generating a balanced distribution of fragment lengths.
    This ratio is essential for the following reasons:

    -   **Fragment Distribution**: The ratio ensures that chain termination occurs randomly at different positions along the template DNA, producing a set of fragments that differ in length by one nucleotide.
    -   **Read Length**: It allows for the generation of fragments covering the entire sequence of interest, typically up to 900-1000 base pairs.

    **If the concentration of ddNTPs is too high:**

    -   **Short Fragments**: There would be an overabundance of short DNA fragments due to frequent early termination of DNA synthesis.
    -   **Loss of Long Reads**: Longer fragments would be underrepresented or absent, leading to incomplete sequence information for the latter part of the template.
    -   **Reduced Overall Signal**: The signal intensity would decrease rapidly along the length of the sequence, making it difficult to read bases accurately beyond the first 100-200 nucleotides.

    **If the concentration of ddNTPs is too low:**

    -   **Long Fragments**: There would be an overabundance of long DNA fragments due to infrequent termination of DNA synthesis.
    -   **Loss of Short Reads**: Shorter fragments would be underrepresented, leading to poor sequence quality at the beginning of the read.
    -   **Weak Signal for Short Fragments**: The signal intensity for the first part of the sequence would be very low, making it difficult to accurately determine the initial bases.

## Q05

**Points**: 4

Illumina sequencing uses "bridge amplification" to create clusters of identical DNA fragments.
Describe how this process works and explain why it's necessary for the Illumina sequencing method.
How does this compare to the amplification process in Sanger sequencing?

??? success "Solution"

    Bridge amplification is a crucial step in Illumina sequencing that creates clusters of identical DNA fragments on the surface of a flow cell.
    The process works as follows:

    1. **Flow Cell Preparation**: The flow cell surface is coated with two types of oligonucleotide adapters.
    2. **DNA Fragment Attachment**: Single-stranded DNA fragments with adapters at both ends are added to the flow cell. These fragments bind randomly to the complementary adapters on the surface.
    3. **Bridge Formation**: The free end of a bound DNA fragment bends over and hybridizes to a nearby complementary adapter on the surface, forming a "bridge."
    4. **Amplification**: DNA polymerase creates a complementary strand, forming a double-stranded bridge.
    5. **Denaturation**: The double-stranded bridge is denatured, resulting in two single-stranded copies of the molecule tethered to the flow cell surface.
    6. **Repeated Cycles**: Steps 3-5 are repeated multiple times, with each fragment amplifying into a distinct cluster.
    7. **Reverse Strand Removal**: One strand (usually the reverse strand) is cleaved and washed away, leaving clusters of single-stranded, identical DNA fragments.

    Bridge amplification is necessary for Illumina sequencing for several reasons:

    1. **Signal Amplification**: It creates thousands of identical copies of each DNA fragment, significantly amplifying the signal for detection during sequencing.
    2. **Clonal Clusters**: Each cluster represents a single original DNA fragment, ensuring that the sequencing signal comes from identical molecules.
    3. **Parallelization**: Millions of clusters can be generated on a single flow cell, allowing for massive parallelization of sequencing reactions.
    4. **Improved Accuracy**: The clonal nature of each cluster helps to reduce sequencing errors by providing multiple identical copies for each base call.
    5. **High Throughput**: The dense arrangement of clusters on the flow cell surface enables high-throughput sequencing.

    The amplification process in Illumina sequencing differs significantly from that used in Sanger sequencing:

    1.  **Method**:
        - Illumina: Uses solid-phase bridge amplification on a flow cell surface.
        - Sanger: Typically uses solution-phase PCR or cloning in bacterial vectors.
    2. **Scale**:
        - Illumina: Massively parallel, creating millions of clusters simultaneously.
        - Sanger: Limited to amplifying one DNA fragment at a time.
    3. **Product**:
        - Illumina: Generates clonal clusters of single-stranded DNA.
        - Sanger: Produces a population of double-stranded DNA fragments.
    4. **Locality**:
        - Illumina: Amplification occurs in a fixed location on the flow cell.
        - Sanger: Amplification occurs in solution.

## Q06

**Points**: 4

You are designing primers for a Sanger sequencing experiment.
The region you want to sequence contains an important single nucleotide polymorphism (SNP) at position 90 from the start of your sequence of interest.
Given what you know about the typical quality of Sanger sequencing reads at different positions, where would you design your sequencing primer to bind?
Explain your reasoning.

??? success "Solution"

    Before designing the primer, it's crucial to understand the typical quality pattern of Sanger sequencing reads:

    -   **Start of the read** (first ~15-35 bases): Often low quality due to primer binding and initial reaction instability.
    -   **Middle section** (~35-700 bases): Highest quality, with accurate base calls.
    -   **End of the read** (beyond ~700-900 bases): Decreasing quality due to signal decay and increased noise.

    Given that the SNP of interest is at position 90 from the start of the sequence, the ideal primer design would place this SNP within the high-quality middle section of the sequencing read.
    Specifically, design the primer to bind approximately 40-50 bases upstream of the SNP.

    **Rationale**:

    - This placement allows for the initial low-quality bases (first 15-35) to be read before reaching the SNP.
    - It positions the SNP at around base 130-140 in the sequencing read (40-50 bases for primer + 90 bases to SNP).
    - This location falls well within the high-quality middle section of a typical Sanger sequencing read.

    **Benefits of this design**:

    - Ensures high-quality base calls around the SNP position.
    - Provides sufficient context before and after the SNP for accurate analysis.
    - Allows for potential upstream sequence verification if needed.

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

??? success "Solution"
    The observation of multiple overlapping peaks at several positions in a Sanger sequencing chromatogram, persisting even with newly designed primers, can be attributed to various molecular and genomic phenomena.
    Given the context of a wild plant population in an area of high biodiversity, several plausible explanations warrant consideration.

    **High Heterozygosity Due to Outcrossing**

    In outcrossing plant species, high levels of heterozygosity can accumulate, especially in regions with large, diverse populations.

    -   Molecular Mechanism
        -   Plants in the population cross-pollinate, leading to offspring with diverse allelic combinations.
        -   Over generations, multiple alleles for each gene can persist in the population.
        -   Individual plants may carry two or more distinct alleles for many genes.
    -   How it Causes Overlapping Peaks
        -   When sequencing a heterozygous individual, both alleles are amplified and sequenced.
        -   Differences between alleles result in double peaks at heterozygous positions.
    -   Supporting Evidence
        -   Consistent with a wild population in a biodiverse area.
        -   Might be particularly noticeable if the population has high genetic diversity.

    **Allopolyploidy**

    Allopolyploidy results from hybridization between two or more different species, followed by chromosome doubling.

    -   Mechanism
        -   Hybridization occurs between two related species (e.g., Species A: AA and Species B: BB).
        -   The resulting hybrid (AB) undergoes chromosome doubling to form an allopolyploid (AABB).
        -   The allopolyploid now contains two sets of similar but not identical genomes.
    -   How it Causes Overlapping Peaks
        -   Multiple similar copies of each gene are present in the genome.
        -   During PCR and sequencing, all copies are amplified and sequenced simultaneously.
        -   Where sequences differ between copies, multiple bases are incorporated, resulting in overlapping peaks.
    -   Supporting Evidence
        -   Consistent with the high biodiversity and presence of closely related species in the area.
        -   Explains the persistence of the pattern with new primers.

## Q08

**Points**: 4

In Illumina sequencing, adapters are ligated to DNA fragments before sequencing.

-   Explain the role of these adapters in the sequencing process.
-   How might errors in adapter ligation affect the sequencing results and downstream data analysis?
-   Describe how the design of these adapters helps prevent the formation of adapter dimers.

??? success "Solution"
    Adapters in Illumina sequencing play several crucial roles throughout the sequencing workflow:

    -   Enabling Bridge Amplification
        -   Adapters contain sequences complementary to oligonucleotides on the flow cell surface.
        -   This allows DNA fragments to bind to the flow cell and undergo bridge amplification.
    -   Priming for Sequencing
        -   Adapters include binding sites for sequencing primers.
        -   This enables the initiation of sequencing reactions for both forward and reverse reads.
    -   Index Sequences
        -   Adapters often contain index sequences (barcodes).
        -   These allow for multiplexing, where multiple samples can be sequenced in the same lane and later demultiplexed.
    -   Facilitating Paired-End Sequencing
        -   In paired-end sequencing, adapters at both ends of the fragment allow sequencing from both directions.

    Errors in adapter ligation can have several negative effects on sequencing results and downstream analysis:

    -   Reduced Sequencing Efficiency
        -   Fragments without properly ligated adapters won't bind to the flow cell, reducing the overall yield.
    -   Chimeric Reads
        -   Improper ligation can lead to chimeric fragments where adapters join unrelated DNA fragments.
        -   This results in chimeric reads that can complicate assembly and alignment processes.
    -   Biased Representation
        -   Inefficient ligation can lead to under-representation of certain sequences, especially those with extreme GC content.
        -   This introduces bias in quantitative analyses like RNA-Seq or ChIP-Seq.
    -   Index Hopping
        -   In multiplexed samples, errors in index sequence ligation can lead to index hopping.
        -   This results in reads being assigned to the wrong sample during demultiplexing.
    -   Reduced Read Quality
        -   Partially ligated adapters can lead to poor quality reads, especially at the beginning or end of reads.
    -   Complications in Data Analysis
        -   Adapter contamination in reads can interfere with alignment, assembly, and variant calling.
        -   It necessitates more stringent quality control and adapter trimming steps in data preprocessing.
    -   False Positive Variant Calls
        -   Adapter sequences present in reads can be misinterpreted as real genomic sequence, leading to false positive variant calls.

    Illumina adapters are designed with several features to minimize the formation of adapter dimers:

    -   Y-shaped Adapters
        -   Adapters are often designed with a Y-shape, where only a portion of the adapter is double-stranded.
        -   This reduces the likelihood of adapters ligating to each other.
    -   Sequence Design
        -   Adapter sequences are designed to minimize complementarity between different adapter molecules.
        -   This reduces the likelihood of base-pairing between adapters.
    -   PCR Suppression Effect
        -   Some adapter designs incorporate sequences that, when dimerized, form strong hairpin structures.
        -   These structures are poor substrates for PCR amplification, suppressing the amplification of adapter dimers.

## Q09

**Points**: 5

Compare the structure of a typical surfactant to a phospholipid.
How do these structural differences contribute to the surfactant's ability to lyse cells?
Explain why increasing the concentration of surfactants in a lysis buffer might not always lead to better DNA yield.
What potential problems could arise from using too much surfactant?

??? success "Solution"

    **Structural Comparison: Surfactant vs. Phospholipid**

    Surfactants and phospholipids, while both amphipathic molecules, exhibit distinct structural characteristics that significantly influence their behavior in biological systems.
    A typical surfactant consists of a hydrophilic head group and a single hydrophobic tail.
    The head group can vary in its chemical nature, being ionic (either anionic or cationic), nonionic, or zwitterionic.
    The hydrophobic portion is usually a single tail, often composed of a hydrocarbon chain.
    Common examples of surfactants include sodium dodecyl sulfate (SDS), Triton X-100, and CTAB.

    In contrast, phospholipids possess a more complex structure.
    They are composed of a hydrophilic head group and two hydrophobic tails.
    The head group typically contains a phosphate group and may include other molecules, such as choline in the case of phosphatidylcholine.
    The hydrophobic portion consists of two tails, usually fatty acid chains.
    Examples of phospholipids include phosphatidylcholine, phosphatidylethanolamine, and phosphatidylserine.

    The key structural differences between surfactants and phospholipids lie in several aspects.
    Firstly, the number of hydrophobic tails differs, with surfactants typically having one and phospholipids having two.
    Secondly, the head group composition of surfactants is generally simpler compared to the more complex phosphate-containing heads of phospholipids.
    Thirdly, surfactants are generally smaller molecules than phospholipids in terms of molecular weight.
    Lastly, the overall geometry differs, with surfactants often having a conical shape, while phospholipids tend to be more cylindrical.

    **Structural Differences and Cell Lysis Ability**

    The structural disparities between surfactants and phospholipids significantly contribute to the surfactant's superior ability to lyse cells.
    The single tail and conical shape of surfactants allow them to insert themselves more easily between the phospholipids in the cell membrane.
    This insertion causes membrane curvature and eventually leads to the formation of mixed micelles containing both surfactants and membrane lipids, effectively disrupting the membrane structure.

    Surfactants generally have a lower Critical Micelle Concentration (CMC) than phospholipids.
    At concentrations above the CMC, surfactants form micelles more readily, which enhances their ability to solubilize membrane components.
    The simpler structure of surfactants also allows them to interact more easily with membrane proteins, potentially denaturing them and further destabilizing the membrane.

    The smaller size of surfactants enables them to diffuse and equilibrate across the membrane more quickly than phospholipids.
    Additionally, the variety of head groups available in surfactants (ionic, nonionic, zwitterionic) allows for the selection of surfactants that can optimally interact with different types of cell membranes, making them versatile tools for cell lysis in various applications.

    **Surfactant Concentration and DNA Yield**

    While surfactants are crucial for cell lysis, increasing their concentration in a lysis buffer might not always lead to better DNA yield.
    This counterintuitive phenomenon can be attributed to several factors.

    Excessive surfactant concentrations can lead to extensive protein denaturation.
    While some protein denaturation is necessary for DNA release, overly denatured DNA-binding proteins can potentially lead to DNA degradation.

    At high concentrations, surfactants can interact directly with DNA, potentially causing structural changes or precipitation, which can reduce yield.
    Above the CMC, additional surfactants form micelles rather than contributing to lysis, providing diminishing returns.
    Excessively high surfactant concentrations can also disrupt the careful balance of other buffer components, potentially affecting pH or ionic strength, which are crucial for optimal DNA extraction.

    Furthermore, high surfactant concentrations can interfere with subsequent purification steps or analytical techniques, indirectly reducing the final DNA yield.
    The presence of excess surfactants may complicate downstream processes, leading to losses during purification or hindering accurate quantification of the extracted DNA.

    **Potential Problems from Excessive Surfactant Use**

    Using too much surfactant in cell lysis procedures can lead to several issues that may compromise the quality and quantity of the extracted DNA.
    Excessive surfactant can lead to DNA damage, including denaturation or fragmentation, especially in combination with other factors like heat or mechanical stress.
    Over-solubilization of cellular proteins can lead to higher protein contamination in the DNA extract, necessitating additional purification steps.

    Residual surfactants can inhibit PCR and other enzymatic reactions, affecting downstream applications.
    High surfactant concentrations can interfere with alcohol-based DNA precipitation methods, reducing recovery.
    Excessive surfactant can also cause problematic foam formation during lysis and extraction procedures, making sample handling more difficult.
