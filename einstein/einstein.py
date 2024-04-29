def Convert( kg ):
    return (kg * 300000000 ** 2)

def main():
    var = int( input("m: ") )
    print( f"E: {Convert(var)}" )

main()
