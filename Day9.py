#Task2===============================

import os
import random
with open("file","w") as f:
    while os.stat("file").st_size < 4 * 10 ** 6:
        f.write(f"{random.randint(1, 200


#Task3===============================

dic = {}
with open ("file") as f:
    for i in f:
        dic[i] = dic.get(i, 0) + 1
    for x in sorted(dic):
        f.write(f"{(x + '') * dic[x]}")
