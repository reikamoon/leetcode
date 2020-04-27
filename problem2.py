#Given two arrays, write a function to compute their intersection

#Variable: Value
#array1 = [1,2,3,4]
#array2 = [3,6,7,8]
#num = 3

def intersection(arr1, arr2):
    my_set = {}
    for i in arr1:
        if i in my_set:
            my_set[i] += 1
        else:
            my_set[i] = 1
    new_set = []
    for i in arr2:
        if i in my_set and my_set[i]:
            my_set[i] -= 1
            new_set.append(i)
    return new_set

arr1 = [1,2,3,4]
arr2 = [3,6,7,8]
print(intersection(arr1, arr2))
