# list_data = [1,2,3,4,5,6];
# print("list data is ",list_data)
# result = [x*2 for x in list_data];
# print("List with X multiple by 2 ",result)

import time;
list_data = list(range(1,10000000));
start = time.time();
sum = sum(list_data);
end = time.time();
print("List sum",sum,"time ",round(start-end))