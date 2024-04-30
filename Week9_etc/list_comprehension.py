from typing import List

def ListComprehension(var: int) -> List[int]:
    my_list = [i for i in range(var) if i%2 == 0]
    return my_list


def main():
    my_list = ListComprehension(55)
    my_dict = {*my_list}
    print(my_dict)


if __name__ == "__main__":
    main()