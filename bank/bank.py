def Decision(var):
    var = var.strip().lower()
    if var == "hello":
        print("$0")
    elif "hello" in var:
        print("$0")
    elif var[0] == "h":
        print("$20")
    else:
        print("$100")

def main():
    Decision( input("Greeting: ") )

main()
