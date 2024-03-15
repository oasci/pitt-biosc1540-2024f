# Protein tertiary structure

The tertiary structure of a protein consists of the way a polypeptide is formed into a complex three-dimensional shape.
The tertiary structure will have a single polypeptide chain "backbone" with one or more protein secondary structures, such as alpha helices, beta sheets, or unstructured regions.
Amino acid side chains may interact and bond in several ways.
The interactions and bonds of side chains within a particular protein determine its tertiary structure.
Several tertiary structure subunits may fold into a quaternary structure.

## Driving forces

A protein folded into its native state or native conformation typically has a lower free energy than the unfolded conformation.
A protein will tend towards low-energy conformations, which will determine the protein's fold in the cellular environment.
Because many similar conformations will have similar energies, protein structures are dynamic, fluctuating between these similar structures.

Globular proteins have a core of hydrophobic amino acid residues and a surface region of water-exposed, charged, hydrophilic residues.
This arrangement may stabilize interactions within the tertiary structure.
For example, in secreted proteins, which are not bathed in cytoplasm, disulfide bonds between cysteine residues help to maintain the tertiary structure.
The structure of a protein, such as an enzyme, depends on the cellular environment it is in and may change upon binding of its natural ligands, for example, a cofactor.

## Experimental determination

Determining the structure of a protein is key to understanding its function and is a major task undertaken by structural biologists.
The knowledge of the tertiary structure of soluble globular proteins is more advanced than that of membrane proteins because the former are easier to study with available technology.
Several advanced lab techniques are used to determine ("solve") protein structures.

### X-ray crystallography

!!! quote "Figure 1"

    <figure markdown>
        ![A protein crystal](https://upload.wikimedia.org/wikipedia/commons/0/0e/Protein_crystal.jpg){ width=400 }
    </figure>

    A protein crystal is seen under a microscope.
    Crystals used in X-ray crystallography may be smaller than a millimeter across.

X-ray crystallography is by far the most common tool used to determine protein structure.
It provides high resolution of the structure but it does not give information about protein's conformational flexibility.
X-ray crystallography is the experimental science of empirically determining the atomic and molecular structure of a crystal, in which the crystalline structure causes a beam of X-rays to diffract into many specific directions.
By measuring the angles and intensities of these diffracted beams, a crystallographer can produce a three-dimensional picture of the density of electrons within the crystal.
From this electron density, the positions of the atoms in the crystal can be determined, as well as their chemical bonds.

!!! quote "Figure 2"

    <figure markdown>
        ![Diffraction pattern from a protein crystal](https://upload.wikimedia.org/wikipedia/commons/7/7d/X-ray_diffraction_pattern_3clpro.jpg){ width=500 }
    </figure>

    An X-ray diffraction pattern of a crystallized enzyme.
    The pattern of spots (reflections) and the relative strength of each spot (intensities) can be used to determine the structure of the enzyme.

Since many materials can form crystals—such as salts, metals, minerals, as well as various inorganic, organic, and biological molecules—X-ray crystallography has been fundamental in the development of many scientific fields.
In its first decades of use, this method determined the size of atoms, the lengths and types of chemical bonds, and the atomic-scale differences among various materials.
The method also revealed the structure and function of many biological molecules, including vitamins, drugs, proteins, and nucleic acids such as DNA.
X-ray crystallography is still the primary method for characterizing the atomic structure of new materials and in discerning materials that appear similar to other experiments.

!!! quote "Figure 3A"

    <div id="myoglobin-atomistic-view" class="mol-container"></div>
    <script>
        var uri = 'https://files.rcsb.org/view/3RGK.pdb';
        jQuery.ajax( uri, {
            success: function(data) {
                // https://3dmol.org/doc/GLViewer.html
                let viewer = $3Dmol.createViewer(
                    document.querySelector('#myoglobin-atomistic-view'),
                    { backgroundAlpha: '0.0' }
                );
                viewer.addModel(data, "pdb");
                viewer.setStyle({}, {stick: {}});
                viewer.setStyle({resn: "HEM"}, {stick: {}});
                viewer.setStyle({resi: "200"}, {sphere: {}});
                //viewer.zoomTo({chain: 'A'})
                viewer.setView([ -0.7665464162870579, -31.980985594511658, -1.0271908916093104, -0.8187833451410214, -0.4364964576815298, -0.33783642798767294, -0.526585026363653, -0.6465644595595998 ]);
                viewer.setClickable({}, true, function(atom,viewer,event,container) {
                    console.log(viewer.getView());
                });
                viewer.render();
            },
            error: function(hdr, status, err) {
                console.error( "Failed to load " + uri + ": " + err );
            },
        });
    </script>

    Atomistic representation of myoglobin with the heme group with one oxygen bound.
    PDB ID: [3RGK](https://www.rcsb.org/structure/3RGK)

Such proteins are long, linear molecules with thousands of atoms; yet the relative position of each atom has been determined with sub-atomic resolution by X-ray crystallography.
Since it is difficult to visualize all the atoms at once, the ribbon shows the rough path of the protein's backbone from its N-terminus to its C-terminus.

!!! quote "Figure 3B"

    <div id="myoglobin-view" class="mol-container"></div>
    <script>
        var uri = 'https://files.rcsb.org/view/3RGK.pdb';
        jQuery.ajax( uri, {
            success: function(data) {
                // https://3dmol.org/doc/GLViewer.html
                let viewer = $3Dmol.createViewer(
                    document.querySelector('#myoglobin-view'),
                    { backgroundAlpha: '0.0' }
                );
                viewer.addModel(data, "pdb");
                viewer.setStyle({}, {cartoon: {color: 'spectrum'}});
                viewer.setStyle({resn: "HEM"}, {stick: {}, cartoon: {color: 'spectrum'}});
                viewer.setStyle({resi: "200"}, {sphere: {}});
                //viewer.zoomTo({chain: 'A'})
                viewer.setView([ -0.7665464162870579, -31.980985594511658, -1.0271908916093104, -0.8187833451410214, -0.4364964576815298, -0.33783642798767294, -0.526585026363653, -0.6465644595595998 ]);
                viewer.setClickable({}, true, function(atom,viewer,event,container) {
                    console.log(viewer.getView());
                });
                viewer.render();
            },
            error: function(hdr, status, err) {
                console.error( "Failed to load " + uri + ": " + err );
            },
        });
    </script>

    Ribbon structure of myoglobin with the heme group with one oxygen bound.
    PDB ID: [3RGK](https://www.rcsb.org/structure/3RGK)

Crystal structures of proteins began to be solved in the late 1950s, beginning with the structure of sperm whale myoglobin by Sir John Cowdery Kendrew, for which he shared the Nobel Prize in Chemistry with Max Perutz in 1962.
Since that success, over 130,000 X-ray crystal structures of proteins, nucleic acids, and other biological molecules have been determined.

!!! quote "Figure 4"

    <figure markdown>
        ![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/X_ray_diffraction.png/1024px-X_ray_diffraction.png){ width=400 }
    </figure>

    Workflow for solving the structure of a molecule by X-ray crystallography.

### NMR

The nearest competing method to X-ray crystallography is nuclear magnetic resonance (NMR) spectroscopy, which has resolved less than one-tenth as many macromolecules.
Protein Nuclear Magnetic Resonance (NMR) imaging gives comparatively lower resolution of protein structure and is limited to smaller proteins.
However, it can provide information about conformational changes of a protein in solution.

### Cryogenic electron microscopy

Cryogenic electron microscopy (cryo-EM) can give information about both a protein's tertiary and quaternary structure.
It is particularly well-suited to large proteins and symmetrical complexes of protein subunits.

## Molecular models of protein structures

Once a protein structure has been solved in the lab, the data can be used to create drawings, computer animations, 3D sculptures, and other molecular models representing the data.
A molecular model is a physical, mathematical, or other type of model of an atomistic system that represents molecules and their processes.
They play an important role in understanding chemistry and generating and testing hypotheses.
The creation of mathematical models of molecular properties and behavior is referred to as molecular modeling, and their graphical depiction is referred to as molecular graphics.

Molecular models may be created for several reasons:

-   as teaching aids for students or those unfamiliar with atomistic structures;
-   as objects to generate or test theories (e.g., the structure of DNA);
-   as analog computers (e.g., for measuring distances and angles in flexible systems);
-   or as aesthetically pleasing objects on the boundary of art and science.

The construction of physical models is often a creative act, and many examples have been carefully created in the workshops of science departments.
There is a very wide range of approaches to physical modeling, including ball-and-stick models available for purchase commercially, to molecular models created using 3D printers.
Molecular graphics have made the visualization of molecular models on computer hardware easier, more accessible, and inexpensive, although physical models are widely used to enhance the tactile and visual message being portrayed.

Computers play a key role in building models because they can be used to predict bond lengths and angles, molecular polarity and charge distribution, and even quantum mechanical properties.
For most practical purposes, such as drug design or protein folding, the calculations of a model require supercomputing or cannot be done on classical computers at all in a reasonable amount of time.

### Ribbon diagrams

Ribbon diagrams are schematic representations of protein 3D structure and are one of the most common methods of protein depiction used today.
The ribbon depicts the general course and organization of the protein backbone in 3D and serves as a visual framework for hanging details of the entire atomic structure, such as the balls for the oxygen atoms attached to myoglobin's active site in the adjacent figure.
Ribbon diagrams are generated by interpolating a smooth curve through the polypeptide backbone.
α-helices are shown as coiled ribbons or thick tubes, β-sheets as arrows, and non-repetitive coils or loops as lines or thin tubes.
The direction of the polypeptide chain is shown locally by the arrows and may be indicated overall by a color ramp along the length of the ribbon.

Ribbon diagrams are simple yet powerful, expressing the visual basics of a molecular structure (twist, fold, and unfold).
This method has successfully portrayed the overall organization of protein structures, reflecting their three-dimensional nature and allowing a better understanding of these complex objects both by expert structural biologists and by other scientists, students, and the general public.

The first ribbon diagrams, hand-drawn by Jane Richardson in 1980 (influenced by earlier individual illustrations), were the first schematics of 3D protein structure to be produced systematically.
In 1982, Arthur M. Lesk and co-workers first enabled the automatic generation of ribbon diagrams through a computational implementation that uses Protein Data Bank  *.PDB files as input.
Both hand-drawn and most computer ribbons are smoothed over to produce a more visually pleasing and understandable representation.
Since their inception, and continuing in the present, ribbon diagrams have been the single most common representation of protein structure and a common choice of cover image for a journal or textbook.

#### Current computer programs for ribbon diagrams

Numerous programs exist for modeling proteins and rendering ribbon diagrams.
The most common are [ChimeraX](https://www.cgl.ucsf.edu/chimerax/), [PyMOL](https://pymol.org), and [VMD](https://www.ks.uiuc.edu/Research/vmd/).

!!! quote "Figure 5"

    <div id="tubby-view" class="mol-container"></div>
    <script>
    var uri = 'https://files.rcsb.org/view/1C8Z.pdb';
    jQuery.ajax( uri, {
        success: function(data) {
            // https://3dmol.org/doc/GLViewer.html
            let viewer = $3Dmol.createViewer(
                document.querySelector('#tubby-view'),
                { backgroundAlpha: '0.0' }
            );
            viewer.addModel(data, "pdb");
            viewer.setStyle({}, {cartoon: {color: 'spectrum'}});
            viewer.zoomTo({chain: 'A'})
            viewer.setClickable({}, true, function(atom,viewer,event,container) {
                console.log(viewer.getView());
            });
            viewer.render();
        },
        error: function(hdr, status, err) {
            console.error( "Failed to load " + uri + ": " + err );
        },
    });
    </script>

    Ribbon of the structure of the tubby protein (PDB: [1C8Z](https://www.rcsb.org/structure/1C8Z​)).

### Space-filling models

Another common way to represent protein tertiary structures is a space-filling model.
In chemistry, a space-filling model is a type of three-dimensional (3D) molecular model where the atoms are represented by spheres with radii proportional to atomic radii.
Atoms of different chemical elements are usually represented by spheres of different colors.

An example of a space-filling model of a very complex macromolecule is shown below.
This is a protein, the cell membrane-spanning $\beta$2 adrenoreceptor, a G protein-coupled receptor, viewed as if looking down onto the extracellular surface.
The electrostatic potential surface was applied to a model with atom positions determined by crystallography (PDB code [2RH1](https://www.rcsb.org/structure/2rh1)).
It is shaded blue for electropositive areas to red for electronegative areas.
Somewhat apparent, in stick representation in yellow, red, and blue, in a groove at the top of the receptor, is a small molecule ligand bound to it.
All of such binding interactions and the function of the receptor in signal transduction are mediated by electrostatic effects, and in modern structure work, they are often studied using similar space-filling models.

!!! quote "Figure 6"

    <figure markdown>
        ![](https://upload.wikimedia.org/wikipedia/commons/e/e8/Beta-2-adrenergic-receptor-electrostatic-top.png){ width=400 }
    </figure>

    PDB code [2RH1](https://www.rcsb.org/structure/2rh1).

## Protein structure databases

After being solved the raw data for a protein's structure is deposited in databases to be available to the scientific community.
The [Protein Data Bank](https://www.rcsb.org/) (PDB) is the primary database for the three-dimensional structural data of large biological molecules, such as proteins and nucleic acids.
The data are typically obtained by X-ray crystallography, NMR spectroscopy, or, increasingly, cryo-electron microscopy.
Structures are submitted by scientists from around the world, and are freely accessible on the Internet via the websites of its member organizations.

The PDB is a key resource in areas of structural biology, such as structural genomics.
Most major scientific journals and some funding agencies now require scientists to submit their structure data to the PDB.
PDB data is the basis for the [CASP competition](https://predictioncenter.org/) and source data for the protein structure prediction software and database AlphaFold.

## Acknowledgements

This chapter was adapted from the following Wikipedia entries:

-   https://en.wikipedia.org/wiki/Protein_tertiary_structure
-   https://en.wikipedia.org/wiki/X-ray_crystallography
-   https://en.wikipedia.org/wiki/Molecular_model
-   https://en.wikipedia.org/wiki/Ribbon_diagram
-   https://en.wikipedia.org/wiki/PyMOL
-   https://en.wikipedia.org/wiki/Space-filling_model
-   https://en.wikipedia.org/wiki/Protein_Data_Bank
