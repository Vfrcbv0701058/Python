# country = {'code': 'UA', 'name': 'Ukraine', 'population': 144}
# более сложная форма создания словаря
country = dict(code = 'UA', name = 'Ukraine', population = 144)
# print(country['code'] + '\n' + country['name'] + '\n' + str(country ['population']))
for key,value in country.items():
    print (key, "-", value)
country.update({'code': 'UA UA'}) 
country['name'] = 'UKRAINE'
print(country)
country.clear()

grades_user_1 = {
    'math': 5,
    'physics': 5
}

user_1 = {
    'first_name': 'John', 
    'second_name': 'Morley',
    'age': '45',
    'adress': ('City: London', 'Baker Street', 'flat: 45'),
    'grades': grades_user_1
}

person = {
    'user_1': user_1
}

print(person['user_1']['adress'][1])