# -*- coding: utf-8 -*-
import numpy as np
import fill_data as f

#arr_2_3 = np.vstack((d.arr_data_2, d.arr_data_3))

#физические свойства
#arr_data_phys = np.array([f.data.density, f.data.refractive_index])

#химические свойства: дескрипторы RDKit
#fr_C_O_noCOO;Chi4v;MolWt;TPSA;EState_VSA8;PEOE_VSA11;PEOE_VSA10;BalabanJ;EState_VSA10;BertzCT;Kappa3;Kappa2
'''arr_data_2 = np.array([f.data.fr_C_O_noCOO, f.data.Chi4v, f.data.MolWt, f.data.TPSA, f.data.EState_VSA8,
                      f.data.PEOE_VSA11, f.data.PEOE_VSA10, f.data.BalabanJ, f.data.EState_VSA10,
                      f.data.BertzCT, f.data.Kappa3, f.data.Kappa2])'''

#химические свойства: дескрипторы Rcpi
#nAtom;ALogP;ALogp2;AMR;apol;ECCEN;TopoPSA;MW;WPATH;WPOL;Zagreb;fragC;FMF;C1SP2;C2SP2;C3SP2;C1SP3;C2SP3;C3SP3;C4SP3;BCUTw_1l;BCUTw_1h;BCUTc_1l;BCUTc_1h;BCUTp_1l;BCUTp_1h;bpol
'''arr_data_3 = np.array([f.data.nAtom, f.data.ALogP, f.data.ALogp2, f.data.AMR, f.data.apol,
                      f.data.ECCEN, f.data.TopoPSA, f.data.MW, f.data.WPATH,
                      f.data.WPOL, f.data.Zagreb, f.data.fragC, f.data.FMF,
                      f.data.C1SP2, f.data.C2SP2, f.data.C3SP2, f.data.C1SP3,
                      f.data.C2SP3, f.data.C3SP3, f.data.C4SP3, f.data.BCUTw_1l,
                      f.data.BCUTw_1h, f.data.BCUTc_1l, f.data.BCUTc_1h, f.data.BCUTp_1l,
                      f.data.BCUTp_1h, f.data.bpol])'''

#-----------------------------------------------------------------------------------------------------------------------

arr_for_density = np.array([f.data.Chi4v, f.data.fr_SH, f.data.Chi4n, f.data.fr_Al_COO, f.data.fr_furan, f.data.fr_nitroso,
                      f.data.MolWt, f.data.fr_urea, f.data.fr_benzene, f.data.fr_phos_acid,
                      f.data.fr_sulfone, f.data.VSA_EState10, f.data.fr_N_O, f.data.TPSA,
                      f.data.PEOE_VSA14, f.data.BalabanJ, f.data.nAtom, f.data.AMR,
                      f.data.apol, f.data.ECCEN, f.data.MW, f.data.WPOL,
                      f.data.Zagreb, f.data.FMF, f.data.C1SP2, f.data.BCUTw_1h])

#-----------------------------------------------------------------------------------------------------------------------

arr_for_refractive_index = np.array([f.data.fr_C_O_noCOO, f.data.Chi4v, f.data.fr_SH, f.data.SMR_VSA10, f.data.fr_halogen,
                      f.data.fr_Al_COO, f.data.fr_furan, f.data.fr_nitroso, f.data.SMR_VSA7,
                      f.data.MolWt, f.data.fr_urea, f.data.fr_benzene,
                      f.data.fr_phos_acid, f.data.fr_sulfone, f.data.VSA_EState10,
                      f.data.fr_aniline, f.data.fr_N_O, f.data.EState_VSA8, f.data.PEOE_VSA14, f.data.PEOE_VSA13,
                      f.data.PEOE_VSA12, f.data.PEOE_VSA11, f.data.PEOE_VSA10,
                      f.data.BalabanJ, f.data.EState_VSA10, f.data.HeavyAtomMolWt, f.data.fr_hdrzine,
                      f.data.Chi0, f.data.Chi1, f.data.MolLogP, f.data.fr_Al_OH,
                      f.data.fr_C_O, f.data.NumValenceElectrons, f.data.BertzCT, f.data.Kappa3,
                      f.data.Kappa2, f.data.EState_VSA6, f.data.nAtom, f.data.ALogp2, f.data.BCUTw_1l])

#-----------------------------------------------------------------------------------------------------------------------

arr_for_boiling_point = np.array([f.data.fr_C_O_noCOO, f.data.Chi4v, f.data.fr_SH, f.data.Chi4n, f.data.SMR_VSA10,
                      f.data.fr_halogen, f.data.fr_Al_COO, f.data.fr_furan, f.data.SMR_VSA7,
                      f.data.MolWt, f.data.fr_urea, f.data.fr_benzene, f.data.fr_phos_acid,
                      f.data.VSA_EState10, f.data.fr_aniline, f.data.fr_N_O, f.data.TPSA,
                      f.data.EState_VSA8, f.data.PEOE_VSA14, f.data.BalabanJ])

#--------------------------------------------------------------------------------------------------------------------no_cor

arr_for_density_no_cor = np.array([f.data.fr_SH, f.data.fr_Al_COO, f.data.fr_furan, f.data.fr_nitroso,
                f.data.fr_urea, f.data.fr_benzene, f.data.fr_phos_acid,
                f.data.VSA_EState10, f.data.fr_N_O,
                f.data.PEOE_VSA14, f.data.BalabanJ,
                f.data.WPOL, f.data.FMF, f.data.C1SP2, f.data.BCUTw_1h])

arr_for_refractive_index_no_cor = np.array([f.data.fr_SH, f.data.SMR_VSA10, f.data.fr_halogen,
                      f.data.fr_furan, f.data.fr_nitroso, f.data.SMR_VSA7,
                      f.data.fr_urea,
                      f.data.fr_phos_acid, f.data.VSA_EState10,
                      f.data.fr_aniline, f.data.fr_N_O, f.data.PEOE_VSA14,
                      f.data.PEOE_VSA12, f.data.PEOE_VSA11,
                      f.data.EState_VSA10,
                      f.data.MolLogP,
                      f.data.BertzCT, f.data.Kappa3,
                      f.data.EState_VSA6, f.data.ALogp2, f.data.BCUTw_1l])

#--------------------------------------------------------------------------------------------------------------------phys

#arr_for_density_phys = np.array([f.data.refractive_index, f.data.boiling_point])
#arr_for_refractive_index_phys = np.array([f.data.density, f.data.boiling_point])
