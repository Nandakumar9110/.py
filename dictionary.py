d={1:"python",'python':123,324:"nanda"}
print(d)
print(type(d))
print(d.values())
print(d.keys())
print(d.items())
d.update({111:"kumar"})
print(d)
print(d.get(111))
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i,j in d.items():
    print(i,j)