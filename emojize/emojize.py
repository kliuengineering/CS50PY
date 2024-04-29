import emoji
import sys


def Emoji(var):
    print( emoji.emojize(f"Output: {var}", language="alias") )


def main():
    Emoji( input() )

main()
