# simple function no passing parameter and no return type 
# def hello():
#     print("Welcome to user defined function")

# hello();

# # function passing parameter but no return type 
# def add(a,b):
#     sum = a+b;
#     print("sum of two number is ",sum)

# add(10,20);

# # function passing parameter and return value 

# def checkLoginDetails(emailId,password):
#     if emailId=='admin@gmail.com' and password=='123':
#         return True;
#     else:
#         return False;

# result1 = checkLoginDetails('admin@gmail.com','123')
# print(result1)
# result2 = checkLoginDetails('admin@gmail.com',4444)
# print(result2)

# function with default arguments 
# def empDetails(id=0,name="UnKnown",salary=800):
#     print('id is ',id,'name is ',name,'salary is ',salary)

# empDetails(100,"John",1500);
# empDetails(101,'Steven')
# empDetails(102)
# empDetails()

# function with return more than one value 
# def operation(a,b):
#     add = a+b;
#     sub = a-b;
#     mul = a*b;
#     div = a/b
#     return add,sub,mul,div;
# result = operation(10,5);
# print(result)
# print('sum is ',result[0])
# print('sub is ',result[1])
# print('mul is ',result[2])
# print('div is ',result[3])

# recursive function : calling same function again and again 
# def factorial(n):
#     if n == 1:
#         return 1;
#     elif n <1:
#         return "Invalid input";
#     else:
#         return n*factorial(n-1);

# print(factorial(1))
# print(factorial(0))
# print(factorial(-10))
# print(factorial(3));

# lambda function : if we want to write shortest code ie one line lambda function prefarable 
# def add(a,b):
#     return a+b;
# print("Sum of two number without lambda is ",add(10,20))

# sum = lambda a,b:a+b;
# print("Sum of two number using lambda style is ",sum(10,20));

# num_list = [1,2,3,4,5,6,7,8,9,10]
# square_list = list(map(lambda x:x*2,num_list))
# cube_list = list(map(lambda x:x*3,num_list))
# print(num_list)
# print(square_list)
# print(cube_list)

# callback function : passing the function itself or function body to another function as parameter list 
# nested function : function within another function is known as nested function 

def main():
    #pass;
    def add(a,b):
        return a+b;
    def sub(a,b):
        return a-b;
    def mul(a,b):
        return a*b;
    def div(a,b):
        return a/b;
    def calculation(a,b,callback):
        return callback(a,b);
    print("Sum of two number is ",calculation(10,20,add))
    print("Sub of two number is ",calculation(10,20,sub))
    print("Mul of two number is ",calculation(10,20,mul))
    print("Div of two number is ",calculation(10,20,div))
    print("Sum of two number using lambda style ",calculation(4,2,lambda a,b:a+b))
    print("Sub of two number using lambda style ",calculation(4,2,lambda a,b:a-b))
    print("Mul of two number using lambda style ",calculation(4,2,lambda a,b:a*b))
    print("Div of two number using lambda style ",calculation(4,2,lambda a,b:a/b))
main();
