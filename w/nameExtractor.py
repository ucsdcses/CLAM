#Outputs the number of unique names dependent on who is on
# **** Issues: for some reason, users.txt picks up ./run.sh 
with open('users.txt') as w:
    name = w.read().split()
users = []
INTERVAL = 6
name = name[INTERVAL:]
for i in range(0, len(name), INTERVAL):
    # gets rid of the heading
    users.append(name[i])
print(len(set(users)))
#print(users)
