s = "a good   example"
s2=s.split(" ")
s2.reverse()
print(s2)

while "" in s2: s2.remove("")

print(s2)
print(" ".join(s2).strip())


