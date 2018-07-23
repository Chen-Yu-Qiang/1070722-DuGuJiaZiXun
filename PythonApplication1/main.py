def jie(a):
    if a==1:
        return 1
    else:
        return a*jie(a-1)

print(jie(10))