#Task2=========================================

def strmove(word, step):
    word = word[-step:] + word[:-step]
    return word

print(strmove("yeghiazaryan",


#Task3=========================================

def gum(tiv):
    f = 5
    t = 3
    st = set()

    while t < tiv:
      if f < tiv:
        st.add(f)
        st.add(t)
      else:
        st.add(t)
      f += 5
      t += 3
    return sum(st)
print(gum(1000))


#Task4=========================================
              
              sumik = 0
n1 = 1
n2 = 2
while n1 < 4 * 10 ** 6:
    if n1 % 2 == 0:
        sumik += n1
    n1, n2 = n2, n1 + n2
print(sumik)
