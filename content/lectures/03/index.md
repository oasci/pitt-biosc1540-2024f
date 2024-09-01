<h1 align="center">
<b>Lecture 03</b><br>
Quality control
</h1>
<p align="center">
<b>Date:</b> Sep 3, 2024
</p>

!!! danger "DRAFT"

    This page is a work in progress and is subject to change at any moment.

This session focuses on the critical steps of quality control and preprocessing in genomic data analysis.
We will explore the fundamentals of sequencing data formats and delve into essential techniques for assessing and improving data quality.

## Learning objectives

What you should be able to do after today's lecture:

1.  Explain the basic concepts and importance of genome assembly.
2.  Interpret FASTA and FASTQ file formats and their role in storing sequences.
3.  Perform and interpret quality control on reads using FastQC.
4.  Identify common quality issues in sequencing data and explain their impacts.
5.  Describe the process and importance of sequence trimming and filtering.

## Readings

Relevant content for today's lecture.

-   [Genome assembly](https://omics.crumblearn.org/genomics/assembly/)
-   [Assembly concepts](https://omics.crumblearn.org/genomics/assembly/concepts/) and nested content
-   [FASTA files](https://omics.crumblearn.org/appendices/file-types/fasta/)
-   [FASTQ files](https://omics.crumblearn.org/appendices/file-types/fastq/)
-   [FastQC](https://omics.crumblearn.org/genomics/assembly/qc/fastqc/) and nested content

## Presentation

-   **Live link:** [slides.com/d/HVHLMoo/live](https://slides.com/d/HVHLMoo/live)
<!-- -   **Download:** [biosc1540-l03.pdf](/lectures/03/biosc1540-l03.pdf) -->

<iframe src="https://slides.com/aalexmmaldonado/biosc1540-l03/embed?byline=hidden&share=hidden" width="100%" height="600" title="BIOSC 1540: Lecture 03" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

<!--
Key Topics

Introduction to Genome Assembly

Basic concepts and importance
Overview of assembly process
Challenges in genome assembly


Sequence File Formats

FASTA format

Structure and components
Use cases and examples


FASTQ format

Structure and components
Quality score encoding
Interpretation of quality scores




Quality Control with FastQC

Purpose and importance of quality control
Running FastQC
Interpreting FastQC reports

Per base sequence quality
Per sequence quality scores
GC content
Sequence length distribution
Overrepresented sequences
Adapter content




Common Quality Issues in Sequencing Data

Low quality bases
Adapter contamination
Overrepresented sequences
GC bias
Duplicate reads
Impact of quality issues on downstream analysis


Sequence Trimming and Filtering

Importance of trimming and filtering
Common trimming operations

Quality-based trimming
Adapter removal
Length filtering


Popular trimming tools (e.g., Trimmomatic, Cutadapt)
Balancing data quality and quantity


Preparing Data for Genome Assembly

Importance of high-quality input data
Impact of quality control on assembly outcomes
Brief overview of assembly algorithms (to be covered in detail in the next lecture)



Practical Exercises

FASTA and FASTQ File Exploration

Provide students with sample FASTA and FASTQ files
Ask them to identify key components (header, sequence, quality scores)
Have students write a simple script to count the number of sequences in each file


Running FastQC

Provide a raw sequencing dataset
Guide students through running FastQC on the command line
Have students interpret the FastQC report, identifying potential quality issues


Quality Score Analysis

Provide a FASTQ file with varying quality scores
Ask students to calculate and plot the average quality score per position
Discuss the implications of different quality score patterns


Trimming and Filtering

Introduce a dataset with known quality issues (e.g., adapter contamination, low-quality bases)
Guide students through using a trimming tool (e.g., Trimmomatic)
Have students compare FastQC reports before and after trimming


Impact of Quality Control on Assembly

Provide two datasets: one raw and one quality-controlled
Have students perform a simple assembly on both datasets using a basic assembler
Compare assembly statistics (e.g., N50, total length) between the two assemblies
Discuss the importance of quality control in genome assembly


Group Discussion: Quality Control Strategies

Divide the class into groups
Assign each group a different type of sequencing project (e.g., bacterial genome, transcriptome, metagenome)
Have groups discuss and present their proposed quality control strategy for their assigned project



These exercises will provide hands-on experience with the key concepts of the lecture, allowing students to apply their knowledge to real-world scenarios. They progress from basic file manipulation to more complex analysis and interpretation tasks, culminating in a discussion that encourages critical thinking about quality control in different contexts. -->
