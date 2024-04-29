def Search(input_string):
    result = []

    for i in range(len(input_string)):
        if input_string[i] == "a" or input_string[i] == "e" or input_string[i] == "i" or input_string[i] == "o" or input_string[i] == "u":
            result.append(i)
        if input_string[i] == "A" or input_string[i] == "E" or input_string[i] == "I" or input_string[i] == "O" or input_string[i] == "U":
            result.append(i)

    input_array = [*input_string]
    # print(input_array)

    counter = 0
    if len(result):
        for itr in result:
            # print(itr)
            input_array.pop(itr - counter)
            # print(input_array)
            counter += 1
    input_array = "".join(input_array)

    return input_array


def main():
    word = input("Input: ")
    print(f"Output: {Search(word)}")

main()
