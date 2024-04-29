with open("names.txt", "a") as file:
    for i in range(10):
        file.write(f"line #{i}\n")


with open("names.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.rstrip())

