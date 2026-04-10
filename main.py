#1-misol
words = ["Hello", "World"]
result = " ".join(words)
print(result)

#2-misol
items = ["apple", "banana", "cherry"]
result = ", ".join(items)
print(result)
#
#3-misol
chars = ["P", "Y", "T", "H", "O", "N"]
result = "".join(chars)
print(result)

#4-misol
numbers = [1,2,3,4]
result = ", ".join(map(str, numbers))
print(result)

#5-misol
words = ["I", "Love", "Python"]
result = " ".join(words)
print(result)

#6-m
folders = ["home", "user", "documents"]
path = "/".join(folders)
print(path)

#7-m
words = ["Python", "", "Django", "None", "Api"]
result = " ".join([w for w in words if w])
print(result)
