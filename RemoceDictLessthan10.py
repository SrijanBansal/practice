d = {'a':2,'b':3,'c':4,'d':10,'e':20,'f':30}

result = {k:v for k,v in d.items() if v >= 10}
print(result)
