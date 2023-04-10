print ("Результат: ", 5, 15,".", sep=" ", end = "!\n")
print ("Second line")
print("some \t\"thing\"")
print (8%3)
list = [4,7,342432,7,4,2,8,0,-3,7653,23,3,4]
print(min(list))
print(max(list))
print(abs(min(list))) # выведет значение по модулю минимального числа в списке list
print(pow(max(list), abs(min(list)))) # берет максимальный элемент списка list и возводит его в степень, а степенью являеться модуль минимального значения списка list
print(round(list[0]/list[3]))
input("Ведите данные: ")