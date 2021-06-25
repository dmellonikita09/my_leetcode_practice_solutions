def mergeArray(arr1, arr2):
        
        if n == 0:
            return arr1
        else:
            #del arr1[-n:]
            arr1.extend(arr2)
            arr1.sort()
        return arr1
    
arr1 = [2, 4, 6, 8]
arr2 = [3, 5, 7, 9]
m = len(arr1)
n = len(arr2)
print(mergeArray(arr1,arr2))

