def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)

arr = [-2, 3, 4, 7, 8, 9, 11, 13]
target = 11
print(binary_search_recursive(arr, target, 0, len(arr)))

var myArray = ['a', 'b', 'c', 'd'];
myArray.push("end")
myArray.unshift("start")

console.log(myArray)