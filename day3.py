s1 = "string"
s2 = "Fridge"
s = "".join([s1[i] + s2[i] for i in range(len(s1))]) + s2[len(s1):]
print(s)
