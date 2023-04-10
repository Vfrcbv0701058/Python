l = [] 
lis = [1,56,'x', 34, 2.34, ['s','t','r','o','k','a']]
print(lis[5][4])

for i in range(len(lis)):
    print(lis[i])

n = int(input("Enter lenght: "))
i = 0
user_list = []
while i < n :
    string = "Enter element #" + str(i + 1) + ": "
    user_list.append(input(string))
    i +=1

print(user_list)


# a = [a+b for a in 'list' if a != 's' for b in 'soup' if b!='u']
# print(a)

# lis.append (23)
# lis.append (34)
# b = [24,67]
# lis.extend (b)
# lis.insert (1, 56)
# lis.append (34)
# lis.remove (34)
# lis.pop (0)
# lis.sort ()
# lis.reverse ()
# lis.clear ()

# print(lis)
# print (lis.index(56))
# print (lis.count(34))