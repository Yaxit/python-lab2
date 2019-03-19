from sys import argv

if len(argv) < 2:
    print("Too little arguments")
    exit(-1)

file = open(argv[1], "r")
activities = [line.rstrip() for line in file]
file.close()
cmd = "5"
while not cmd == "4":
    print("1 - Insert\n2 - Remove\n3 - View\n4 - Quit\n")
    cmd = input("Cosa vuoi fare?\t")
    if cmd == "1":
        line = input("Insert title\t")
        activities.append(line)
    elif cmd == "2":
        num = input("Testo da cercare?\t")
        for activity in activities:
            if num in activity:
                activities.remove(activity)
    elif cmd == "3":
        sort = sorted(activities)
        for i, j in enumerate(sort):
            print(i, j)
    elif cmd == "4":
        file = open(argv[1], "w")
        for line in activities:
            file.write(line + "\n")
        file.close()
        break
