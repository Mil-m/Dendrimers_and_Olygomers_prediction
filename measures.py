# -*- coding: utf-8 -*-
import pybel
import fill_data as f
import get as g

def get_Tanimoto(smiles1, smiles2):
    try:
        mol1 = pybel.readstring("smi", smiles1)
        mol2 = pybel.readstring("smi", smiles2)
        fp1 = mol1.calcfp()
        fp2 = mol1.calcfp()
    except:
        return "", "", -1
    return mol1.formula, mol2.formula, fp1 | fp2

def get_Tanimoto_by_data():
    SMILES = []
    for i in range(0, len(f.data.Core)):
        #если дендример
        if (isinstance(f.data.Core[i], str)):
            core, branch, terminal_branch, generation = f.data.Core[i], f.data.Branch[i], f.data.Terminal_Branch[i], f.data.Generation[i]
            core, _ = g.get_smiles(core, branch, terminal_branch, generation)
        else:
            core = f.data.SMILES[i]
            SMILES.append(core)

    for i in range(0, len(SMILES)):
        for j in range(0, len(SMILES)):
            if (i != j):
                formula1, formula2, measure_t = get_Tanimoto(SMILES[i], SMILES[j])
                print i, j, formula1, formula2, measure_t