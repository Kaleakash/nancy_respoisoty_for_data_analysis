d1 = {}
emp1 = {
    "id":100,
    "name":"Raj Deep",
    "salary":45000,
    "age":21
}
emp2 = dict(id=101,name="John",salary=34000,age=36);
print(type(d1))
print(type(emp1))
print(type(emp2))
print(emp1)
print(emp2)
print(emp1.get("id"))
print(emp2.get("name"))
emp1["salary"]=48000;
print(emp1)
emp1.pop("age");
print(emp1)