
# Python program for implementation of Insertion Sort
def insertionSort(arr):
     for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
 
#sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
#empty list to store sorted elements
lst = [] 
print("Sorted array is : ")
for i in range(len(arr)):
    lst.append(arr[i])     #appending the elements in sorted order
print(lst)
 