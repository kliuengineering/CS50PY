def Interpreter(x, y, z):
    rc = None
    if y == "+":
        rc = x + z
    elif y == "-":
        rc = x - z
    elif y == "*":
        rc = x * z
    elif y == "/":
        rc = x / z
    return rc

def Parser(var):
    x, y, z = var.strip().split(" ")
    x = float(x)
    z = float(z)
    rc = Interpreter(x, y, z)
    return rc

def main():
    expression = input("Expression: ")
    print( round( Parser(expression), 2 ) )

main()
