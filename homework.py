#Exercise 1
#Given a list as a parameter,write a function that returns a list of numbers that are less than ten

num_list = [1,11,14,5,8,9]

def less_than_ten(a_list):
    new_list = []
    for number in a_list:
        if number < 10:
            new_list.append(number)
            
    return new_list

print(less_than_ten(num_list))

#List Comp

def less_than_ten2(a_list):
    return [number for number in a_list if number < 10 ]

print(less_than_ten2(num_list))

#Excercise 2
#Write a function that takes in two lists and returns the two lists merged together and sorted

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge_lists(a, b):
    for number in b:
        a.append(number)
    return sorted(a)

print(merge_lists(l_1, l_2))

#A much better way
l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]


def merge_lists(a, b):
    return sorted(a + b)

print(merge_lists(l_1, l_2))

#Can't really use list comp on this.....too simple