import sys
import random
from pyfiglet import Figlet


def Check(argv):

    flag = False

    if len(argv) == 1 or len(argv) == 3:
        flag = True
    else:
        return flag

    try:
        if argv[1] == "-f" or argv[1] == "--f":
            flag = True
        else:
            flag = False
            return flag

    except:
        flag = False

    print(flag)
    return flag


def main():

    argv = sys.argv
    if Check(argv) == False:
        sys.exit("Invalid usage")

    figlet = Figlet()
    figlet.setFont(font=argv[2])
    print( "Output: ", figlet.renderText( input("Input: ") ) )


if __name__ == "__main__":
    main()
