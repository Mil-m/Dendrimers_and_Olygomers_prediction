# -*- coding: utf-8 -*-
from sklearn.tree import DecisionTreeRegressor
from sklearn import preprocessing
from sklearn.svm import SVR
from sklearn.cross_decomposition import PLSRegression
from sklearn.linear_model import ARDRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.utils import shuffle
from scipy.sparse import coo_matrix
import matplotlib.pyplot as plt
import scipy
import numpy as np
from sklearn.model_selection import LeaveOneOut
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import fill_data as f

def get_plot(Y_e, Y_p, target_str):
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(Y_e, Y_p)
    #for trend-line
    predict_y = intercept + slope * Y_e
    equal = ""
    if (intercept > 0):
        equal = "y = " + str(slope) + "*x" + "+" + str(intercept)
    else:
        equal = "y = " + str(slope) + "*x" + str(intercept)

    R = r_value**2
    str_label = "R-squared = " + str(R)

    file_name = "./output/OUT_for_plot.csv"
    f_out_table = open(file_name, 'w')
    f_out_table.write("Experimental;Computed\n")
    for i in range(0, len(Y_e)):
        str_out = str(Y_e[i]) + ";" + str(Y_p[i])
        f_out_table.write(str_out + "\n")
    f_out_table.close()

    '''facecolor = (1.0, 1.0, 1.0, .5)
    fig, ax = plt.subplots(1)
    ax.scatter(list(Y_e), list(Y_p),
               facecolor=facecolor,
               s=20,
               linewidths=1,
               edgecolors='k')'''
    # Plot the results
    plt.plot(list(Y_e), list(Y_p), 'o', color="black", alpha=0.3, markeredgecolor="black", markeredgewidth=0.5, antialiased=True)
    plt.plot(list(Y_e), predict_y, 'k-', color="black")
    plt.xlabel("Experimental values")
    plt.ylabel("Predicted values")
    plt.title("Decision Tree for " + target_str + ": " + str_label + "\n" + equal)
    plt.show()

def build_tree(X_train, Y_train, X_tagret, Y_target, target_str):
    clf = DecisionTreeRegressor(criterion='mse', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1,
                                min_weight_fraction_leaf=0.0, max_features=None, random_state=0, max_leaf_nodes=None,
                                min_impurity_split=1e-07, presort=False)
    clf.fit(X_train, Y_train)
    Y_p = clf.predict(X_tagret)
    #get PLOT
    Y_e = np.array(Y_target)
    #get_plot(Y_e, Y_p, target_str)
    return Y_e, Y_p

def build_SVR(X_train, Y_train, X_tagret, Y_target, target_str):
    clf = SVR()
    #normalized_X = preprocessing.normalize(X_train)
    clf.fit(X_train, Y_train)
    Y_p = clf.predict(X_tagret)
    Y_e = np.array(Y_target)
    return Y_e, Y_p

def build_PLSRegression(X_train, Y_train, X_tagret, Y_target, target_str):
    clf = PLSRegression()
    clf.fit(X_train, Y_train)
    Y_p = clf.predict(X_tagret)
    Y_e = np.array(Y_target)
    return Y_e, Y_p

def build_ARDRegression(X_train, Y_train, X_tagret, Y_target, target_str):
    clf = ARDRegression()
    clf.fit(X_train, Y_train)
    Y_p = clf.predict(X_tagret)
    Y_e = np.array(Y_target)
    return Y_e, Y_p

def cross_validation(arr_data, arr_res, target_str):
    #simple
    arr_data = arr_data.transpose()
    #перемешать индексы
    arr_sparse = coo_matrix(arr_data)

    #для перемешивания 3-х массивов
    buf_arr_res = np.vstack((arr_res, f.data.Name)).transpose()

    arr_data, arr_sparse, buf_arr_res = shuffle(arr_data, arr_sparse, buf_arr_res, random_state=0)

    #переписать arr_res и записать данные в файл
    arr_res = []
    file_name = "./output/OUT_for_plot_data.csv"
    f_out_table = open(file_name, 'w')
    f_out_table.write("Name;Experimental\n")
    for i in range(0, len(buf_arr_res)):
        arr_res.append(buf_arr_res[i][0])
        #if (i >= k):
        f_out_table.write(str(buf_arr_res[i][1]) + ";" + str(buf_arr_res[i][0]) + "\n")
    f_out_table.close()
    arr_res = np.array(arr_res)

    X_train, X_tagret, Y_train, Y_target = train_test_split(arr_data, arr_res, test_size=0.70)
    #print np.shape(X_train), np.shape(X_tagret), np.shape(Y_train), np.shape(Y_target)

    loo = LeaveOneOut()
    Y_p = []
    rmse_arr = []
    for train_index, test_index in loo.split(X_train):
        X_train_loo, X_tagret_loo = X_train[train_index][:], X_train[test_index][:]
        Y_train_loo, Y_target_loo = Y_train[train_index], Y_train[test_index]
        _, el_p = build_tree(X_train_loo, Y_train_loo, X_tagret_loo, Y_target_loo, target_str)
        #_, el_p = build_SVR(X_train, Y_train, X_tagret, Y_target, target_str)
        #_, el_p = build_PLSRegression(X_train, Y_train, X_tagret, Y_target, target_str)
        #_, el_p = build_ARDRegression(X_train, Y_train, X_tagret, Y_target, target_str)
        Y_p.append(el_p[0])
        #Y_p.append(el_p[0][0])
        rmse_arr.append(mean_squared_error(Y_target_loo, [el_p[0]]))

    #Y_p = np.array(Y_p)
    rmse_arr = np.array(rmse_arr)
    print "RMSE train (mean) =", rmse_arr.mean()

    arr_e, arr_p = build_tree(X_train, Y_train, X_tagret, Y_target, target_str)
    print "RMSE test = ", mean_squared_error(arr_e, arr_p)

    get_plot(arr_e, arr_p, target_str)

    return

def prediction_for_big_data(arr_data, arr_data_p, arr_res, arr_res_p, target_str):

    arr_data = arr_data.transpose()
    arr_data_p = arr_data_p.transpose()

    X_train = arr_data
    Y_train = arr_res

    X_tagret = arr_data_p
    Y_target = arr_res_p

    Y_e, Y_p = build_tree(X_train, Y_train, X_tagret, Y_target, target_str)
    get_plot(Y_e, Y_p, target_str)

