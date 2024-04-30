from typing import List, Dict

def ListComprehension(var: int) -> List[int]:
    my_list = [i for i in range(var) if i%2 == 0]
    return my_list


def DictComprehension(my_list:List[int]) -> Dict[str, int]:
    my_dict = {str(itr):itr for itr in my_list}
    return my_dict 


def main():
    my_list = ListComprehension(55)
    my_dict = DictComprehension(my_list)
    print(my_dict)


if __name__ == "__main__":
    main()