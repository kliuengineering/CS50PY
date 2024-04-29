def CheckInput( var ):
    flag = False
    var = var.strip().lower()
    if var == "42" or var == "forty-two" or var == "forty two":
        flag = True
    return flag

def main():
    var = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if CheckInput(var):
        print("Yes")
    else:
        print("No")

main()
