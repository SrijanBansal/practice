d = {'c':30,'b':3,'a':4,'d':10,'e':20,'f':30}

result = [k for k,v in d.items() if d[k] == max(d.values())]

print(result)
