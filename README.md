# w3d2hw
Week 2 Day 2 HW

## Exercise 1
Given a list as a parameter,write a function that returns a list of numbers that are less than ten

defined the less_than_ten function which recieves a_list.       
Within the function an empty list is defined named new_list.   
We then enter a for loop which iterates through every number in a_list.  
if number less < 10, the number is appended to the empty list.   
After iterating through the entirety of a_list, the function returns new_list which.

#### List Comp Version

Defined less_than_ten2 which again accepts a_list.   
we then return an appended list of numbers from a_list if the number < 10

`return [number for number in a_list if number < 10 ]`

## Exercise 2
Write a function that takes in two lists and returns the two lists merged together and sorted

#### Dumb Way
Defined the merge_lists function which recieves two lists a and b.
Use a for loop to iterates through every number in b.   
Within the loop the numbers are appended to a.   
we then return sorted(a), sorted() puts the numbers in numerical order as the question asks.

#### Smart way

define function merge_lists which accepts two lists a and b.   
return sorted(a + b).   
+ adds the contents of list b to list a without the iterating and appending....
