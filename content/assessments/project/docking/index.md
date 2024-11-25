<h1 align="center">
<b>Part 3:</b><br>
Docking
</h1>

!!! danger "DRAFT"
    This page is a work in progress and is subject to change at any moment.

| PDB ID | Additional ligand |
| ------ | ----------------- |
| [3FRD](https://www.rcsb.org/structure/3FRD) | [Folate]( https://www.ebi.ac.uk/chembl/explore/compound/135398658) |
| [6PRA](https://www.rcsb.org/structure/6PRA) | None |
| [6PRB](https://www.rcsb.org/structure/6PRB) | [OWM]( https://www.ebi.ac.uk/chembl/explore/compound/146170546) |

## Instructions

We will be using [MolModa][molmoda] to perform protein-ligand docking of *S. aureus* DHFR.

### Protein preparation

Download the following PDB structures and load them into [MolModa][molmoda] using `File` -> `PDB ID`.

-   `3FRD`
-   `6PRA`
-   `6PRB`

Prepare each structure for docking by remove all non-polymer atoms (e.g., water molecules and co-crystallized ligands) except for NADP(H).

### Docking analysis

| Label | Inhibitor | Average IC50 ± SEM (nM) | Average Ki ± SEM (nM) | MIC (µg/mL) |
|-------| ----------|-------------------------|-----------------------|-------------|
| 11a | [`CHEMBL2042372`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042372) | 6.3 ± 0.3 | 1.2 ± 0.1 | 0.0625-0.25 |
| 11b | [`CHEMBL2042373`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042373) | 5.5 ± 1.0 | 1.1 ± 0.2 | 0.0469-0.0938 |
| 11c | [`CHEMBL2042374`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042374) | 8.7 ± 2.1 | 1.7 ± 0.4 | 0.0938-0.1875 |
| 11d | [`CHEMBL2042375`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042375) | 8.2 ± 0.5 | 1.6 ± 0.1 | 0.0938-0.25 |
| 11e | [`CHEMBL2042376`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042376) | 9.2 ± 0.5 | 1.8 ± 0.1 | 0.125-0.25 |
| 11f | [`CHEMBL2042377`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042377) | 13.1 ± 3.1 | 2.6 ± 0.6 | 0.5 |
| 11g | [`CHEMBL551038`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL551038) | 4.6 ± 0.7 | 0.9 ± 0.1 | 0.1875-0.375 |
| 11h | [`CHEMBL565020`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL565020) | 4.1 ± 0.4 | 0.8 ± 0.1 | 0.125-0.25 |
| 11i | [`CHEMBL2042475`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042475) | 5.8 ± 0.3 | 1.1 ± 0.1 | 0.125-0.25 |
| 11j | [`CHEMBL550083`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL550083) | 8.4 ± 1.7 | 1.7 ± 0.3 | 0.0469-0.1875 |
| 11k | [`CHEMBL2042476`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042476) | 7.2 ± 0.8 | 1.4 ± 0.2 | 0.25 |
| 11l | [`CHEMBL2042477`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042477) | 4.8 ± 0.8 | 0.9 ± 0.2 | 0.125 |
| 11m | [`CHEMBL2042478`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042478) | 5.7 ± 0.6 | 1.1 ± 0.1 | 0.125-0.375 |
| 11n | [`CHEMBL2042479`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042479) | 7.0 ± 0.3 | 1.4 ± 0.1 | 0.25-0.5 |
| 11o | [`CHEMBL2042480`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042480) | 11.6 ± 2.2 | 2.3 ± 0.4 | 0.5 |
| 11p | [`CHEMBL2042481`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042481) | 6.3 ± 1.9 | 1.2 ± 0.4 | 0.5 |
| 11q | [`CHEMBL2042482`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2042482) | 9.6 ± 0.5 | 1.9 ± 0.1 | 1 |
| 12a | N/A | 7.7 ± 2.9 | 1.5 ± 0.6 | 1 |
| 12b | [`CHEMBL4799218`]( https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4799218) | 5.8 ± 3.3 | 1.1 ± 0.7 | 1 |
| 12c | [`CHEMBL4781757`](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4781757) | 3.3 ± 1.7 | 0.7 ± 0.3 | 1 |
| 12d | N/A | 6.7 ± 3.9 | 1.3 ± 0.8 | 0.5-1 |
| 12e | N/A | 6.3 ± 2.8 | 1.2 ± 0.6 | 0.5 |
| 12f | N/A | 5.6 ± 2.8 | 1.1 ± 0.6 | 0.5 |
| 12g | N/A | 4.5 ± 2.6 | 0.9 ± 0.5 | 1 |
| 12h | N/A | 4.5 ± 2.2 | 0.9 ± 0.4 | 1 |
| 12i | N/A | 5.4 ± 3.1 | 1.1 ± 0.6 | 0.5 |
| 12j | N/A | 5.2 ± 2.3 | 1.0 ± 0.5 | 0.5 |
| 13a | N/A | 8.4 ± 3.8 | 1.7 ± 0.7 | 0.5-1 |
| 13b | [`CHEMBL4790501`](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4790501) | 6.1 ± 2.7 | 1.2 ± 0.5 | 0.5-1 |
| 13c | N/A | 5.2 ± 3.0 | 1.0 ± 0.6 | 0.5 |
| 13d | N/A | 7.2 ± 3.2 | 1.4 ± 0.6 | 0.5 |
| 13e | N/A | 7.4 ± 4.2 | 1.5 ± 0.8 | 0.5 |
| 13f | N/A | 6.1 ± 2.7 | 1.2 ± 0.5 | 0.5 |

??? quote "SMILES"

    | Label | SMILES |
    | ----- | ------ |
    | 11a | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](CCC)c4c(C=N3)cccc4` |
    | 11b | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](C(C)C)c4c(C=N3)cccc4` |
    | 11c | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](CCC(F)(F)F)c4c(C=N3)cccc4` |
    | 11d | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](CC(C)C)c4c(C=N3)cccc4` |
    | 11e | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3/C(=C/C(C)C)c4c(C=N3)cccc4` |
    | 11f | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](C(CC)CC)c4c(C=N3)cccc4` |
    | 11g | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](C4CCCCC4)c5c(C=N3)cccc5` |
    | 11h | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](c4ccccc4)c5c(C=N3)cccc5` |
    | 11i | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](c4c(cccc4)C)c5c(C=N3)cccc5` |
    | 11j | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](c4ccc(cc4)C)c5c(C=N3)cccc5` |
    | 11k | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@@H](c4c(C=N3)cccc4)c5cc(C)cc(c5)C` |
    | 11l | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](c4cc(ccc4)F)c5c(C=N3)cccc5` |
    | 11m | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](c4ccc(cc4)F)c5c(C=N3)cccc5` |
    | 11n | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@@H](c5c(C=N3)cccc5)Cc4ccccc4` |
    | 11o | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@@H](c5c(C=N3)cccc5)Cc4ccc(C)cc4` |
    | 11p | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](c5c(C=N3)cccc5)Cc4ccc(OC)cc4` |
    | 11q | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@@H](c5c(C=N3)cccc5)Cc4ccc(cc4)OC(F)(F)F` |
    | 12a | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@@H](CC)c4c(C=N3)cc(OC)c(c4)OC` |
    | 12c | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](C4CC4)c5c(C=N3)cc(OC)c(c5)OC` |
    | 12d | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](C=C)c4c(C=N3)cc(OC)c(c4)OC` |
    | 12e | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](C=C(C)C)c4c(C=N3)cc(OC)c(c4)OC` |
    | 12f | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](c4ccccc4)c5c(C=N3)cc(OC)c(c5)OC` |
    | 12g | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](c4c(cccc4)C)c5c(C=N3)cc(OC)c(c5)OC` |
    | 12h | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@@H](c4c(cccc4)CC)c5c(C=N3)cc(OC)c(c5)OC` |
    | 12i | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@@H](c4c(cccc4)OC)c5c(C=N3)cc(OC)c(c5)OC` |
    | 12j | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@@H](c4ccc(cc4)OC)c5c(C=N3)cc(OC)c(c5)OC` |
    | 13a | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@@H](CC)c4c(C=N3)cc(C)c(c4)C` |
    | 13b | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@@H](CCC)c4c(C=N3)cc(C)c(c4)C` |
    | 13c | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](C4CC4)c5c(C=N3)cc(C)c(c5)C` |
    | 13d | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](C=C)c4c(C=N3)cc(C)c(c4)C` |
    | 13e | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](C=C(C)C)c4c(C=N3)cc(C)c(c4)C` |
    | 13f | `Nc1nc(N)c(cn1)Cc2cc(c(c(c2)OC)OC)/C=C/C(=O)N3[C@H](c4ccccc4)c5c(C=N3)cc(C)c(c5)C` |

<!-- LINKS -->

[molmoda]: https://durrantlab.pitt.edu/molmoda/#
