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

## Instructions

Using the UniProt DHFR sequence from your [genome assembly project](../genome/), we will perform several predictions.
Instead of flooding these free servers with the same jobs, we will all use the same outputs.

-   **[I-TASSER](https://zhanggroup.org/I-TASSER/):** [S799334](./S799334/)
-   **[D-I-TASSER](https://zhanggroup.org/D-I-TASSER/):** [DIT6377](./DIT6377/)
-   **[I-TASSER-MTD](https://zhanggroup.org/I-TASSER-MTD/):** [ITM552669806](./ITM552669806/)
-   **[C-QUARK](https://zhanggroup.org/C-QUARK/):** [QB4066](https://seq2fun.dcmb.med.umich.edu/C-QUARK/output/QB4066/)
-   **[SWISS-MODEL](https://swissmodel.expasy.org/):** [a7BMLv](https://swissmodel.expasy.org/interactive/a7BMLv/)

You will, however, need to run your own [AlphaFold3](https://alphafoldserver.com/) prediction.

!!! note "Report"

    In your report, answer the following questions:

    1.  TODO:

### Experimental Structure Analysis

Identify the optimal experimental structure of *S. aureus* DHFR from the PDB.

TODO:

### Structural Analysis

Using PyMOL or ChimeraX, analyze the following for both predicted and experimental structures:

TODO:

<!-- REFERENCES -->

[^zhou2022itassermtd]: Zhou, X., Zheng, W., Li, Y., Pearce, R., Zhang, C., Bell, E. W., ... & Zhang, Y. (2022). I-TASSER-MTD: a deep-learning-based platform for multi-domain protein structure and function prediction. *Nature Protocols, 17*(10), 2326-2353. DOI: [10.1038/s41596-022-00728-0](https://doi.org/10.1038/s41596-022-00728-0)
