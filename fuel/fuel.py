def Calculate(X, Y):
    return float(X) / float(Y)


def Percentage(Z):
    return int( round(Z, 2) * 100 )


def Print(Z):
    if Z <= 1:
        print("E")
    elif Z >= 99:
        print("F")
    else:
        print(f"{Z}%")


def Input(prompt):
    is_running =  True
    
    while is_running:
        try:
            X, Y = input(prompt).strip().split("/")

            if int(X)>int(Y):
                continue

            Z = Calculate( int(X) , int(Y) )
            Z = Percentage(Z)
            Print(Z)
            is_running = False

        except ValueError:
            pass

        except ZeroDivisionError:
            pass


def main():
    prompt = "Fraction: "
    Input(prompt)


main()
