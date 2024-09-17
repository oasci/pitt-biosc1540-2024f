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

## Q02

Compare and contrast global and local sequence alignment.
Provide example(s) of when each would be more appropriate to use.

## Q03

Describe the role of gap penalties in sequence alignment algorithms.
How do different types of gap penalties (e.g., linear vs. affine) affect alignment results?

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
Which ORF is most likely to be a real gene and why?

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
