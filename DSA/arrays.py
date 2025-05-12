myArray = [4,5, 6, 7]

length = len(myArray)
# print(myArray[0]) # 1

#Regardless of the size of the array, the time required to access an element is constant.
# This is called constant time complexity, or O(1) time complexity.

# Traversing an array

# for i in range(len(myArray)):
#     print (myArray[i])   

# To Traverse through a array of size n, the time complexity is O(n)

# Deleting from an array 

# Deleting the last element 

def removeEnd(arr, length):
    if length > 0:
        arr[length -1] = 0

# Deleting the ith Element 

def removeMiddle(arr, length, i):
    # [4 ,5 6, 7]
    return arr[:i] + arr[i+1:]


modifiedArray = removeMiddle(myArray,length,2)
print(modifiedArray)

# Inserting array at the last 

def insertEnd(arr, value):

    return arr + [value]

insertedArray = print(insertEnd(myArray, 10))


myArray = [4,5, 6, 7,10] 
def insertMiddle(arr, value, i):
    return arr[:i] + [value] + arr[i:]

insertMiddleArray = print(insertMiddle(myArray, 15, 3))

# Reading - O(1)
# Deleting - O(n)
# Inserting - O(n)
