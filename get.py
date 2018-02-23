# -*- coding: utf-8 -*-
from rdkit import Chem
from rdkit.Chem import Descriptors
import re
import fill_data as f

def get_smiles(core, branch, terminal_branch, generation):
    file_name = "./input/SMILES/" + str(core) + "_" + str(branch) + "_" + str(terminal_branch) + "_" + str(generation) + ".smi"
    f_out = open(file_name, 'w')
    #стандартное формирование ветви
    if (type(terminal_branch) is float):
        if (generation.is_integer()):
            generation = int(generation)
            for n_gen in range(0, generation+1):
                if (n_gen != generation):
                    core = core.replace('*', branch.strip())
                else:
                    branch = branch.strip()
                    #new_branch - для удаления всех (*)
                    new_branch = branch[0:len(branch)-6]
                    core = core.replace('*', new_branch)
            f_out.write(core)
            f_out.write("\n")
            f_out.close()
        else:
            #формирование ветки нецелого поколения
            generation = int(generation)
            #место деления ветки пополам
            medium_pattern = re.findall(r'\)\w+\(', core)[0]
            for n_gen in range(0, generation+1):
                if (n_gen != generation):
                    core = core.replace('*', branch.strip())
                else:
                    branch = branch.strip()
                    core = core.replace('*', branch)
            branch = branch.strip()
            new_branch = branch[0:len(branch)-6]
            split_core = core.split(medium_pattern)
            #заменяем левую ветвь
            split_core[0] = split_core[0].replace('*', new_branch)
            new_core = split_core[0] + medium_pattern + split_core[1]
            new_core = new_core.replace('(*)(*)', "")
            f_out.write(new_core)
            f_out.write("\n")
            f_out.close()

    if (type(terminal_branch) is str):
        if (generation.is_integer()):
            print "War: generation is integer for: core=", core, "; branch=", branch, "; terminal_branch=", terminal_branch, "; generation=", generation
        #формирование ветки нецелого поколения
        generation = int(generation)
        for n_gen in range(0, generation+1):
            if (n_gen != generation):
                core = core.replace('*', branch.strip())
            else:
                branch = branch.strip()
                core = core.replace('*', branch)
        core = core.replace('*', terminal_branch.strip())
        f_out.write(core)
        f_out.write("\n")
        f_out.close()

    return core, file_name

def get_smiles_by_data():
    for i in range(0, len(f.data.Core)):
        #если дендример
        if (isinstance(f.data.Core[i], str)):
            core, branch, terminal_branch, generation = f.data.Core[i], f.data.Branch[i], f.data.Terminal_Branch[i], f.data.Generation[i]
            core, file_name = get_smiles(core, branch, terminal_branch, generation)

def get_descriptors_by_smiles(core):
    desc_dict = {}
    mol = Chem.MolFromSmiles(core)
    for descName, descFn in Descriptors._descList:
        try:
            desc_dict[descName] = descFn(mol)
        except:
            desc_dict[descName] = ''
        #print descName, desc_dict[descName]
    return desc_dict