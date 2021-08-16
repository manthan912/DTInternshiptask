import random
#binary search
def binarysearch( arr, l, r, x ):
    if r >= l:
        mid = l + ( r - l ) //2
        if arr[ mid ] == x:
            return True
        elif arr[mid] > x:
            return binarysearch( arr, l, mid-1, x )
        else:
            return binarysearch(arr, mid + 1, r, x)
    else:
        return False



# driver code
# list with random elements between 0 & 100 wth
randomList = random.sample(range(0, 100), 20)  # no of elements in list = 20
randomList.sort()
# getting user input
print(" Welcome, Enter a number")
i = int(input())
result = binarysearch( randomList, 0, len(randomList)-1, i )
if result:
    print("Given number is present")
else:
    print("Number not found")
