
ss2 = set()
ss3 = {1, 2, 3}
ss4 = set([1, 2, 3])
ss5 = set(range(1,10));
ss6 = {4,6,2,8,9,5,1,2,"A","B"}
print(ss6)
print(ss5)
print(type(ss2)) 
print(type(ss3)) 
print(type(ss4))
ss2.add(1)
ss2.add(2)
ss2.add(3)
ss3.add(3)
print(ss2)
ss2.discard(2)
ss2.discard(10)
ss2.remove(1)
pop_element = ss2.pop();
#ss2.remove(8)   # if element not present it generate the error 
print(ss2)
print(ss2)
print(pop_element)
