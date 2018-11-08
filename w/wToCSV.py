# Potentially useful if we encounter large files.
#Not sure if we will need other info
with open('users.txt', 'r') as users:
    with open('w.csv', 'w') as w:
        for line in users:
            w.write(','.join(line.split()) + '\n')

