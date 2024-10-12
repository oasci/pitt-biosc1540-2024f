<h1 align="center">
A05
</h1>

<p style="text-align: center;">
    <object hspace="50">
        <strong>Due</strong></a>: Oct 25, 2024 by 11:59 p.m.
    </object>
    <object hspace="50">
        <strong>Points</strong></a>: 60
    </object>
</p>

Be concise and focus on critical concepts.
For each question or subpart, your response should be between 50 and 100 words.

## Q01

**Points**: 8

Explain how X-ray crystallography is used to determine the electron density of a molecule.
Describe how this information leads to fitting and refining an atomic model.
Include the key steps in your explanation, from data collection to model refinement.

## Q02

**Points**: 8

Explain how X-rays scatter off electrons in a crystal.
Discuss why this phenomenon is essential for determining protein structures using X-ray crystallography.
In your answer, briefly describe the relationship between the crystal lattice and the resulting diffraction pattern.

## Q03

**Points**: 8

Explain constructive and destructive interference in the context of X-ray diffraction patterns.
Describe how these phenomena contribute to the formation of diffraction spots and the absence of certain reflections.
Briefly discuss how understanding these concepts helps in interpreting X-ray diffraction data.

## Q04

**Points**: 10

Compare and contrast Cryo-Electron Microscopy (Cryo-EM) and X-ray Crystallography as methods for determining the structures of biological macromolecules.

## Q05

**a**

**Points**: 4

Use [UniProt](https://www.uniprot.org/) to search for the Enoyl-[acyl-carrier-protein] reductase [NADH] (`inhA`) from *Mycobacterium smegmatis* with the highest annotation score.
Summarize the function of this protein and provide the UniProt ID.

<!-- UniProt ID: P9WGR1 -->

**b**

**Points**: 2

Provide the amino acid sequence of the protein you found in part (a).

**c**

**Points**: 4

Visit the Protein Data Bank (PDB) and find the best experimental structure for native `inhA` and provide the four-character PDB ID.
Explain why you chose this structure (e.g., resolution, completeness, mutations).
Download the structure in `PDBXmmCIF Format`.

??? tip

    To select the best native structure of *Enoyl-[acyl-carrier-protein] reductase* (`inhA`) from the Protein Data Bank (PDB), follow these steps:

    1.  Once the search results appear, you’ll see a list of structures associated with the protein.
        Each structure will have a unique PDB ID and may have different experimental conditions, resolutions, and details.
    2.  To select the most suitable structure, consider the following:
        -   Structures with a lower resolution (in Ångstroms) are generally more accurate.
            Aim to select a structure with a resolution below 2.0 Å, as these offer higher detail. Structures with a resolution above 3.0 Å might be less precise.
        -   Check the structure for any missing regions, such as loops or domains.
            A complete structure provides a more accurate representation of the protein, while structures missing important regions may limit its reliability.
        -   Prefer structures solved using X-ray crystallography or Cryo-Electron Microscopy (Cryo-EM).
            X-ray crystallography typically yields high-resolution structures, but Cryo-EM can also provide important structural insights, especially for flexible regions.
        -   Review the structure’s description and any bound ligands.
            Choose a structure that reflects the biologically relevant state of the protein.
            For example, if studying the active form of the protein, select a structure where a relevant ligand or cofactor is bound.
    3.  If available, examine the structure’s validation report, which provides insights into the accuracy and reliability of the structural data.
        Look for structures with good validation scores for quality assurance.

## Q06

**Points**: 6

Describe the concept of homology modeling in protein structure prediction.
Explain the main principles behind this method and why it's useful.
Mention at least one limitation of this approach.

## Q07

**a**

**Points**: 4

-   Visit the [SWISS-MODEL](https://swissmodel.expasy.org/interactive) interactive workspace.
-   Use the following amino acid sequence for prediction:

    ```text
    MTGLLDHKRILVSGIVTDSSIAYHVQAVAQEQGGELVLTGFDKLRVIQRVTDRL
    PSKAPLLELDAENEQHLASLAGKITEAIGAGNKIDGVTHSIGFMPRTGMGVNPF
    FDTPYADVTRGPHISAYSYTSMSKALLPIMNPGGTIVGMNFDPSRAMPVYNWMT
    AAKSAAESINRFVARETGKYGIRNNLVAAGPIRTLVMSAIVGGVLGAEAGAQIC
    LVEENWDQRTPMGWNMKDITPVCKTVCGLLSDWLPATTGDIIYHDGGAHTQLL
    ```
-   After submitting the sequence, identify and record the five PDB IDs with the highest identity scores from the template search results.
-   Build homology models using these templates.
-   Explain what Global Model Quality Estimation (GMQE) is in the context of protein modeling.
-   Note which PDB structure provided the highest GMQE score.
-   Download the `modelCIF` file by clicking on the "Download Files" button associated with your best model.

**b**

**Points**: 2

-   Navigate to [AlphaFold 3](https://alphafoldserver.com/) (AF3)
-   Predict the structure of the inhA protein using the same amino acid sequence provided above.
-   Once the prediction is complete, download and extract the results.
-   Locate the file named `_model_0.cif`, which contains the predicted structure from AF3.

**c**

**Points**: 4

-   Load the following structures into [Mol*](https://molstar.org/viewer):
    -   The experimental structure of the protein from Q05.
    -   The predicted structure from SWISS-MODEL (`modelCIF` file).
    -   The predicted structure from AlphaFold 3 (`_model_0.cif` file).
-   Align the structures within Mol* to compare their conformations.
-   Take a screenshot of the aligned structures and include it in your submission.
-   Discuss at least one key difference observed between the structures. This could relate to structural features such as folding patterns, active sites, or any notable deviations.

## Programming+

These problems are not required and will not impact your BIOSC 1540 grade.
The instructor will assess these separately to validate correctness without an assigned grade.
Thus, you may work on these problems individually or in a team-based setting and "due" by the end of the semester.
Happy coding!

**Acceptable languages**: Python v3.10+, Mojo v24.4+, Zig v0.13+, Rust v1.80+

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

### P01: PDB File Parser

In the field of structural biology, the Protein Data Bank (PDB) file format is widely used to store three-dimensional structural data of molecules.
Your task is to create a program that can read and extract basic information from a PDB file. This will give you hands-on experience with the kind of data processing often required in structural biology research.

Write a program that takes a PDB file as input and extracts the following information:

1. The total number of atoms in the structure
2. The number of amino acid residues

To accomplish this, you'll need to understand the structure of a PDB file.
Each line in a PDB file represents a record, and different record types contain different information.
For example, ATOM records contain information about individual atoms, while HELIX and SHEET records describe secondary structures.

You may find it helpful to use the Biopython library, specifically the Bio.PDB module, which provides tools for working with PDB files. If you choose to use Biopython, look into the PDBParser class for reading PDB files and the Structure class for accessing the parsed data.

Your program should output a summary of the extracted information in a clear, readable format.

### P02: RMSD Calculator

Root Mean Square Deviation (RMSD) is a commonly used measure to compare protein structures.
It quantifies the average distance between atoms of superimposed proteins.
This metric is crucial in various applications, such as assessing the quality of predicted protein structures or analyzing conformational changes.

Your task is to write a program that calculates the RMSD between two protein structures.
The program should:

1. Take two PDB files as input. These could represent the same protein in different states (e.g., experimental vs. predicted structures).
2. Align the structures (you may assume they are already roughly aligned).
3. Calculate the RMSD between corresponding atoms.

To calculate RMSD, you'll need to:

1. Extract the 3D coordinates of corresponding atoms from both structures.
2. Calculate the squared differences between these coordinates.
3. Take the average of these squared differences.
4. Take the square root of this average.

You may want to focus on comparing only the backbone atoms (N, Cα, C) or all heavy atoms.
Be sure to specify in your output which atoms you're using for the comparison.

Consider using libraries like NumPy to handle the 3D coordinate data and perform calculations efficiently.

### P03: Secondary Structure Predictor

Predicting protein secondary structure from amino acid sequence is a fundamental problem in bioinformatics. While modern methods use sophisticated machine learning techniques, simpler algorithms can still provide insights into the relationship between sequence and structure.

Your task is to implement a basic secondary structure prediction algorithm, such as the Chou-Fasman method.
This algorithm assigns propensities for each amino acid to be in an alpha helix, beta sheet, or random coil, then uses these propensities to predict the most likely secondary structure for each residue.

Your program should:

1. Take a protein sequence as input (a string of one-letter amino acid codes).
2. Implement the Chou-Fasman algorithm or another simple prediction method.
3. Output the predicted secondary structure for each residue (e.g., H for helix, E for sheet, C for coil).

To implement the Chou-Fasman method:

1. Use a table of propensity values for each amino acid.
2. Scan the sequence to find regions with high propensities for helices or sheets.
3. Apply rules for extending and terminating these structures.
4. Assign remaining regions as coils.

Remember, this is a simplified method and won't be as accurate as modern predictors, but it will give you insight into the principles of sequence-based structure prediction.

### P04: Solvent-Accessible Surface Area Calculator

Solvent-Accessible Surface Area (SASA) is an important property in protein structure analysis. It represents the surface area of a protein that is accessible to a solvent molecule (typically water) and can provide insights into protein-protein interactions, ligand binding sites, and more.

Your task is to write a program that calculates the SASA for each residue in a protein structure. The program should:

1. Take a PDB file as input.
2. Calculate the SASA for each residue.
3. Output the SASA values in a clear, readable format.

To calculate SASA, you can:

1. Use the Biopython library, which provides SASA calculation functionality.
2. Use an external tool like FreeSASA, which you can call from your Python script.
3. Implement a simple SASA algorithm yourself (this is more challenging and less accurate, but educational).

If using Biopython or FreeSASA:

1. Read the documentation to understand how to use the SASA calculation functions.
2. Ensure you understand the units of the output (typically Å²) and any parameters you need to set (like probe radius).

If implementing your own algorithm:

1. Represent the protein as a set of spheres (atoms).
2. Use a probe sphere to "roll" over the surface of these spheres.
3. Calculate the area accessible to the probe.

Your output should list each residue along with its calculated SASA.
Consider also providing summary statistics, like average SASA per residue type or total protein SASA.
