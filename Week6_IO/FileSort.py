import random

with open("second.txt", "w") as file:
    for i in range(10):
        file.write(f"hello {random.randint(1, 100)}\n")

with open("second.txt") as file:
    data = []
    for itr in file:
        data.append(itr.rstrip())
    print(sorted(data))
