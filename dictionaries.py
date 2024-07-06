dic = {
    "title" : "Deyal",
    "author" : "Humayun Ahmed",
    "year" : "2013"
}
print(dic)
print(dic.get("title"))
print(dic.get("author"))
print(dic.get("year"))

dic["genra"] = "Novel" #Add new key value
print(dic.get("genra"))

print(len(dic)) #Length of the dictionary
print(type(dic)) #Type of the dictionary

for i in dic.items():
    print(i)

for i in dic.keys():
    print(i)