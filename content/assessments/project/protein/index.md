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

-   **[I-TASSER](https://zhanggroup.org/I-TASSER/)** (Job ID [S799334](./S799334/)): A threading-based method for predicting protein structures and functions by assembling models from template fragments and refining them iteratively; it is robust for cases with moderate to strong homologous templates and provides functional annotations, often generating medium-resolution models​.
-   **[D-I-TASSER](https://zhanggroup.org/D-I-TASSER/)** (Job ID [DIT6377](./DIT6377/)):[^zhou2022itassermtd] An advanced iteration of I-TASSER using deep-learning-based spatial restraints to model proteins with greater accuracy, especially in challenging cases with weak homology, providing more reliable multi-domain structure predictions compared to I-TASSER​.
-   **[I-TASSER-MTD](https://zhanggroup.org/I-TASSER-MTD/)** (Job ID [ITM552669806](./ITM552669806/)): Designed specifically for multi-domain proteins, it combines domain parsing, single-domain folding, and inter-domain assembly with improved functionality and accuracy for large, multi-domain proteins compared to D-I-TASSER​
-   **[C-QUARK](https://zhanggroup.org/C-QUARK/)** (Job ID [QB4066](https://seq2fun.dcmb.med.umich.edu/C-QUARK/output/QB4066/)): An *ab initio* modeling tool that integrates coevolution and deep-learning-guided contact predictions to fold non-homologous proteins; it is particularly effective in cases lacking homologous templates, outperforming standard *ab initio* methods like QUARK​.
-   **[SWISS-MODEL](https://swissmodel.expasy.org/)** (Job ID [a7BMLv](https://swissmodel.expasy.org/interactive/a7BMLv/)): A homology modeling platform emphasizing user accessibility and high-quality models through evolutionary template matching; while not as suitable for low-homology cases as I-TASSER or AlphaFold3, it excels in providing intuitive results for well-conserved targets
-   [**AlphaFold3**](https://alphafoldserver.com/) (You must run your own job): A state-of-the-art model leveraging a diffusion-based architecture to predict highly accurate protein structures and biomolecular interactions across diverse targets, outperforming specialized tools in protein-ligand and protein-nucleic acid interactions​.

!!! note "Report"

    In your report, answer the following questions:

    1.  TODO:

### Experimental Structure Analysis

Identify the optimal experimental structure of *S. aureus* DHFR from the PDB.

TODO:

<!--
There are no wild types without some inhibitors.

# Paper: Increased hydrophobic interactions of iclaprim with Staphylococcus aureus dihydrofolate reductase are responsible for the increase in affinity and antibacterial activity

3FRA: S. aureus F98Y DHFR complexed with iclaprim
3FRB: S. aureus F98Y DHFR complexed with TMP
3FRD: S. aureus DHFR complexed with NADPH and folate
3FRE: S. aureus DHFR complexed with NADPH and TMP
3FRF: S. aureus DHFR complexed with NADPH and iclaprim

# Paper: Inhibitor design to target a unique feature in the folate pocket of Staphylococcus aureus dihydrofolate reductase.

6PRA: S. aureus dihydrofolate reductase with NADP(H) and empty folate pocket
6PR6: S. aureus dihydrofolate reductase co-crystallized with para-tolyl-dihydropthalazine inhibitor and NADP(H)
6PR7: S. aureus dihydrofolate reductase co-crystallized with benzyl-dihydropthalazine inhibitor and NADP(H)
6PR8: S. aureus dihydrofolate reductase co-crystallized with 3,5-dimethylphenyl-dihydropthalazine inhibitor and NADP(H)
6PR9: S. aureus dihydrofolate reductase co-crystallized with 1-ethylpropyl-dihydropthalazine inhibitor and NADP(H)
6PRB: S. aureus dihydrofolate reductase co-crystallized with cyclopropyl-dimethyoxydihydropthalazine inhibitor and NADP(H)
6PRD: S. aureus dihydrofolate reductase co-crystallized with para-methoxyphenyl-dimethyoxydihydropthalazine inhibitor and NADP(H)
-->

### Structural Analysis

Using [PyMOL](https://www.pymol.org/) or [ChimeraX](https://www.cgl.ucsf.edu/chimerax/), analyze the following for both predicted and experimental structures:

TODO:

<!-- REFERENCES -->

[^zhou2022itassermtd]: Zhou, X., Zheng, W., Li, Y., Pearce, R., Zhang, C., Bell, E. W., ... & Zhang, Y. (2022). I-TASSER-MTD: a deep-learning-based platform for multi-domain protein structure and function prediction. *Nature Protocols, 17*(10), 2326-2353. DOI: [10.1038/s41596-022-00728-0](https://doi.org/10.1038/s41596-022-00728-0)
