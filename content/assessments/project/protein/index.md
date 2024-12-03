<h1 align="center">
<b>Part 2:</b><br>
Protein structure prediction
</h1>

In this phase, you will predict and analyze the structure of dihydrofolate reductase (DHFR) from *S. aureus* that you identified in [Part 1](../genome/).
DHFR is an essential enzyme involved in folate metabolism and an important antibiotic target.

By completing this project, you will:

-   Gain practical experience with state-of-the-art protein structure prediction tools.
-   Learn to critically evaluate and compare protein structure predictions.
-   Understand how to analyze protein structures and their functional features.
-   Develop skills in structural visualization and analysis.

## Instructions

Use [PyMOL](https://www.pymol.org/) for your structural analysis.
You often will need to use the "licorice" representation of the protein to see that atomistic differences.

To support your computational biology project, your instructor has provided a PSE file for each question.
A PSE file is a PyMOL session file that contains a pre-configured molecular structure and relevant visualizations to help you address the specific questions.
These files are designed to save you time and effort by providing the necessary setup, including loaded molecules, annotations, and possibly preset views that align with the problem requirements.

In each screenshot, ensure you provide a visual indication and/or label to specify the origin (e.g., I-TASSER or 6PRD) of the structure.
Below is an example of an appropriate image to use in your report.

!!! quote "Example image"
    Conformations of His23, Glu143, and Lys144 of DHFR are shown below for 3FRD and 6PR6 with carbon atoms shown in pink and white, respectively.
    Structures were aligned by their alpha carbons.
    <figure markdown>
    ![](./example-report-image.png)
    </figure>

### Structure predictions

Using the UniProt DHFR sequence from your [genome assembly project](../genome/), we will perform several predictions.
Instead of flooding these free servers with the same jobs, we will all use the same outputs.

-   **[I-TASSER](https://zhanggroup.org/I-TASSER/)** (Job ID [S799334](./S799334/)): A threading-based method for predicting protein structures and functions by assembling models from template fragments and refining them iteratively; it is robust for cases with moderate to strong homologous templates and provides functional annotations, often generating medium-resolution models​.
-   **[D-I-TASSER](https://zhanggroup.org/D-I-TASSER/)** (Job ID [DIT6377](./DIT6377/)): An advanced iteration of I-TASSER using deep-learning-based spatial restraints to model proteins with greater accuracy, especially in challenging cases with weak homology, providing more reliable multi-domain structure predictions compared to I-TASSER​.
-   **[I-TASSER-MTD](https://zhanggroup.org/I-TASSER-MTD/)** (Job ID [ITM552669806](./ITM552669806/)): Designed specifically for multi-domain proteins, it combines domain parsing, single-domain folding, and inter-domain assembly with improved functionality and accuracy for large, multi-domain proteins compared to D-I-TASSER​
<!-- -   **[C-QUARK](https://zhanggroup.org/C-QUARK/)** (Job ID [QB4066](https://seq2fun.dcmb.med.umich.edu/C-QUARK/output/QB4066/)): An *ab initio* modeling tool that integrates coevolution and deep-learning-guided contact predictions to fold non-homologous proteins; it is particularly effective in cases lacking homologous templates, outperforming standard *ab initio* methods like QUARK​. -->
-   **[SWISS-MODEL](https://swissmodel.expasy.org/)** (Job ID [a7BMLv](./a7BMLv/BIOSC_1540__Project/models.html)): A homology modeling platform emphasizing user accessibility and high-quality models through evolutionary template matching; while not as suitable for low-homology cases as I-TASSER or AlphaFold3, it excels in providing intuitive results for well-conserved targets
-   [**AlphaFold3**](https://alphafoldserver.com/) (You must run your own job): A state-of-the-art model leveraging a diffusion-based architecture to predict highly accurate protein structures and biomolecular interactions across diverse targets, outperforming specialized tools in protein-ligand and protein-nucleic acid interactions​.

!!! note "Submission"

    In your submission, answer the following questions:

    1.  Download the PDB files for SWISS-MODELS 01 (6E4E), 05 (3FYW), 03 (6PRP), and 06 (6PR8).
        Identify if there are any apparent protein conformational differences near the NADP(H) and folate binding pockets.
        Provide screenshots to support your claims.
        [(PyMol session file)](./pse/1-swiss.pse.gz)
    2.  Download the PDB file for SWISS-MODEL 02 (2W3M) and compare it against model 01 (6E4E).
        What is the alpha-carbon RMSD after alignment?
        Out of these two structures, which would you use for docking?
        Justify your choice.
        Provide screenshots to support your claims.
        [(PyMol session file)](./pse/2-swiss.pse.gz)
    3.  Download the [I-TASSER](./S799334/), [D-I-TASSER](./DIT6377/), [I-TASSER-MTD](./ITM552669806/), and your AlphaFold3 PDB structures.
        Compare these structure to each other and to SWISS-MODEL 01.
        Which prediction has the highest similarity (i.e., low RMSD) to the SWISS-MODEL?
        Which method would you generally find more reliable?
        Provide screenshots to support your claims.
        [(PyMol session file)](./pse/3-tasser.pse.gz)

### Experimental structures

The following experimental structures were selected for our analysis.
All are wild-type *S. aureus* DHFR with co-crystallized NADP(H).

| PDB ID | Additional ligand |
| ------ | -------------- |
| [3FRD](https://www.rcsb.org/structure/3FRD) | [Folate](https://pubchem.ncbi.nlm.nih.gov/compound/135398658) |
| [6PRA](https://www.rcsb.org/structure/6PRA) | None |
| [6PRB](https://www.rcsb.org/structure/6PRB) | [OWM](https://pubchem.ncbi.nlm.nih.gov/compound/146170546) |
| [6PRD](https://www.rcsb.org/structure/6PRD) | [OWG](https://pubchem.ncbi.nlm.nih.gov/compound/146170547) |
| [6PR6](https://www.rcsb.org/structure/6PR6) | [OWS](https://pubchem.ncbi.nlm.nih.gov/compound/146170541) |
| [6PR7](https://www.rcsb.org/structure/6PR7) | [OWP](https://pubchem.ncbi.nlm.nih.gov/compound/146170542) |
| [6PR8](https://www.rcsb.org/structure/6PR8) | [OWJ](https://pubchem.ncbi.nlm.nih.gov/compound/146672960) |
| [6PR9](https://www.rcsb.org/structure/6PR9) | [OWV](https://pubchem.ncbi.nlm.nih.gov/compound/146672961) |

Remember that you need to add hydrogens to your structures!

!!! note "Submission"

    In your submission, answer the following questions:

    1.  Download [3FRD](https://www.rcsb.org/structure/3FRD) and [6PRA](https://www.rcsb.org/structure/6PRA) PDB files.
        Suppose you will be docking in the folate pocket while keeping NADP(H) and removing all water molecules.
        Are there any structural differences in the protein that could impact your docking results?
        If yes, specify which residues, explain how this would impact docking, and provide screenshots to support your claims.
        If no, provide evidence in the form of screenshots and a possible explanation.
    2.  Identify noncovalent interactions in [3FRD](https://www.rcsb.org/structure/3FRD) that stabilize this folate pose.
        Use screenshots to support your claims.
    3.  Download all PDB structures in the above table that start with `6PR`.
        Each of these `6PR` structures, excluding [6PRA](https://www.rcsb.org/structure/6PRA), contain co-crystallized ligands that are potential *S. aureus* DHFR inhibitors from [this publication](https://doi.org/10.1016/j.ejmech.2020.112412).
        Identify protein-ligand noncovalent interactions for each inhibitor and note similarities and differences between folate noncovalent interactions.
    4.  In the same `6PR` structures, identify amino acids that are in different conformations depending on the ligand.
        Also, which protein would be the least reliable for subsequent protein-ligand docking?
        Provide a rationale.
