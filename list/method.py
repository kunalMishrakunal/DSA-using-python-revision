#1. append() = mainly use for add the single element in list of values.
l_1 = [1, 2, 2, 3, 3, 3, 4, 4, 4]
l_1.append(4)
print("Now this list is append the value 4: ", l_1, '\n')

#2. extend() = append selected item
l_2 = ['Ram', 'Sheeta', 'Radha', 'Krishna', 'Lakshaman']
l_2.extend('Lakshaman')
print(l_2, '\n')

#3. insert() = insert a single item at a specify index
l_3 = [2, 3, 4, 5, 5]
l_3.insert(5, 'Ram')
print(l_3, '\n')

#4. pop() = pop use to remove the element in specify index and return the item at a specify index and if we not give index then it remove defalt index
l_4 = [11, 22, 33, 44, 55]
l_4.pop(1)
print(l_4, '\n')

#5. remove() = remove method use to find and delete the very first occerence of a specify value.
l_5 = [11, 22, 33, 44, 55]
l_5.remove(11)
print(l_5, '\n')

#6. clear() = clear are use to wipes out every single item from the list, leaving it compelitely empity. it is use for create empity list.
l_6 = [10, 20, 30, 40, 50]
l_6.clear()
print(l_6, '\n')

#7. index() = index is use to Returns the zero-based index of the first occurrence of a value. Throws a ValueError if the item is missing.
l_7 = [10, 20, 30, 40, 50]
l_7.index(10, 0)
print(l_7, '\n')

#8. count() = count method is use to show how many time a specificy show up inside the list.
l_8 = [11, 22, 11, 22, 11]
print(l_8.count(11), '\n')

