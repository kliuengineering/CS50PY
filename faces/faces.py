def convert( var ):
    if ":)" in var:
        # print("im :)")
        var = var.replace( ":)", "🙂" )

    if ":(" in var:
        # print("im :(")
        var = var.replace( ":(", "🙁" )

    return var

def main():
    my_string = input()
    print( convert(my_string), end = "" )

main()
