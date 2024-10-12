<h1 align="center">
A05
</h1>

<p style="text-align: center;">
    <object hspace="50">
        <strong>Due</strong></a>: Oct 20, 2024 by 11:59 p.m.
    </object>
    <object hspace="50">
        <strong>Points</strong></a>: 60
    </object>
</p>

Be concise and focus on critical concepts.
For each question, your response should be around 45 to 75 words.

## Q01

Explain how X-ray crystallography is used to determine the electron density of a molecule and how this information leads to fitting and refining an atomic model.

## Q02

Explain how X-rays scatter off electrons in a crystal and why this phenomenon is essential for determining protein structures using X-ray crystallography.

## Q03

Explain constructive and destructive interference in the context of X-ray diffraction patterns.

## Q04

Compare and contrast Cryo-Electron Microscopy (Cryo-EM) and X-ray Crystallography as methods for determining the structures of biological macromolecules.

## Q05

**a**

Use [UniProt](https://www.uniprot.org/) to search for the Enoyl-[acyl-carrier-protein] reductase [NADH] (`inhA`) from *Mycobacterium smegmatis* with the highest annotation score.
Summarize the function of this protein.

<!-- UniProt ID: P9WGR1 -->

**b**

What is the amino acid sequence of the protein?

**c**

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

Describe the concept of homology modeling in protein structure prediction.
In your answer, briefly explain the main principles behind homology modeling.

## Q07

**a**

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

-   Navigate to [AlphaFold 3](https://alphafoldserver.com/) (AF3)
-   Predict the structure of the inhA protein using the same amino acid sequence provided above.
-   Once the prediction is complete, download and extract the results.
-   Locate the file named `_model_0.cif`, which contains the predicted structure from AF3.

**c**

-   Open the [Mol*](https://molstar.org/viewer)
-   Load the following structures into Mol*:
    -   The experimental structure of the protein from Q05.
    -   The predicted structure from SWISS-MODEL (`modelCIF` file).
    -   The predicted structure from AlphaFold 3 (`_model_0.cif` file).
-   Align the structures within Mol* to compare their conformations.
-   Take a screenshot of the aligned structures.
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

Given your focus on experimental protein structure determination and protein structure prediction (homology modeling and AlphaFold 2), here are some programming problems tailored to these topics:

### P01

**Objective**: Write a program that parses a PDB file and extracts basic information such as the number of atoms, the number of residues, and the types of secondary structures (helix, sheet, etc.).
- **Input**: A PDB file.
- **Output**: The number of atoms, residues, and secondary structures (helix, sheet, etc.).
- **Hints**: Use Python libraries such as `Bio.PDB` from Biopython to extract the required information.

This problem introduces students to working with PDB files, a key format in experimental protein structure determination.

### P02

**Objective**: Write a program that computes the Root Mean Square Deviation (RMSD) between two protein structures.
- **Input**: Two PDB files of the same protein (e.g., one experimental and one predicted).
- **Output**: The RMSD value.
- **Hints**: Use the atomic coordinates from the PDB files and calculate the RMSD between the corresponding atoms.

This problem will help students understand how protein structures are compared and analyzed.

### P03

**Objective**: Write a program that predicts the secondary structure (helix, sheet, or coil) of a given protein sequence using a simple scoring method (e.g., Chou-Fasman algorithm).
- **Input**: A protein sequence (amino acid string).
- **Output**: Predicted secondary structure for each residue.
- **Hints**: You can implement the Chou-Fasman algorithm or use another simple method to predict the secondary structure.

This task introduces students to basic principles behind predicting structural features of proteins based on their sequence.

### P04

**Objective**: Write a script that automates the process of submitting a protein sequence to SWISS-MODEL, retrieving the homology models, and reporting back the best models based on GMQE scores.
- **Input**: A protein sequence.
- **Output**: A summary of the top five models with their GMQE scores.
- **Hints**: Use Python's `requests` library or similar tools to automate the process.

This problem helps students connect the theoretical aspects of homology modeling to practical applications.

### P05

**Objective**: Write a program that interacts with the AlphaFold server to predict the structure of a protein from its sequence and download the resulting model.
- **Input**: A protein sequence.
- **Output**: The predicted protein structure in PDB or CIF format.
- **Hints**: Research the AlphaFold API and automate the process of submitting sequences and retrieving results.

This problem reinforces protein structure prediction using modern machine learning tools.

### P06

**Objective**: Write a program that calculates the solvent-accessible surface area (SASA) for a protein structure provided in PDB format.
- **Input**: A PDB file.
- **Output**: SASA for each residue.
- **Hints**: Use libraries such as `Biopython` or external tools like `FreeSASA` to compute SASA.

This introduces students to the concept of protein structure properties that can be inferred from 3D coordinates.

These problems are aligned with your course’s focus and allow students to apply programming skills directly to tasks related to experimental structure determination and protein structure prediction methods.

Given your focus on experimental protein structure determination and protein structure prediction (homology modeling and AlphaFold 2), here are some programming problems tailored to these topics:

### P01

**Objective**: Write a program that parses a PDB file and extracts basic information such as the number of atoms, the number of residues, and the types of secondary structures (helix, sheet, etc.).
- **Input**: A PDB file.
- **Output**: The number of atoms, residues, and secondary structures (helix, sheet, etc.).
- **Hints**: Use Python libraries such as `Bio.PDB` from Biopython to extract the required information.

### P02

**Objective**: Write a program that computes the Root Mean Square Deviation (RMSD) between two protein structures.
- **Input**: Two PDB files of the same protein (e.g., one experimental and one predicted).
- **Output**: The RMSD value.
- **Hints**: Use the atomic coordinates from the PDB files and calculate the RMSD between the corresponding atoms.

### P03

**Objective**: Write a program that predicts the secondary structure (helix, sheet, or coil) of a given protein sequence using a simple scoring method (e.g., Chou-Fasman algorithm).
- **Input**: A protein sequence (amino acid string).
- **Output**: Predicted secondary structure for each residue.
- **Hints**: You can implement the Chou-Fasman algorithm or use another simple method to predict the secondary structure.

### P04

**Objective**: Write a script that automates the process of submitting a protein sequence to SWISS-MODEL, retrieving the homology models, and reporting back the best models based on GMQE scores.
- **Input**: A protein sequence.
- **Output**: A summary of the top five models with their GMQE scores.
- **Hints**: Use Python's `requests` library or similar tools to automate the process.

This problem helps students connect the theoretical aspects of homology modeling to practical applications.

### P05

**Objective**: Write a program that interacts with the AlphaFold server to predict the structure of a protein from its sequence and download the resulting model.
- **Input**: A protein sequence.
- **Output**: The predicted protein structure in PDB or CIF format.
- **Hints**: Research the AlphaFold API and automate the process of submitting sequences and retrieving results.

### P06

**Objective**: Write a program that calculates the solvent-accessible surface area (SASA) for a protein structure provided in PDB format.
- **Input**: A PDB file.
- **Output**: SASA for each residue.
- **Hints**: Use libraries such as `Biopython` or external tools like `FreeSASA` to compute SASA.
