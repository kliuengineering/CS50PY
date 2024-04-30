


def Generator(n: int) -> any:
    for i in range(n):
        yield "⭐" * i


def Print(n: int) -> None:
    for s in Generator(n):
        print("⭐")


def main():
    n = int(input("how many sheeps to generate? "))
    Print(n)


if __name__ == "__main__":
    main()