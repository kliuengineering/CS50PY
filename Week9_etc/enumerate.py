from typing import List


# enumerates over all of the elements and adding an index before them
def Enumerate(my_list: List[int]) -> None:
    my_dict = {i:itr for i, itr in enumerate(my_list)}
    print(my_dict)
    
    key_types = set()
    value_types = set()
    for key, value in my_dict.items():
        key_types.add(type(key))
        value_types.add(type(value))
    print("Unique types of keys:", key_types)
    print("Unique types of values:", value_types)


def main():
    my_list = [i for i in range(55) if i%2 == 0]
    Enumerate(my_list)


if __name__ == "__main__":
    main()