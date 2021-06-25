def largestVal(arr):
    val = set()
    ar = []
    for i in arr:
        if abs(i) in val:
            ar.append(abs(i))
        else:
            val.add(abs(i))
    ar.sort()
    return max(ar)
if __name__ == "__main__":
    arr = [-3, -2, 1, 2, 3, 5]
    print(largestVal(arr))

