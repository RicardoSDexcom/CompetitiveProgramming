
# Example usage:
a = [1, 2, 2, 4]
b = [1,2,2,5]

c = []
for i in a:
    if i in b:
        c.append(i)
        
print(c)
