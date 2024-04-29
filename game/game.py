import random


target = None
is_running = None


def Evaluate():

    global is_running

    while is_running:

        guess = int( input("Guess: ") )

        if guess > target:
            Print(1)
        elif guess < target:
            Print(-1)
        else:
            Print(0)
            is_running = False


def Print(result):
    if result == -1:
        print("Too small!")
    if result == 1:
        print("Too large!")
    else:
        print("Just right!")



def main():
    global is_running
    global target

    is_running = True
    while is_running:

        try:
            level = int( input("Level: ") )
            if level < 1:
                continue

            target = random.randint(1, level)
            Evaluate()

        except ValueError:
            continue




if __name__ == "__main__":
    main()
