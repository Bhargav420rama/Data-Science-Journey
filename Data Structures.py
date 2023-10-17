'''
--Datastructures/Collection types in Python helps to store more than one value

There are 4 collection types majorly used

- List
-Tuple
-Set
-Dict

List====================

# List is similar to arrays in other programming languages
# List is an orderly collection of valid python values
# A list can be created by enclosing values separated by commas in square brackets
#Lists are mutable, which means the values in the list can be changed
'''
int_list = [1, 2, 3, 4, 5]
print(int_list[:])  # output: [1, 2, 3, 4, 5]

# empty list
empty_list = []
print(empty_list)  # output:[]

# mixed value list
mixed_list = [1, 'a', 3.0, 21, True]
print(mixed_list)  # output:[1, 'a', 3.0, 21, True]

# Nested Lits---A list can contain another list as a value

list_in_list = [[1, 2, 3], 'bhragav', 3.45]
print(list_in_list)  # output:[[1, 2, 3], 'bhragav', 3.45]

'''
#Indexing in List
=================
->The values in the list can be identified with an index either from left or from right
-> For values starting from left, Index value starts from 0
-> for values starting from right, Index value starts from -1
'''

list1 = ['bhargav', 'sindu', 'viswaroop', 'sravya']

print(list1[0])  # output: bhargav
print(list1[2])  # output: viswaroop
print(list1[-2])  # output: viswaroop
# print(list1[-5])  #output: IndexError: list index out of range
# print(list[10])   #output: IndexError: list index out of range


list1[0] = 'Bhragavarama'
print(
    list1)  # output:['Bhragavarama', 'sindu', 'viswaroop', 'sravya'] ---The value in 0th index was overridden by new value

'''
Adding an element
===========================================

3 different methods available to add an element
-Append
-Insert
-Extend

Append
========
* Append is a function operated on the list to add values to the existing list
* values are appended only at the end of the list
========
'''
list1.append('maxi')

print(list1)  # output: ['Bhragavarama', 'sindu', 'viswaroop', 'sravya', 'maxi']

'''
Insert
========
* Insert is a function operated to add an element to the existing list at any Index required
* Syntax is :  listname.insert(Index, new_value)
========
'''
list1.insert(4, 'chocky')

print(list1)  # output: ['Bhragavarama', 'sindu', 'viswaroop', 'sravya', 'chocky', 'maxi']

'''
Extend
==========
* Extend is a function used to combine lists, adding all items from one list to the end of another
'''
list2 = ['baby1','baby2','maxi']
list1.extend(list2)
print(list1)  #output:['Bhragavarama', 'sindu', 'viswaroop', 'sravya', 'chocky', 'maxi', 'baby1', 'baby2','maxi']

'''
Removing an element
=========================================
--In order to remove an element or elements in a list, we have below methods
*Remove()
*Pop()
*clear()
*del()

Remove()
============
* Remove function removes the first occurance of the element
*syntax is: listname.remove(objectname)
'''
#Although Maxi element exists more than once, it only elminates/removes first occurance which is at Index 5
list1.remove("maxi")
print(list1)
#output: ['Bhragavarama', 'sindu', 'viswaroop', 'sravya', 'chocky', 'baby1', 'baby2', 'maxi']

'''
Del()
=============
* Del function removes a value at certain index
* It also allows to remove multiple items based on the range provided
* Syntax is: Del listname(Index) ,  Del listname([Indexfrom: Index till])
*while using Del listname([Indexfrom: Index till]), Index till is exclusive which means if we say 7, it is 6(7-1) 
'''
# To delete baby1, its index is 5

del list1[5]
print(list1)    #output:['Bhragavarama', 'sindu', 'viswaroop', 'sravya', 'chocky', 'baby2', 'maxi']

#To delete range of values
print(list1)
del list1[5:7]
print(list1)   #output: ['Bhragavarama', 'sindu', 'viswaroop', 'sravya', 'chocky']


'''
Pop()
===============
* Pop is pretty much same as Del methods, but the only difference is Pop method returns the deleted value
* syntax is : listname.pop(index)
'''
abc = list1.pop(-1)
print(abc)          #output:chocky
print(list1)        #output:['Bhragavarama', 'sindu', 'viswaroop', 'sravya']

'''
Clear()
===============
* Clear method clears all the elements in the list
* Syntax is listname.clear()
'''

list1.clear()

print(list1)       #output:[]

list1=['Bhragavarama', 'sindu', 'viswaroop', 'sravya', 'chocky', 'baby1', 'baby2', 'maxi']

#to Find Length of a list

print(len(list1))    #output: 8

#To find the count of occurances of a value in list

print(list1.count('maxi'))    #output:1

# To reverse the values in a list

print(list1)            #['Bhragavarama', 'sindu', 'viswaroop', 'sravya', 'chocky', 'baby1', 'baby2', 'maxi']
print(list1[::-1])      #['maxi', 'baby2', 'baby1', 'chocky', 'sravya', 'viswaroop', 'sindu', 'Bhragavarama']
#print(list(list1.reverse()))
print(list1)

'''
======================================================================================================
Tuples
========
* Tuples behaves in the same way as List but these are immutable(Values cant be changed)
* Tuples are created using round brackets with values separated by commas
* All mixed data types are allowed
* Insert, Append doesnt work with Tuples
* Only extend functionality is available in Tuples using '+' operator  
* Remove(), Pop(), del() doesnt work with tuples
* In order to make any changes to a tuple, we need to convert it to List first and make appropriate changes
======================================================================================================
'''
Tuple=(10,'abc')

print(Tuple)        #output:(10, 'abc')

Tuple1= Tuple +(1,2)
print(Tuple1)       #output:(10, 'abc', 1, 2)

#convert tuple to list

tuple_to_list= list(Tuple1)
print(tuple_to_list)  #output:[10, 'abc', 1, 2]

#convert list to tuple

list_to_tuple=tuple(tuple_to_list)
print(list_to_tuple)   #output:(10, 'abc', 1, 2)

'''
========================================================================================================
Sets
=====

-In python, set is a collection of unique elements, even if given duplicates at the time of creation will result in unique values
--Unlike List and Tuples which allows Duplicate values, Sets only allow unique values
--Set is created by separating values with comma and enclosed by flower brackets({})
--Set offers 2 variants(set and Frozenset), Set acts like List (mutable) , where as Frozenset acts like Tuple(Immutable)
--Apart from adding an element and removing an element, set also helps with other operations like union(), Intersection(), difference() etc..
--List as a value in a set is not allowed
========================================================================================================
'''

set={1,1,2,2,3}

print(set)    #output:{1, 2, 3}

#Add items to a set (Add function)
#Add function allows us to add only one element to the set
set.add(10)
print(set)   #output:{10, 1, 2, 3}

#Add Multiple items to a set

set.update([20,10,30])
print(set)   #output:{1, 2, 3, 10, 20, 30}

#Remove Items from a set--using Remove

set.remove(10)
print(set)    #output:{1, 2, 3, 20, 30}

#Remove Items from a set--using Discard()
set.discard(20)
print(set)     #output:{1, 2, 3, 30}

#Main difference between remove and Discard() is : If ane element to be removed doesnt exist in remove function it throws an error,
#where as discard ignores the error and prints the existing set as is.

set.discard(100)
print(set) #output:{1, 2, 3, 30}
#set.remove(100)---error
#print(set)

#clear contents of set--clear
set.clear()

print(set)    #output set()

'''
Set Operations
=========================================================
-union
-intersection
-difference
-symmetric_difference


Union
==================
'''
A={1,2,3,4,5}
B={3,5,6,7,8}
c={3,5,6}

A.union(B)

print(A.union(B))   #output:{1, 2, 3, 4, 5, 6, 7, 8}

print(A.union(B, c))  #output:{1, 2, 3, 4, 5, 6, 7, 8}--Eliminates all duplicates


'''
Intersection
=====================
'''

print(A.intersection(B))     #output: {3, 5}--ony matching values from both sets

'''
Difference
=====================
'''

print(A.difference(B))     #output:{1, 2, 4} ---brings only values that exist in set A


'''
Symmentric Difference
========================
'''

print(A.symmetric_difference(B))   #output:{1, 2, 4, 6, 7, 8}

'''
isSubset, isSuperset, isDisjoint

isSuperset--B.issuperset(A): Set B is said to be superset of B, when all elements of A exist in B, It returns True else False
isSubset--B.issubset(A): Set B is said to be subset of A, when all elements of B exist in A, It returns True else False
isDisjoint--B.isdisjoint(A): Two sets are said to be disjoint when there are no common elements
'''

print(B.issubset(A)) #output:False

print(A.issubset(B)) #output:False

print(A.issuperset(B)) #output:False

print(A.isdisjoint(c)) # output:False


'''
================================================================================================================
Dictionary
=================================================================================================================
* Dictionary is a mutable data type in Python
* Dictionaries in python are collection of key and value pairs separated by a colon(:) & enclosed in flower brackets {}
* Duplicate values are not allowed in Dictionary

'''

#create dictionary

dictionary=dict()  #empty dictionary

dictionary={1:'one',2:'two',3:'three'}

print(dictionary)    #output: {1: 'one', 2: 'two', 3: 'three'}

#to return only keys of a dictionary--keys

print(dictionary.keys())  #output: dict_keys([1, 2, 3])

#to return only values of a dictionary--values

print(dictionary.values())   #output:dict_values(['one', 'two', 'three'])


