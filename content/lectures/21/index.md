<h1 align="center">
<b>Lecture 21</b><br>
Predictive modeling
</h1>
<p align="center">
<b>Date:</b> Dec 3, 2024
</p>

## Learning objectives

After today, you should have a better understanding of:

1.  Define linear regression, its limitations, and objective function.
2.  Describe the purpose of loss functions in regression.
3.  Understand the conversion of data from a DataFrame to NumPy arrays.
4.  Develop hands-on programming skills for implementing regression in Python.
5.  Interpret the coefficients obtained through optimization and evaluate the model's performance.
6.  Visualize linear regression models and their fit to data.
7.  Discuss practical considerations for model interpretation, assumptions, and limitations.

Some relevant code snippets.

```python
import numpy as np
import pandas as pd

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import py3Dmol


def show_mol(smi, style="stick"):
    mol = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.MMFFOptimizeMolecule(mol, maxIters=200)
    mblock = Chem.MolToMolBlock(mol)

    view = py3Dmol.view(width=500, height=500)
    view.addModel(mblock, "mol")
    view.setStyle({style: {}})
    view.zoomTo()
    view.show()
```

```python
CSV_PATH = "https://github.com/oasci-courses/pitt-biosc1540-2024f/raw/refs/heads/main/content/lectures/21/smiles-pka-desc.csv"

df = pd.read_csv(CSV_PATH)
```
