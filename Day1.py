#Task1==================================================

res = 0
file1 = open("FileForInt_1t.txt", "r")
for i in file1:
    for j in i.split():
        if j.isdigit():
           res += int(j)
print(res)
file1.close()

#Task2==================================================


with open("FileForStr_2t.txt", "r") as file2:
    with open("FileForStr2_2t.txt", "w") as file3:
        var = file2.read()
        var = var.title()
        file3.write(var)

#Task3==================================================


lst = [2, 4, 6, 22, 4, 4, 9, 2, 6, 2]
dict = {}
for i in lst:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)

#Task4=================================================


with open("FileForStr_2t.txt", "r") as file1:
    var = file1.read()
    print(len(var))
    
#Task5=================================================


name = "YuraYeghiazaryan"
'''def del3(str):
    i = 0
    z = 2
    new = ""
    while i <= len(str):
      new += str[i:z]
      i = z+1
      z += 3
    return new
print(del3(name))'''


def ud3(str):
    str = list(str)
    del str[2::3]
    str = "".join(str)
    return str


print(ud3(name))


#Task6=================================================

qanak = open("FileNames_6.txt", "r")

def count(file):
    dict = {}
    for i in file:
        for j in i.split():
            if j in dict:
                dict[j] += 1
            else:
                dict[j] = 1
    return dict.items()

print(count(qanak))
qanak.close()



#Task7=================================================

lst1 = [4, 2, 7, 1]
lst2 = []
for i in lst1:
    lst2.append(i**2)
lst2 = sorted(lst2)
print(lst2)


#Task8=================================================

var = 1279137
res = 0
while var >= 1:
    res += var % 10
    var = var / 10
print(res)



#Task9=================================================

tiv = 1234
add = 0
mult = 1
while tiv >= 1:
    add += tiv % 10
    mult *= tiv % 10
    tiv = tiv / 10
print(mult - add)


#Task10=================================================

def kent(l, r):
    if l > r:
        return "range error"
    elif l == r:
        if l % 2 != 0:
            return l
        else:
            return "no elements"
    if l % 2 != 0:
        return range(l, r + 1, 2)
    else:
        return range(l + 1, r + 1, 2)


print(kent(5, 2))
