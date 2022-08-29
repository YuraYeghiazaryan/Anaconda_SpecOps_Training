#Task1=======================================

target = [1, 3]
n = 3
stack = []
relst = []
for i in range(1, n+1):
    stack.append(i)
    relst.append("push")
    if i not in target:
        stack.pop()
        relst.append("pop")
    if stack[-1] == target[-1]:
        break

print(relst)


#Task2=======================================

nums1 = [2, 5, 3, 3, 3]
nums2 = [4, 2, 6, 3]


def unique(lst1, lst2):
    u_lst = []
    for i in nums1:
        if i in nums2 and i not in u_lst:
            u_lst.append(i)
    return u_lst


print(unique(nums1, nums2))


#Task3=======================================

nums = [1, 2, 4, 1, 2]


def frequency_element(lst):
    dict = {}
    for i in lst:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    for j in dict:
       if dict[j] == max(dict.values()):
        el = j
    first = lst.index(el)
    last = len(lst) - 1 - lst[::-1].index(el)
    return len(lst[first:last])


print(frequency_element(nums))


#Task4=======================================

nums = [3, 4, 6, 1, 2, 7]
any_nums = [0] * len(nums)
l = 0
r = len(nums)-1
for i in nums:
    if i % 2 == 0:
        any_nums[l] = i
        l += 1
    else:
        any_nums[r] = i
        r -= 1
print(any_nums)



#Task5=======================================

nums = [1, 2, 55, 1, 2]
sum = 0

for i in nums:
    if nums.count(i) == 1:
        sum += i
print(sum)


#Task6=======================================

needle = "hello"
haystack = "ll"


def strStr(str1, str2):
    if haystack in needle:
        for i in needle:
            if haystack[0] == i:
                return needle.index(i)

    else:
        return -1


print(strStr(needle, haystack))


#Task7=======================================

def len_last_word(str):
    return len((str.split())[-1])

print(len_last_word("hsbdch jdsb jjjkk"))



#Task8=======================================

def palindrome(str):
    str = str.replace(" ", "")
    str = str.lower()
    if str == str[::-1]:
        return "Yes"
    else:
        return "No"

print(palindrome("a sA dg Gda Sa"))


#Task9=======================================

email = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]


def unique_email(lst):
  for i in range(len(lst)):
     plus = lst[i].index("+")
     dog = lst[i].index("@")
     lst[i] = lst[i][:plus].replace(".", "") + lst[i][dog:]
  return len(set(lst))


print(unique_email(email))


#Task10======================================

nums = [1, 3, 5, 5, 5, 7, 9]


def start_end(lst, target):
    left = binSearch(lst, target, True)
    right = binSearch(lst, target, False)
    return [left, right]


def binSearch(lst, target, leftBias):
    l, r = 0, len(lst) - 1
    i = -1
    while l <= r:
        m = (l + r) // 2
        if target > lst[m]:
            l = m + 1
        elif target < lst[m]:
            r = m - 1
        else:
            i = m
            if leftBias:
                r = m - 1
            else:
                l = m + 1
    return i


print(start_end(nums, 5))


