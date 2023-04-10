word = "football, basketball, skate"
print (len(word)) # возвращает кол-ство элементов в строке word
print (word.count("m")) # возвращает кол-ство m в сроке word
print (word.upper())
print (word.isupper())
hobby = word.split(", ")
print (hobby[1])

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

result = ", ". join(hobby)
print (result)

word = "Football"
print(word[1:-1:2]) 

lis = [6,4,6,"stroka", True, 6.5, False, "nfdiw"]
print (lis [2:7])