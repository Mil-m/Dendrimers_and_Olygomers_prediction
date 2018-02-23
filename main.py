# -*- coding: utf-8 -*-
import numpy as np
import fill_data as f
import get as g
import learning as l
import measures as m
import descriptors as d

arr_res = np.array(f.data.density)

l.cross_validation(d.arr_for_density_no_cor, arr_res, "density")

#arr_res_p = np.array(f.data_p.boiling_point)

#l.prediction_for_big_data(d.arr_for_boiling_point, d.arr_for_boiling_point_p, arr_res, arr_res_p, "boiling_point")

#m.get_Tanimoto_measures()

#g.get_smiles_by_data()