name = "mypackage"
num = 99
size = 10.1234

base = "A package named {name} with {num} items of size={size}"
f_string = f"A package named {name} with {num} items of {size=}"
t_string = t"A package named {name} with {num} items of {size=}"

for s in base, f_string, t_string:
    print(type(s))
    print(s)

print(base.format(name=name, num=num, size=size))
print(f_string)
print(t_string.interpolations)
