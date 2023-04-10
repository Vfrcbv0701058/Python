for i in range (1,6,2):
    print(i)
word = "Hello world!"

count = 0
for i in word:
    if i == "l":
        print("Yes")
        count += 1
print(count)

i = 5
while i <= 15 :
    print("i =", i)
    i += 2
isHasCar = True
while isHasCar: 
    if input("Enter something: ") == "Stop":
        isHasCar = False

for i in range(1,11):
    if i == 4:
        continue
    print(i)
    if i == 9: 
        break

found = None
for i in "Hello":
    if i == "l":
        found = True
        break
    else: 
        found = False
print(found)