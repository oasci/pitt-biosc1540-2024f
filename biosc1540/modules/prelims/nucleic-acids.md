# Nucleic Acids Review

Nucleic acids are the most important macromolecules for the continuity of life.
They carry the genetic blueprint of a cell and carry instructions for the functioning of the cell.

## DNA and RNA

The two main types of nucleic acids are deoxyribonucleic acid (DNA) and ribonucleic acid (RNA).
DNA is the genetic material found in all living organisms, ranging from single-celled bacteria to multicellular mammals.
It is found in the nucleus of eukaryotes and the organelles, chloroplasts, and mitochondria.
In prokaryotes, the DNA is not enclosed in a membranous envelope.

The entire genetic content of a cell is known as its genome, and the study of genomes is genomics.
In eukaryotic cells, DNA forms a complex with histone proteins to form chromatin, the substance of eukaryotic chromosomes.
A chromosome may contain tens of thousands of genes.
Many genes contain the information to make protein products; other genes code for RNA products.
DNA controls all of the cellular activities by turning the genes "on" or "off."

The other type of nucleic acid, RNA, is mostly involved in protein synthesis.
DNA molecules never leave the nucleus but instead, use an intermediary to communicate with the rest of the cell.
This intermediary is the messenger RNA (mRNA).
Other types of RNA&mdash;like rRNA, tRNA, and microRNA&mdash;are involved in protein synthesis and its regulation.

DNA and RNA are made up of monomers known as nucleotides.
The nucleotides combine to form a polymer known as polynucleotide, DNA, or RNA.
Each nucleotide is made up of three components: a nitrogenous base, a pentose (five-carbon) sugar, and a phosphate group (Figure 1).
Each nitrogenous base in a nucleotide is attached to a sugar molecule, which is attached to one or more phosphate groups.

!!! quote "**Figure 1**"

    <figure markdown>
    ![Nucleotide structure](https://bio.libretexts.org/@api/deki/files/965/Figure_03_05_01.jpg){ alight=left width=600 }
    </figure>

    A nucleotide is made up of three components: a nitrogenous base, a pentose sugar, and one or more phosphate groups.
    Carbon residues in the pentose are numbered 1′ through 5′ (the prime distinguishes these residues from those in the base, which are numbered without using a prime notation).
    The base is attached to the 1′ position of the ribose, and the phosphate is attached to the 5′ position.
    When a polynucleotide is formed, the 5′ phosphate of the incoming nucleotide attaches to the 3′ hydroxyl group at the end of the growing chain.
    Two types of pentose are found in nucleotides, deoxyribose (found in DNA) and ribose (found in RNA).
    Deoxyribose is similar in structure to ribose, but it has an H instead of an OH at the 2′ position.
    Bases can be divided into two categories: purines and pyrimidines.
    Purines have a double-ring structure, and pyrimidines have a single ring.
    Source: LibreText: /bio.libretexts.org/@api/deki/files/965/Figure_03_05_01.jpg?revision=1

The nitrogenous bases, important components of nucleotides, are organic molecules and are so named because they contain carbon and nitrogen.
They are bases because they contain an amino group that has the potential of binding an extra hydrogen, and thus, decreases the hydrogen ion concentration in its environment, making it more basic.
Each nucleotide in DNA contains one of four possible nitrogenous bases: adenine (A), guanine (G) cytosine (C), and thymine (T).

Adenine and guanine are classified as purines.
The primary structure of a purine is two carbon-nitrogen rings.
Cytosine, thymine, and uracil are classified as pyrimidines which have a single carbon-nitrogen ring as their primary structure (Figure 1).
Each of these basic carbon-nitrogen rings has different functional groups attached to it.
In molecular biology shorthand, the nitrogenous bases are simply known by their symbols `A`, `T`, `G`, `C`, and `U`.
DNA contains `A`, `T`, `G`, and `C` whereas RNA contains `A`, `U`, `G`, and `C`.

The pentose sugar in DNA is deoxyribose, and in RNA, the sugar is ribose (Figure 1).
The difference between the sugars is the presence of the hydroxyl group on the second carbon of the ribose and hydrogen on the second carbon of the deoxyribose.
The carbon atoms of the sugar molecule are numbered as 1′, 2′, 3′, 4′, and 5′ (1′ is read as "one prime").
The phosphate residue is attached to the hydroxyl group of the 5′ carbon of one sugar and the hydroxyl group of the 3′ carbon of the sugar of the next nucleotide, which forms a 5′&ndash;3′ phosphodiester linkage.
The phosphodiester linkage is not formed by a simple dehydration reaction like the other linkages connecting monomers in macromolecules: its formation involves the removal of two phosphate groups.
A polynucleotide may have thousands of such phosphodiester linkages.

### Double-helix structure

DNA has a double-helix structure (Figure 2).
The sugar and phosphate lie on the outside of the helix, forming the backbone of the DNA.
The nitrogenous bases are stacked in the interior, like the steps of a staircase, in pairs; the pairs are bound to each other by hydrogen bonds.
Every base pair in the double helix is separated from the next base pair by 0.34 nm.
The two strands of the helix run in opposite directions, meaning that the 5′ carbon end of one strand will face the 3′ carbon end of its matching strand.
(This is referred to as antiparallel orientation and is important to DNA replication and in many nucleic acid interactions.)

!!! quote "**Figure 2**"

    <div id="dna-view" class="mol-container"></div>
    <script>
        var uri = 'https://files.rcsb.org/view/8G9O.pdb';
        jQuery.ajax( uri, {
            success: function(data) {
                // https://3dmol.org/doc/GLViewer.html
                let viewer = $3Dmol.createViewer(
                    document.querySelector('#dna-view'),
                    { backgroundAlpha: '0.0' }
                );
                viewer.addModel(data, "pdb");
                viewer.setStyle({}, {});
                viewer.setStyle({chain: 'C'}, {'stick': {}});
                viewer.setStyle({chain: 'D'}, {'stick': {}});
                // viewer.zoomTo({chain: 'D'})
                viewer.setView([ -161.09883216783226, -166.75760606060624, -143.52469930069938, -38.2880908209946, 0.5487204759120768, 0.03371018933075234, 0.12052074451927908, -0.8265858773234799 ]);
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

    Native DNA is an antiparallel double helix.
    The phosphate backbone is on the outside, and the bases are on the inside.
    Each base from one strand interacts via hydrogen bonding with a base from the opposing strand.
    PDB ID: [8G9O](https://www.rcsb.org/structure/8G9O)

Only certain types of base pairing are allowed.
For example, a certain purine can only pair with a certain pyrimidine.
This means `A` can pair with `T`, and `G` can pair with `C`, as shown in Figure 3.
This is known as the base complementary rule.
In other words, the DNA strands are complementary to each other.
If the sequence of one strand is `AATTGGCC`, the complementary strand would have the sequence `TTAACCGG`.
During DNA replication, each strand is copied, resulting in a daughter DNA double helix containing one parental DNA strand and a newly synthesized strand.

!!! quote "**Figure 3**"

    <figure markdown>
    ![](https://bio.libretexts.org/@api/deki/files/967/Figure_03_05_03.jpg){ alight=left width=500 }
    </figure>

    In a double-stranded DNA molecule, the two strands run antiparallel to one another so that one strand runs 5′ to 3′ and the other 3′ to 5′.
    The phosphate backbone is located on the outside, and the bases are in the middle.
    Adenine forms hydrogen bonds (or base pairs) with thymine, and guanine base pairs with cytosine.

## RNA

Ribonucleic acid, or RNA, is mainly involved in the process of protein synthesis under the direction of DNA.
RNA is usually single-stranded and is made of ribonucleotides that are linked by phosphodiester bonds.
A ribonucleotide in the RNA chain contains ribose (the pentose sugar), one of the four nitrogenous bases (`A`, `U`, `G`, and `C`), and the phosphate group.

There are four major types of RNA:

1.  messenger RNA (mRNA)
1.  ribosomal RNA (rRNA),
1.  transfer RNA (tRNA)
1.  microRNA (miRNA).

The first, mRNA, carries the message from DNA, which controls all of the cellular activities in a cell.
If a cell requires a certain protein to be synthesized, the gene for this product is turned "on" and the messenger RNA is synthesized in the nucleus.
The RNA base sequence is complementary to the coding sequence of the DNA from which it has been copied.
However, in RNA, the base `T` is absent and `U` is present instead.
If the DNA strand has a sequence `AATTGCGC`, the sequence of the complementary RNA is `UUAACGCG`.
In the cytoplasm, the mRNA interacts with ribosomes and other cellular machinery (Figure 4).

!!! quote "**Figure 4**"

    <figure markdown>
    ![Basic ribosome structure](https://bio.libretexts.org/@api/deki/files/968/Figure_03_05_04.jpg){ alight=left width=500 }
    </figure>

    A ribosome has two parts: a large subunit and a small subunit.
    The mRNA sits in between the two subunits.
    A tRNA molecule recognizes a codon on the mRNA, binds to it by complementary base pairing, and adds the correct amino acid to the growing peptide chain.

mRNA is read in sets of three bases known as codons.
Each codon codes for a single amino acid.
In this way, the mRNA is read and the protein product is made.
Ribosomal RNA (rRNA) is a major constituent of ribosomes on which the mRNA binds.
The rRNA ensures the proper alignment of the mRNA and the ribosomes; the rRNA of the ribosome also has an enzymatic activity (peptidyl transferase) and catalyzes the formation of the peptide bonds between two aligned amino acids.
Transfer RNA (tRNA) is one of the smallest of the four types of RNA, usually 70--90 nucleotides long.
It carries the correct amino acid to the site of protein synthesis.
It is the base pairing between the tRNA and mRNA that allows for the correct amino acid to be inserted into the polypeptide chain.
microRNAs are the smallest RNA molecules and their role involves the regulation of gene expression by interfering with the expression of certain mRNA messages.
Table 3.5.1 below summarizes the features of DNA and RNA.

**Table 1** Features of DNA and eukaryotic mRNA.

| Feature | DNA | mRNA |
| ------- | --- | ---- |
| Function | Carries genetic info | Involved in protein synthesis |
| Location | Nucleus | Cytoplasm |
| Structure | Double helix | Usually single-stranded |
| Sugar | Deoxyribose | Ribose |
| Pyrimidines | Cytosine, thymine | Cytosine, uracil |
| Purines | Adenine, guanine | Adenine, guanine   |

Even though the RNA is single-stranded, most RNA types show extensive intramolecular base pairing between complementary sequences, creating a predictable three-dimensional structure essential for their function.

As you have learned, information flow in an organism takes place from DNA to RNA to protein.
DNA dictates the structure of mRNA in a process known as transcription, and RNA dictates the structure of protein in a process known as translation.
This is known as the Central Dogma of Life, which holds for all organisms; however, exceptions to the rule occur in connection with viral infections.

## Summary

Nucleic acids are molecules made up of nucleotides that direct cellular activities such as cell division and protein synthesis.
Each nucleotide is made up of a pentose sugar, a nitrogenous base, and a phosphate group.
There are two types of nucleic acids: DNA and RNA.
DNA carries the genetic blueprint of the cell and is passed on from parents to offspring (in the form of chromosomes).
It has a double-helical structure with the two strands running in opposite directions, connected by hydrogen bonds, and complementary to each other.
RNA is single-stranded and is made of a pentose sugar (ribose), a nitrogenous base, and a phosphate group.
RNA is involved in protein synthesis and its regulation.
Messenger RNA (mRNA) is copied from the DNA, is exported from the nucleus to the cytoplasm, and contains information for the construction of proteins.
Ribosomal RNA (rRNA) is a part of the ribosomes at the site of protein synthesis, whereas transfer RNA (tRNA) carries the amino acid to the site of protein synthesis.
microRNA regulates the use of mRNA for protein synthesis.

## Acknowledgements

This content was adapted with permission from from [LibreText General Biology](https://bio.libretexts.org/Bookshelves/Introductory_and_General_Biology/Book%3A_General_Biology_(OpenStax)), Chapter 3, Section 3.5: [Nucleic Acids](https://bio.libretexts.org/Bookshelves/Introductory_and_General_Biology/Book%3A_General_Biology_(OpenStax)/1%3A_The_Chemistry_of_Life/3%3A_Biological_Macromolecules/3.5%3A_Nucleic_Acids).
