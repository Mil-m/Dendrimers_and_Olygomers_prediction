# -*- coding: utf-8 -*-
from pandas import read_csv
from time import gmtime, strftime
import get as g
from scipy.stats import pearsonr
import numpy as np
#import descriptors as d

#data = read_csv('./input/OUT_prop_for_o.csv', delimiter=";")
#data = read_csv('./input/OUT_prop_for_o_d.csv', delimiter=";")

data = read_csv('./input/Table_properties_o_d_density.csv', delimiter=";")
#data = read_csv('./input/Table_properties_o_d_ref_idx.csv', delimiter=";")
#data = read_csv('./input/Table_properties_o_b_point.csv', delimiter=";")

out_dict = {}
#кол-во всех веществ
#out_dict["Count"] = len(data)
#количество пустых значений
#физические свойства
#out_dict["Generation"] = len(data.Generation[data.Generation.isnull()]) #null_g
#out_dict["volume"] = len(data.volume[data.volume.isnull()]) #null_v
#out_dict["pH"] = len(data.pH[data.pH.isnull()]) #null_pH
#out_dict["viscosity"] = len(data.viscosity[data.viscosity.isnull()]) #null_vi
#out_dict["transition_temp"] = len(data.transition_temp[data.transition_temp.isnull()]) #null_tp
#out_dict["density"] = len(data.density[data.density.isnull()]) #null_d
#out_dict["boiling_point"] = len(data.boiling_point[data.boiling_point.isnull()]) #null_bp
#out_dict["refractive_index"] = len(data.refractive_index[data.refractive_index.isnull()]) #null_ri
#out_dict["freezing_point"] = len(data.freezing_point[data.freezing_point.isnull()]) #null_fp
#out_dict["solubility"] = len(data.solubility[data.solubility.isnull()]) #null_solub
#out_dict["solution"] = len(data.solution[data.solution.isnull()]) #null_solut
#out_dict["PSA"] = len(data.PSA[data.PSA.isnull()]) #null_PSA

#заполнение всех пустых ячеек средними значениями (для цифр)
#if (out_dict["Generation"] != out_dict["Count"]):
#    data.Generation[data.Generation.isnull()] = data.Generation.median()

#химические свойства
#fr_C_O_noCOO;Chi4v;MolWt;TPSA;EState_VSA8;PEOE_VSA11;PEOE_VSA10;BalabanJ;EState_VSA10;BertzCT;Kappa3;Kappa2

def fill_data(data):
    for head in data:
        if (head != "Generation"):
            for i in range(len(data[head])):
                if (not isinstance(data[head][i], str)):
                    if (np.isnan(data[head][i])):
                        try:
                            data[head][i] = data[head].median()
                        except:
                            err = True

fill_data(data)

for key in out_dict:
    print key, out_dict[key]

#-----------------------------------------------------------------------------------------------Table_with_median_values
#1 -> возвращение входной таблицы после заполнения пустых ячеек
#необходима для дальнейших подсчетов
flag_for_write = 1

if (flag_for_write):
    file_name = "./output/OUT_prop.csv"
    f_out_table = open(file_name, 'w')
    str_head_out = ""
    str_out = ""
    for i in range(0, len(data)):
        #заполнение заголовка таблицы
        if (i == 0):
            for head in data:
                str_head_out += str(head) + ";"
        #если дендример - (if not pd.isnull(data.Core[i]))
        #if (isinstance(data.Core[i], str)):
        #для всех заголовков датафрейма
        for head in data:
            if ((data[head][i] is float and np.isnan(data[head][i])) or (data[head][i] is str and len(data[head][i]) == 0)):
                str_out += ";"
            else:
                str_out += str(data[head][i]) + ";"
        str_out += "\n"
    f_out_table.write(str_head_out + "\n")
    f_out_table.write(str_out + "\n")
    f_out_table.close()

#------------------------------------------------------------------------------------------------------RDKit_Descriptors
#1 -> заполнение таблицы с RDKit-дескрипторами
flag_rdkit = 0

def get_rdkit_descriptors(f_out_rdkit):

    str_head_out = ""
    str_out = ""
    for i in range(0, len(data.Core)):
        #если дендример
        core, branch, terminal_branch, generation = data.Core[i], data.Branch[i], data.Terminal_Branch[i], data.Generation[i]
        if (isinstance(data.Core[i], str)):
            core, file_name = g.get_smiles(core, branch, terminal_branch, generation)
            core_for_table = data.Core[i]
        else:
            core = data.SMILES[i]
            core_for_table = data.Name[i]

        #print "get_descriptors"
        desc_dict = g.get_descriptors_by_smiles(core)

        #заполнение заголовка таблицы
        if (i == 0):
            str_head_out += "core;branch;terminal_branch;generation;"
            for key in desc_dict:
                str_head_out += key + ";"

        str_out += str(core_for_table) + ";" + str(branch) + ";" + str(terminal_branch) + ";" + str(generation) + ";"
        for key in desc_dict:
            str_out += str(desc_dict[key]) + ";"
        str_out += "\n"

    f_out_rdkit.write(str_head_out + "\n")
    f_out_rdkit.write(str_out + "\n")

if (flag_rdkit):
    file_name = "./output/OUT_RDKit_for_o_d.csv"
    f_out_rdkit = open(file_name, 'w')
    print "Calculation of descriptors...", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    get_rdkit_descriptors(f_out_rdkit)
    f_out_rdkit.close()

#----------------------------------------------------------------------------------------------------------Pearson_table
flag_pearson = 0

arr_for_boiling_point_cor = np.array(["fr_C_O_noCOO", "Chi4v", "fr_SH", "Chi4n", "SMR_VSA10",
                      "fr_halogen", "fr_Al_COO", "fr_furan", "SMR_VSA7",
                      "MolWt", "fr_urea", "fr_benzene", "fr_phos_acid",
                      "VSA_EState10", "fr_aniline", "fr_N_O", "TPSA",
                      "EState_VSA8", "PEOE_VSA14", "BalabanJ"])

def pearson_affinity(data):
    file_name = "./output/Table_pearson_boiling_point.csv"
    f_out_pearson = open(file_name, 'w')
    array = []
    for b in data:
        for a in data:
            if (a in arr_for_boiling_point_cor) and (b in arr_for_boiling_point_cor):
                if (a != b):
                    try:
                        pearson = pearsonr(data[a], data[b])
                        if (pearson[0] >= 0.9):
                            f_out_pearson.write(str(a) + ";" + str(b) + ";" + str(pearson[0]) + "\n")
                            array.append(pearson[0])
                    except:
                        err = 1
    f_out_pearson.close()
    return 1 - np.array(array)

if (flag_pearson):
    p_arr = pearson_affinity(data)
    '''p_res_arr = []
    for el in p_arr:
        if (isinstance(el, float)):
            if (not np.isnan(el)):
                p_res_arr.append(el)'''

