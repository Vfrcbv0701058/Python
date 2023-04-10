user_data = int(input("Enter num:"))

isHappy = True

if isHappy: 
    print()

if isHappy and user_data > 5:
    print ("Number is bigger than 5")
elif user_data < 5:
    print ("Number is smaller than 5")
    if user_data == 0:
        print ("Number is zero")
else:
    print ("Number is equal to 5")

# Длинная запись
data = input()
if data == "Five":
    number = 5
else:
    number = 0
print(number)

# Короткая запись 
number = 5 if data == "Five" else 0
# number будет равна 5 если переменная data = строке Five если нет то number = 0
print (number)