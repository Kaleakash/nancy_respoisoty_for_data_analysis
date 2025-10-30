# import numpy as np;
# np_data = np.array([1,2,3,4,5,6]);
# print("numPy data",np_data)
# result = np_data*2;
# print("NumPy with X multiple by 2 ",result)

import numpy as np;
import time;
list_data = np.arange(1,10000000)
start = time.time();
sum = sum(list_data);
end = time.time();
print("NumPy sum",sum,"time ",round(start-end))