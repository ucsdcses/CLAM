# Outputs the number of unique names dependent on who is on
with open('users.txt') as whoAmI:
    name = who.read().split()
processUsers = []
for i in range(0, len(name), 5):
    processUsers.append(name[i])
print(len(set(processUsers)))
    
