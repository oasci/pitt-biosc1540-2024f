<h1 align="center">
A03
</h1>

<p style="text-align: center;">
    <object hspace="50">
        <strong>Due</strong></a>: Sep 19, 2024 by 11:59 p.m.
    </object>
    <object hspace="50">
        <strong>Points</strong></a>: 60
    </object>
</p>

## Q01

Explain the difference between structural and functional annotation in gene prediction.
Why are both important in genomics research?

??? success "Solution"

    **Structural Annotation** refers to the identification and mapping of the physical components of the genome.
    This includes delineating the locations of genes, exons, introns, promoters, and other regulatory elements.
    The primary objective of structural annotation is to construct a comprehensive framework that outlines the architecture of the genome.
    Techniques such as sequence alignment, ab initio prediction algorithms, and comparative genomics are commonly employed to accurately predict gene structures.
    For instance, structural annotation would determine where a gene begins and ends, the arrangement of its coding sequences, and the presence of any non-coding regions within the gene.

    On the other hand, **Functional Annotation** delves into assigning biological roles and characteristics to the identified genomic elements.
    Once the structural components are mapped, functional annotation seeks to elucidate the roles of these genes and regulatory regions in cellular processes, pathways, and overall organismal biology.
    This involves predicting gene functions based on sequence similarity to known genes, identifying protein domains, inferring metabolic pathways, and associating genes with phenotypic traits or diseases.
    Tools such as gene ontology (GO) databases, pathway analysis software, and protein interaction networks are integral to functional annotation efforts.

    The distinction between the two lies in their focus: structural annotation is concerned with "where" genes and elements are located within the genome, while functional annotation addresses "what" these genes and elements do biologically.

    Both types of annotation are indispensable in genomics research for several reasons:

    1.  **Comprehensive Genome Understanding**: Structural annotation provides the necessary map of the genome, serving as a foundation upon which functional insights are built.
        Without knowing the precise locations and structures of genes, it would be challenging to investigate their functions effectively.
    2.  **Facilitating Downstream Analyses**: Functional annotation enables researchers to interpret the biological significance of genetic variations, identify potential targets for therapeutic intervention, and understand the molecular mechanisms underlying various traits and diseases.
    3.  **Enhancing Comparative Genomics**: By combining structural and functional annotations, scientists can perform comparative analyses across different species, revealing evolutionary conservation and divergence in gene structure and function.
    4.  **Supporting Personalized Medicine**: Accurate annotations are crucial for identifying genetic variants that may influence an individual's response to drugs or susceptibility to diseases, thereby advancing personalized healthcare strategies.

## Q02

Compare and contrast global and local sequence alignment.
Provide example(s) of when each would be more appropriate to use.

??? success "Solution"

    In the study of bioinformatics and computational biology, **sequence alignment** is a critical tool used to identify regions of similarity between biological sequences, which can indicate functional, structural, or evolutionary relationships.
    There are two primary types of sequence alignment: **global** and **local**.
    Understanding the distinctions between these two methods is essential for selecting the appropriate approach based on the specific objectives of a genomic analysis.

    **Global alignment** involves aligning two sequences from end to end, encompassing their entire lengths.
    This method attempts to optimize the alignment across the whole sequence, ensuring that every nucleotide or amino acid is included in the comparison.
    Global alignment is particularly effective when the sequences being compared are of similar length and are expected to be largely similar across their entire span.

    One of the most widely used algorithms for global alignment is the **Needleman-Wunsch algorithm**, which employs dynamic programming to find the optimal alignment by scoring matches, mismatches, and gaps.
    The algorithm constructs a matrix to evaluate all possible alignments and determines the one with the highest score, representing the best overall alignment between the two sequences.

    Global alignment is most suitable when comparing **orthologous genes**—genes in different species that originated from a common ancestral gene and retain similar functions.
    For instance, aligning the entire coding sequences of the hemoglobin gene from humans and mice can provide insights into evolutionary conservation and functional similarities.
    Since these genes are expected to be similar in length and structure, a global alignment ensures that the entire gene sequences are compared comprehensively.

    In contrast, **local alignment** focuses on identifying the most similar subsequences within two larger sequences.
    Instead of attempting to align the entire length of both sequences, local alignment seeks regions of high similarity, which may be significantly shorter than the full length of the sequences.
    This approach is advantageous when the sequences being compared contain conserved domains or motifs amidst regions of divergence.

    The **Smith-Waterman algorithm** is the standard method for performing local alignments.
    Like its global counterpart, it uses dynamic programming but differs in that it allows for the identification of optimal local matches by resetting the scoring matrix when negative scores are encountered.
    This enables the algorithm to locate the best matching regions without being penalized by dissimilar regions elsewhere in the sequences.

    Local alignment is particularly useful when comparing sequences that may contain **functional domains** or **motifs** within otherwise divergent regions. For example, when aligning a protein sequence to a large genomic DNA sequence to identify potential coding regions, local alignment can pinpoint specific exons or functional domains without requiring the entire genomic sequence to match the protein. Another common application is in the identification of conserved motifs within regulatory regions of genes across different species, where only certain segments are expected to be conserved.

## Q03

Describe the role of gap penalties in sequence alignment algorithms.
How do different types of gap penalties (e.g., linear vs. affine) affect alignment results?

??? success "Solution"

    Gap penalties are scoring mechanisms that penalize the introduction of gaps—insertions or deletions—during the alignment process.
    These penalties are essential for balancing the alignment to reflect biological realities, such as insertions or deletions that occur during evolution or genetic variation.
    Understanding the role and types of gap penalties is fundamental to achieving biologically meaningful and accurate alignments.

    **Role of Gap Penalties in Sequence Alignment**

    When aligning two sequences, gaps are introduced to account for insertions or deletions that allow for a better overall alignment of matching regions.
    However, without appropriate penalties, algorithms might introduce excessive gaps, leading to unrealistic alignments.
    Gap penalties serve to:

    1.  **Discourage Excessive Gaps**: By assigning a cost to each gap introduced, the algorithm is incentivized to minimize the number of gaps, promoting alignments that require fewer insertions or deletions.
    2.  **Reflect Biological Reality**: Different types of gaps (e.g., single nucleotide insertions versus large indels) have varying biological implications.
        Gap penalties help model these differences by assigning appropriate costs.
    3.  **Optimize Alignment Scores**: Gap penalties are integrated into the scoring system of alignment algorithms to ensure that the overall alignment score accurately reflects the quality of the alignment, balancing matches, mismatches, and gaps.

    **Types of Gap Penalties**

    Gap penalties can be broadly categorized into two types: **linear** and **affine**.
    Each type influences the alignment results differently based on how gaps are penalized.

    <u>Linear Gap Penalties</u>

    **Linear gap penalties** assign a fixed cost for each gap position, regardless of the length of the gap. The total penalty for a gap of length $k$ is simply $\text{gap penalty} \times k$.

    - **Mathematical Representation**: If the penalty per gap is $g$, then a gap of length $k$ incurs a penalty of $g \times k$.

    - **Equal Penalization**: Each additional gap position is equally penalized, making longer gaps increasingly costly.
    - **Alignment Characteristics**: This approach tends to favor multiple shorter gaps over fewer longer ones because the penalty accumulates linearly with gap length.

    Linear gap penalties are suitable for alignments where insertions and deletions are expected to occur sporadically and independently throughout the sequence, without forming extended indels.

    <u>Affine Gap Penalties</u>

    **Affine gap penalties** differentiate between the initiation and extension of gaps by assigning separate penalties for gap opening and gap extension. Typically, the penalty is structured as:

    $$
    \text{Total Gap Penalty} = \text{Gap Open Penalty} + (\text{Gap Extend Penalty} \times (k - 1))
    $$

    where $k$ is the length of the gap.

    If the gap opening penalty is $g_o$ and the gap extension penalty is $g_e$, then a gap of length $k$ incurs a penalty of $g_o + g_e \times (k - 1)$.

    - **Differentiated Penalization**: Opening a new gap incurs a higher penalty, while extending an existing gap is less costly.
    - **Alignment Characteristics**: This approach favors the creation of longer, contiguous gaps over multiple shorter gaps because the relative cost of extending a gap is lower than opening a new one.

    Affine gap penalties are ideal for alignments where insertions or deletions tend to occur in blocks or segments, reflecting scenarios such as exon-intron boundaries in genes or structural variations in genomes.

    **Comparative Effects on Alignment Results**

    The choice between linear and affine gap penalties significantly influences the resulting alignment:

    | **Aspect**                | **Linear Gap Penalty**                                  | **Affine Gap Penalty**                                    |
    |---------------------------|---------------------------------------------------------|-----------------------------------------------------------|
    | **Penalty Structure**     | Fixed cost per gap position                            | Higher cost for gap initiation, lower cost for extension  |
    | **Tendency in Alignments**| Favors multiple short gaps                             | Favors fewer, longer gaps                                 |
    | **Biological Relevance**  | Suitable for random, independent indels                 | Suitable for grouped indels or structural variations      |
    | **Algorithm Complexity** | Simpler to implement and compute                        | More complex due to separate handling of gap openings and extensions |
    | **Use Cases**             | Aligning sequences with scattered mutations             | Aligning sequences with potential large insertions/deletions or domain rearrangements |

    **Illustrative Example**

    Consider aligning two sequences where one sequence has a segment that is entirely inserted compared to the other. Using a **linear gap penalty**, the algorithm might introduce multiple single-nucleotide gaps to accommodate the insertion, incurring a penalty for each gap.
    In contrast, with an **affine gap penalty**, the algorithm is more likely to introduce a single contiguous gap covering the entire inserted segment, resulting in a lower total penalty and a more biologically plausible alignment.

## Q04

Given the following DNA sequences:

-   `ATGCACTAGCTA`
-   `ATGCTACGTA`

Perform the following tasks:

**a)** Perform a global alignment using the Needleman-Wunsch algorithm.
Use a scoring system of +1 for matches, -1 for mismatches, and -2 for gaps.
Show your work, including the scoring matrix and traceback path.

**b)** Using the same sequences and scoring system as above, perform a local alignment using the Smith-Waterman algorithm.
Show your work, including the scoring matrix and traceback path.

**c)** Compare your results from the global and local alignments.
What differences do you notice?
Discuss the biological implications of these differences.

## Q05

**a)** List and briefly describe three key challenges in prokaryotic gene annotation.

**b)** What role do ribosomal binding sites (RBS) play in prokaryotic gene prediction?
How are they typically identified?

**c)** Explain the importance of identifying regulatory elements in gene annotation.
Give two examples of regulatory elements and their functions.

## Q06

**a)** What is the significance of using multiple k-mer sizes in SPAdes?
How does this strategy improve assembly quality?

**b)** What are "bulges" and "tips" in the context of the SPAdes assembly graph?
How does SPAdes handle these structures?

**c)** Explain the concept of "paired-end reads" and how SPAdes utilizes this information to improve assembly.

## Q07

**a)** You are assembling a bacterial genome using SPAdes.
The assembly results in several large contigs and many small contigs.
What might this indicate about the genome or sequencing data, and what steps could you take to improve the assembly?

**b)** Describe how you would use the SPAdes assembly graph visualization tool Bandage to analyze the quality of your assembly.
What features would you look for?

## Q08

**a)** You are given the following bacterial DNA sequence:
`5' ATGCATGCTAGCTAATGCCCGGGTAACCCATGA 3'`
Identify all possible ORFs in this sequence (consider both strands).
How would you determine which ORF is most likely to be a real gene?

**b)** Compare and contrast the challenges of identifying genes in GC-rich vs. AT-rich prokaryotic genomes.
How might these differences affect gene prediction strategies?

## Q09

In gene prediction, coding scores are often used to identify potential protein-coding regions.
One method to calculate coding scores involves analyzing the frequency of hexamers (6-nucleotide sequences) in known genes versus the entire genome.
Given the following information:

-   Hexamer: `ATGGCC`
-   Frequency in known genes ($G$): 0.015
-   Frequency in the whole genome ($B$): 0.005

**a)** Calculate the coding score $C(w)$ for this hexamer using the formula:

$$
C(w) = \log \left(\frac{G(w)}{B(w)} \right)
$$

Where $G(w)$ is the frequency of the word in genes, and $B(w)$ is the frequency in the whole genome.

**b)** Interpret the result.
What does the score indicate about this hexamer?

**c)** If you found this hexamer in an uncharacterized region of DNA, how might this score influence your assessment of whether this region is likely to be protein-coding?

## Q10

You are analyzing a short DNA sequence to determine if there is likely to be a protein-coding gene.

-   Given DNA sequence: `ATATGCATGCTTAGCTTA`

You have a table of pre-calculated coding scores for all possible hexamers based on known genes in the bacteria's genome.

| Hexamer | Score | Hexamer | Score |
|---------|-------|---------|-------|
| ATATGC  | -0.2  | CATGCT  | 1.2   |
| TATGCA  | -0.4  | ATGCTT  | 0.7   |
| ATGCAT  | 0.8   | TGCTTA  | -0.1  |
| TGCATG  | -0.2  | GCTTAG  | 0.3   |
| GCATGC  | 0.5   | CTTAGC  | 0.6   |
| TTAGCT  | -0.3  | TAGCTT  | -0.5  |
| AGCTTA  | 0.1   |         |       |

**a)** Calculate the overall coding score for the **gene** in this DNA sequence.
To do this:

-   Determine the score for each overlapping hexamer in the gene.
-   Sum these scores to get the total coding score for the gene.

Remember that you [shift over one codon a time](https://slides.com/aalexmmaldonado/biosc1540-l05#/4/6).
(I had to [read their C code](https://github.com/hyattpd/Prodigal/blob/c1e2d361479cc1b18175ea79ebd8ff10411c46cb/node.c#L325-L367) to figure this out.)

**b)** What is the average coding score per hexamer for this sequence?

**c)** Based on your results, do you think this gene is likely to be protein-coding?
Explain your reasoning.

**d)** Discuss potential limitations of using this hexamer-based coding score approach for gene prediction.
What factors might lead to false positives or false negatives?

## Programming+

These problems are not required and will not impact your BIOSC 1540 grade.
The instructor will assess these separately to validate correctness without an assigned grade.
Thus, you may work on these problems individually or in a team-based setting and "due" by the end of the semester.
Happy coding!

**Acceptable languages**: Python v3.10+, Rust v1.80+, Mojo v24.4+

!!! success "Rewards"
    Engaging with these optional programming problems offers several valuable academic and professional growth opportunities.

    -   Consistent engagement with these **Programming+** problems will allow me to write more detailed, compelling recommendation letters highlighting your computational skills.
    These personalized letters can significantly boost your applications for future academic programs, internships, or job opportunities.
    -   If there is enough interest, optional Friday recitations will be provided.
    This will give you individualized attention to accelerate learning and actionable feedback on your code and problem-solving approaches.
    -   Exceptional solutions may be featured on our course website with the students' permission. This is a way for us to recognize and appreciate your hard work and dedication to these problems.

!!! note
    These problems would be similar to ones given in a major-only version of the class.
    Although, there would be more relevant instructions during class and would be given more than a week to complete.

### P01

Implement the Needleman-Wunsch algorithm for global sequence alignment.

**a)** Write a function `needleman_wunsch(seq1, seq2, match_score, mismatch_score, gap_penalty)` that takes two sequences and scoring parameters as input and returns the optimal alignment score and the aligned sequences.

**b)** Test your implementation with the sequences from Q04 in the assignment:

-   `ATGCACTAGCTA`
-   `ATGCTACGTA`

Use a match score of +1, mismatch score of -1, and gap penalty of -2.

**c)** Add functionality to visualize the scoring matrix and the traceback path.

### P02

Implement the Smith-Waterman algorithm for local sequence alignment.

**a)** Write a function `smith_waterman(seq1, seq2, match_score, mismatch_score, gap_penalty)` that takes two sequences and scoring parameters as input and returns the optimal local alignment score and the aligned subsequences.

**b)** Test your implementation with the same sequences from P01.

**c)** Add functionality to visualize the scoring matrix and the traceback path, highlighting the highest-scoring local alignment.

### P03

Create a script to find all possible Open Reading Frames (ORFs) in a given DNA sequence.

**a)** Write a function `find_orfs(sequence, min_length=100)` that takes a DNA sequence as input and returns a list of all ORFs longer than the minimum length. Consider both strands of the DNA.

**b)** Implement a function to translate the ORFs into amino acid sequences.

**c)** Test your implementation with the sequence from Q08 in the assignment: `5' ATGCATGCTAGCTAATGCCCGGGTAACCCATGA 3'`

**d)** Add functionality to identify the longest ORF and potential start codons (ATG) within the ORFs.

### P04

Implement a Python script to calculate coding scores for a DNA sequence based on hexamer frequencies.

**a)** Write a function `calculate_coding_score(sequence)` that takes a DNA sequence and returns the overall coding score for the sequence.

Use the following function to compute the hexamer scores.

```python
def compute_hexamer_score(hexamer):
    """
    Compute a score for a given hexamer based on its nucleotide composition.

    This function uses a simple scoring system based on GC content and specific dinucleotide frequencies.

    Args:
        hexamer (str): A string of 6 nucleotides (A, T, C, or G)

    Returns:
        The computed score for the hexamer
    """
    if len(hexamer) != 6 or not all(base in 'ATCG' for base in hexamer.upper()):
        raise ValueError("Input must be a string of 6 nucleotides (A, T, C, or G)")

    hexamer = hexamer.upper()

    # Base scores
    base_scores = {'A': 1, 'T': 1, 'C': 2, 'G': 2}

    # Dinucleotide bonus scores
    dinucleotide_bonus = {'CG': 0.5, 'GC': 0.5, 'AT': -0.3, 'TA': -0.3}

    # Calculate base score
    score = sum(base_scores[base] for base in hexamer)

    # Add dinucleotide bonuses
    for i in range(5):
        dinucleotide = hexamer[i:i+2]
        if dinucleotide in dinucleotide_bonus:
            score += dinucleotide_bonus[dinucleotide]

    # Normalize score
    score = score / 6

    return round(score, 2)

# Example usage:
print(compute_hexamer_score('ATGCAT'))  # Output: 1.62
print(compute_hexamer_score('CGCGCG'))  # Output: 2.5
print(compute_hexamer_score('ATATAG'))  # Output: 0.95
```

**b)** Implement the sliding window approach, shifting by one codon (3 nucleotides) at a time, as mentioned in Q10 of the assignment.

**c)** Test your implementation with the sequence and hexamer scores from Q10.
