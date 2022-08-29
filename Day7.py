#Task1=======================================

nums = [10, 3, 5, 9,11]


def bubleSort(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                print(lst)
    return lst


print(bubleSort((nums)))



#Task2=======================================

nums = [23, 34, 1, 5, 66, 35]

def selectionSort(lst):
    n = len(lst)
    for i in range(n-1):
        min = i
        for j in range(i + 1, n):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    return lst


print(selectionSort(nums))


#Task3=======================================

nums = [23, 34, 1, 5, 66, 35]

def insertionSort(lst):
    for i in range(1, len(lst)):
        while lst[i - 1] > lst[i] and i > 0:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return(lst)


print(insertionSort(nums))



#Task4=======================================

nums = [2, 4, 6, 1, 8, 5, 3, 9]


def sort(data1, data2):
    result = []
    i, j = 0, 0
    while i < len(data1) and j < len(data2):
        if data1[i] < data2[j]:
            result.append(data1[i])
            i += 1
        else:
            result.append(data2[j])
            j += 1

    while j < len(data2):
        result.append(data2[j])
        j += 1
    while i < len(data1):
        result.append(data1[i])
        i += 1
    return result


def devide(data):
    if len(data) < 2:
        return data
    else:
        middle = len(data) // 2
        data1 = devide(data[:middle])
        data2 = devide(data[middle:])
    return sort(data1, data2)


print(devide(nums))

