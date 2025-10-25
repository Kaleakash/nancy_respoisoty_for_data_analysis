ll = list();    # creating empty list 
ll1 = list([1, 2, 3, 4, 5]);  # creating list with initial values
ll2 = [];
ll3 = list(range(1, 11));  # creating list with range of values from 1 to 10
print(type(ll));
print(type(ll1));
print(type(ll2));
ll.append(10);
ll.append(20);
ll.append(30);
ll.append(40);
ll.append("A")
print("Initial List: ", ll);
print("List with initial values: ", ll3);
print("Length of ll: ", len(ll));
print("get element at index 2: ", ll[0]);
print("get element at index -1 (last element): ", ll[-1]);
ll[1] = 25;  # updating element at index 1
print("List after updating index 1: ", ll);
ll.insert(2, 15);  # inserting element 15 at index 2
print("List after inserting 15 at index 2: ", ll);
ll.remove(30);  # removing element 30
print("List after removing 30: ", ll);
popped_element = ll.pop();  # removing last element
print("Popped element: ", popped_element);
print("List after popping last element: ", ll);
