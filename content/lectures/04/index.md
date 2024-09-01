<h1 align="center">
<b>Lecture 04</b><br>
De novo genome assembly
</h1>
<p align="center">
<b>Date:</b> Sep 5, 2024
</p>

!!! danger "DRAFT"

    This page is a work in progress and is subject to change at any moment.

We will explore the intricate process of piecing together short DNA fragments to create a comprehensive genomic picture.
The session covers fundamental concepts such as contigs and scaffolds, and introduces students to key assembly algorithms, with a focus on de Bruijn graph and overlap-layout-consensus approaches.
We'll discuss the challenges posed by genomic complexities like repetitive sequences and heterozygosity, and examine strategies to overcome these obstacles.
By interpreting common quality metrics, students will develop skills in assessing assembly accuracy and completeness.
This lecture aims to provide a thorough understanding of de novo assembly techniques, their applications, and their crucial role in advancing genomic research.

## Learning objectives

What you should be able to do after today's lecture:

1.  Explain the fundamental challenge of reconstructing a complete genome.
2.  Describe and apply the principles of the greedy algorithm.
3.  Understand and construct de Bruijn graphs.
4.  Comprehend the Overlap-Layout-Consensus (OLC) approach.
5.  Discuss key challenges in de novo assembly.
6.  Interpret and calculate basic assembly quality metrics.

## Readings

Relevant content for today's lecture.

TODO:

## Presentation

TODO:
<!--
Key Topics

Introduction to De Novo Genome Assembly

Definition and importance in genomics
Comparison with reference-based assembly
Applications in various fields (e.g., metagenomics, non-model organisms)


Fundamental Concepts

Reads, k-mers, and overlaps
Contigs: definition and generation
Scaffolds: linking contigs using paired-end information
Gaps and gap closing strategies

Assembly Algorithms

De Bruijn graph approach

Graph construction and traversal
Handling of repeats and errors


Overlap-Layout-Consensus (OLC) approach

All-vs-all read alignment
Graph construction and simplification
Consensus sequence generation


Greedy algorithm approach

Principle of selecting the "best" overlap at each step
Advantages: simplicity and speed for small genomes
Limitations: sensitivity to sequencing errors and repeats


Comparison of DBG, OLC, and greedy approaches

Challenges in De Novo Assembly

Repetitive sequences and their impact
Handling heterozygosity and polyploidy
Sequencing errors and their effects on assembly
Computational resources and scalability issues


Assembly Quality Assessment

Key metrics: N50, L50, total assembly length
Completeness assessment (e.g., BUSCO analysis)
Misassembly detection and validation techniques


Impact of Sequencing Technologies

Short-read technologies (e.g., Illumina)
Long-read technologies (e.g., PacBio, Oxford Nanopore)
Hybrid assembly approaches


Practical Considerations

Choosing the right assembler for your data
Parameter optimization and its importance
Iterative assembly and refinement strategies



Practical Exercise
Students will participate in a hands-on exercise:

Examining a simple dataset of overlapping reads
Manually constructing a small de Bruijn graph
Using a basic command-line assembler on a provided dataset
Calculating and interpreting assembly quality metrics
Comparing assemblies generated from different parameters or algorithms

This exercise will reinforce the theoretical concepts and provide practical experience with genome assembly techniques. -->
