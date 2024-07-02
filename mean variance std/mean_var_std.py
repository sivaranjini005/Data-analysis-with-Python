import numpy as np

def calculate(list_):
    if len(list_) != 9:
        raise ValueError('List must contain nine numbers')
    array_ = np.array(list_).reshape(3,3)

    mean_ax0 = np.mean(array_, axis = 0)
    mean_ax1 = np.mean(array_, axis = 1)
    mean_all = np.mean(array_)

    var_a0 = np.var(array_, axis = 0)
    var_a1 = np.var(array_, axis = 1)
    var_al = np.var(array_)

    var_ax0 = np.around(var_a0, decimals= 3)
    var_ax1 = np.around(var_a1, decimals= 3)
    var_all = np.around(var_al, decimals= 3)


    std_a0 = np.std(array_, axis = 0)
    std_a1 = np.std(array_, axis = 1)
    std_al = np.std(array_)

    std_ax0 = np.around(std_a0, decimals= 3)
    std_ax1 = np.around(std_a1,decimals= 3)
    std_all = np.around(std_al, decimals= 3)

    max_ax0 = np.max(array_, axis = 0)
    max_ax1 = np.max(array_, axis = 1)
    max_all = np.max(array_)

    min_ax0 = np.min(array_, axis = 0)
    min_ax1 = np.min(array_, axis = 1)
    min_all = np.min(array_)

    sum_ax0 = np.sum(array_, axis = 0)
    sum_ax1 = np.sum(array_, axis = 1)
    sum_all = np.sum(array_)

    return {'mean': [mean_ax0.tolist(), mean_ax1.tolist(), float(mean_all)],
            'variance': [var_ax0.tolist(), var_ax1.tolist(), float(var_all)],
            'standard_deviation': [std_ax0.tolist(), std_ax1.tolist(), float(std_all)],
            'max': [max_ax0.tolist(), max_ax1.tolist(), float(max_all)],
            'min': [min_ax0.tolist(), min_ax1.tolist(), float(min_all)],
            'sum': [sum_ax0.tolist(), sum_ax1.tolist(), float(sum_all)]}

    
