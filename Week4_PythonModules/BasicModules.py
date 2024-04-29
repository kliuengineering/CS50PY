import sys          # int argc, char *argv[] equivalence
import random
import statistics


def PrintSimpleRandomSample(seq):
    print( "my random choice is -> ", random.choice(seq) )


def PrintShuffle(seq):
    random.shuffle(seq)
    print("printing a shuffled set of seq")
    for itr in seq:
        print(itr)


def main():
    argv = sys.argv

    if len(argv) < 3:
        sys.exit("Too few arguments... You need exactly 2... ")
    if len(argv) > 3:
        sys.exit("Too many arguments... You need exactly 2...")

    print(argv)


main()
