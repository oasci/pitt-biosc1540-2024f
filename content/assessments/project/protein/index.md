<h1 align="center">
<b>Part 2:</b><br>
Protein structure prediction
</h1>

!!! danger "DRAFT"
    This page is a work in progress and is subject to change at any moment.

In this phase, you will predict and analyze the structure of dihydrofolate reductase (DHFR) from *S. aureus* that you identified in [Part 1](../genome/).
DHFR is an essential enzyme involved in folate metabolism and an important antibiotic target.
You will:

1.  Use multiple computational methods to predict its structure.
2.  Compare these predictions to experimental structures.
3.  Analyze the structural features and their relationship to function.
4.  Evaluate which models would be most suitable for further computational studies.

## Learning Objectives

By completing this project, you will:

-   Gain practical experience with state-of-the-art protein structure prediction tools.
-   Learn to critically evaluate and compare protein structure predictions.
-   Understand how to analyze protein structures and their functional features.
-   Develop skills in structural visualization and analysis.
-   Understand the relationship between protein structure and function.
-   Learn to make informed decisions about computational methodology.

## Instructions

Using the UniProt DHFR sequence from your [genome assembly project](../genome/), we will perform several predictions.
Instead of flooding these free servers with the same jobs, so I ran the jobs for everyone.

### I-TASSER-MTD

Job ID: [ITM552669806](https://zhanggroup.org/I-TASSER-MTD/output/ITM552669806/)

Go to the I-TASSER-MTD[^zhou2022itassermtd] [web server](https://zhanggroup.org/D-I-TASSER/) and read the [about](https://zhanggroup.org/I-TASSER-MTD/about.html) section.

!!! note "Report"

    In your report, answer the following questions:

    1.  TODO:

### D-I-TASSER

Job ID: [DIT6377](https://zhanggroup.org/D-I-TASSER/output/DIT6377/)

!!! note "Report"

    In your report, answer the following questions:

    1.  TODO:

### C-QUARK

Job ID: [QB4066](https://seq2fun.dcmb.med.umich.edu/C-QUARK/output/QB4066/)

!!! note "Report"

    In your report, answer the following questions:

    1.  TODO:

### SWISS-MODEL

Job ID: [a7BMLv](https://swissmodel.expasy.org/interactive/a7BMLv/)

SWISS-MODEL (https://swissmodel.expasy.org/)

!!! note "Report"

### AlphaFold3

AlphaFold3 (https://alphafoldserver.com/)

!!! note "Report"

    In your report, answer the following questions:

    1.  TODO:

### Experimental Structure Analysis

Obtain the experimental structure of *S. aureus* DHFR from the PDB:

TODO:

### Structural Analysis

Using PyMOL or ChimeraX, analyze the following for both predicted and experimental structures:

TODO:

<!-- REFERENCES -->

[^zhou2022itassermtd]: Zhou, X., Zheng, W., Li, Y., Pearce, R., Zhang, C., Bell, E. W., ... & Zhang, Y. (2022). I-TASSER-MTD: a deep-learning-based platform for multi-domain protein structure and function prediction. *Nature Protocols, 17*(10), 2326-2353. DOI: [10.1038/s41596-022-00728-0](https://doi.org/10.1038/s41596-022-00728-0)
