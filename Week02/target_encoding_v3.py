import numpy as np
from collections import OrderedDict

def target_mean_v8(data, y_name, x_name):
    n = data.shape[0]
    result = np.zeros(n)
    X = data[x_name].values
    Y = data[y_name].values
    value_dict = OrderedDict()
    count_dict = OrderedDict()
    for x, y in zip(X, Y):
        if x not in value_dict.keys():
            value_dict[x] = y
            count_dict[x] = 1
        else:
            value_dict[x] += y
            count_dict[x] += 1
    result = [(value_dict[x] - y) / (count_dict[x] - 1) for x, y in zip(X, Y)]
    return np.array(result)