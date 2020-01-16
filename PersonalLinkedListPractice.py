# references:
# library: https://pythonhosted.org/pyllist/
# https://github.com/rgsoda/pypy-llist
# https://pythonhosted.org/llist/

from pyllist import dllist, dllistnode

        #node = mylist.first
        #nextNode = node.iternext
        #nodePrevious = node.iterprev
        #nodeValue = node.value



mylist = dllist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
myotherlist=dllist([3, 7, 8])
myNextOtherList = dllist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
myNextOtherList2 = dllist([1, 2, 3, 4, 5, 6, 7, 8, 9, 101, 2, 3, 4, 5, 6, 7, 8, 9, 10, 80, 60, 9])

print('Printing the original list:')
print(mylist)
print('\n')

print('Printing mylist.first, mylist.first.iternext, and mylist.first.iterprev:')
print(mylist.first)
print(mylist.first.iternext)
print(mylist.first.iterprev)
print('\n')

#Comparing the lists
print('Comparing the lists:')
print(mylist.__cmp__(myotherlist))
print(mylist.__cmp__(myNextOtherList))
print(mylist.__cmp__(myNextOtherList2))

print('\n')
# reference: https://pythonhosted.org/llist/
mylist.append(8000)
print(mylist)

mylist.appendleft(300)
print(mylist)
print(mylist.appendright(510))
print(mylist)
print('\n')

# reference: https://docs.python.org/2/tutorial/datastructures.html

print('Attempting to search for a number:')


def _searchingForNum_(mylist, lookingForListNum):  # is O(n), a linear function for the search

# because must look at all items on list

    for i in mylist:
        if i == lookingForListNum:
            while True:
                try:
                    print('It matches')
                except ValueError:
                    print("This didn't work")
                else:
                    break
        if i != lookingForListNum:
            while True:
                try:
                    i + 1
                    print("doesn't match")
                except ValueError:
                    print('Error was made')
                else:
                    break

_searchingForNum_(mylist, lookingForListNum=5)
_searchingForNum_(mylist, lookingForListNum=8000)

print('\n')

print('Attempting to remove a number from the list:')

def _inserting_(mylist, lookingForListNum, x):
    print("Mylist:")
    print(mylist)
    for i in mylist:
        if i == lookingForListNum:
            while True:
                try:
                    print('Searched for:')
                    print(lookingForListNum)
                    print('It matches')
                    newNum = mylist.nodeat(lookingForListNum)
                    newNum = x
                except ValueError:
                    print("This didn't work")
                else:
                    break
    print(mylist)


print('\n')
print(_inserting_(mylist, lookingForListNum=9, x=9000))



















