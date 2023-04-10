num = int(input("Ведите текст "))

if num > 0:
    print("Hello\n")
elif num < 0:
    print("< 0")
else:
    print("num = 0")
    print("Hello 1")

# Смена значения переменнй с помощью условного оператора
name = input()
A = 'Yes' if name != "test" else 'No'
print(A)
