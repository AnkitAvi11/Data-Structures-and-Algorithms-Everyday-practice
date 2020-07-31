List = list ()  # creating an empty list (list is nothing but an array)

#   functions to add values to a List

List.append(1)
List.append(2)

List.extend([1,2,3,7])

List.insert(4,55)

#   functions related to removing values from List
try : 
    #   remove method throws an error if the value is not in the list
    List.remove(33)
except Exception as e: 
    print(e)

List.pop() #    when no parameters are passed the last element is removed from the array

List.pop(2) #   pops out the element at the second index

del List[3] #   using delete keyword to delete an element



print("New List = ", List, end=" ")
