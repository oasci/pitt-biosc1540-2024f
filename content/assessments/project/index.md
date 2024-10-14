<h1 align="center">
<b>Project:</b><br>
Computer-Aided Drug Design for a Novel Pathogen
</h1>

This project aims to simulate the process of computer-aided drug design (CADD) for a novel pathogen, giving students hands-on experience with key bioinformatics and cheminformatics tools used in early-stage drug discovery.
Students will work through a complete workflow&mdash;from raw sequencing data to potential drug candidates&mdash;mirroring the steps researchers might take when confronted with a new pathogenic threat.

## Learning Objectives

By completing this project, students will:

-   Gain practical experience with a complete CADD workflow.
-   Understand how genomic data informs drug target selection.
-   Learn to use and interpret results from state-of-the-art structure prediction tools.
-   Develop skills in molecular docking and virtual screening.
-   Critically analyze results at each stage of the drug discovery pipeline.

## Overview

### Genomic Data Processing and Analysis

This phase begins with raw Illumina sequencing reads (FASTQ format) from a provided SRA accession number [^bruce2022shared].
Students will perform quality control using tools like FastQC to ensure high-quality data for assembly.
They will then assemble the pathogen's genome using appropriate assembly tools such as SPAdes.
Following assembly, gene prediction and annotation will be done using tools like Prokka.
Students will extract coding sequences, translate them to amino acid sequences, and perform functional annotation using tools such as InterProScan.
This process will help identify potential drug targets based on function, essentiality, and other relevant criteria.

Students will use [Galaxy](https://usegalaxy.org/).

### Protein Structure Prediction

Students will use the amino acid sequences of selected target proteins to predict their 3D structures using AlphaFold3.
This step introduces students to state-of-the-art protein structure prediction methods and the challenges of working with novel proteins.
Students will learn to interpret AlphaFold's confidence metrics and structural output.
They will also compare the predicted structures to known experimental structures in the Protein Data Bank (PDB) to assess the quality of the predictions and gain insights into the structural features of their targets.
This comparison may involve structural alignment and analysis of key functional regions.

Students will use the [AlphaFold web server](https://alphafoldserver.com/).

### Virtual Screening via Molecular Docking

In this final phase, students will screen a provided chemical library virtually against their predicted protein structures.
This process begins with preparing the target protein structures for docking, including defining the binding site.
Students will then set up and run the virtual screening, learning about the principles of molecular docking and scoring functions.
After the screening, they will analyze the docking results to identify promising hit compounds.
This analysis may include examining binding poses, interaction patterns, and docking scores.
Students will learn to critically evaluate virtual screening results and understand their role in the early stages of drug discovery.

Students will use [MolModa](https://durrantlab.pitt.edu/molmoda/).

## Deliverables

Students will compile and analyze their results from each stage throughout the project.
Students will learn to integrate information from multiple computational approaches to make informed decisions about potential drug targets and hit compounds.
They will prepare a final report summarizing their methods, results, and conclusions, demonstrating their understanding of the computer-aided drug design process.

-   Assembled and annotated genome.
-   Predicted 3D structures of selected target proteins.
-   Docking results and analysis of top-hit compounds.
-   Final report summarizing methods, results, and conclusions.

<!-- REFERENCES -->

[^bruce2022shared]: Bruce, S. A., Smith, J. T., Mydosh, J. L., Ball, J., Needle, D. B., Gibson, R., & Andam, C. P. (2022). Shared antibiotic resistance and virulence genes in Staphylococcus aureus from diverse animal hosts. Scientific Reports, 12(1), 4413. DOI: [10.1038/s41598-022-08230-z](https://doi.org/10.1038/s41598-022-08230-z)
