data = (4, 6, 7, 3, 6, True, 5.6, "Hello")
print(data[1:5])
# data[0] = 5 - no
print(data.count(6))
print(len(data))

data_1 = 1, 4, 6, 2, 3.6, True # это тоже кортеж
print(data_1)
data_2 = (5) # это не кортеж
data_2 = (5,) #это кортеж
print(data_2)

for el in data:
    print(el)

nums = [5, 6, 2]
new_data = tuple(nums)
print(new_data)