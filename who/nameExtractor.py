with open('names.txt') as who:
    name = who.read().split()
processUsernames = []
for i in range(0, len(name), 5):
    processUsernames.append(name[i])
print(len(set(processUsernames)))
    
