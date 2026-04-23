from itertools import *
n = 0
for x in product("АНДРЕЙ",repeat = 6):
    s = "".join(x)
    if s[0] != "Й"  and s[5] != "Й" and s.count("Й") == 1 and s.count("ЕЙ") == 0 and s.count("ЙЕ") == 0:
        n+=1
        print(n,s)