def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        # Important midpoint
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


someList = [1, 3, 4, 5, 10, 23, 39, 40]
print(binarySearch(someList, 23))
print(binarySearch(someList, 11))


def binarySearchRecursion(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearchRecursion(alist[:midpoint], item)
            else:
                return binarySearchRecursion(alist[midpoint+1:], item)

print(binarySearchRecursion(someList, 23))
print(binarySearchRecursion(someList, 11))