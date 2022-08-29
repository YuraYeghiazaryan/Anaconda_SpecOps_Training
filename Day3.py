#Task3======================================

res = 0
res2 = 0
for i in range(1,101):
    res += i
    res2 += i ** 2
print(res ** 2 - res2)


#Task4======================================

import urllib.request
data = urllib.request.urlopen("https://projecteuler.net/project/resources/p022_names.txt")
text = data.read()
text = text.title()
with open("file4.txt", "wb") as upper:
    upper.write(text)

print(upper)


#Task5======================================

def pdrom(n):
    if n < 0 or n % 10 == 0:
        return "No"
    else:
        n = str(n)
        if n == n[::-1]:
            return "Yes"
        else:
            return "NO"


print(pdrom(131))
print(pdrom(132))
print(pdrom(130))
print(pdrom(-131))
