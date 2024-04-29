import re
import sys


# input -> str IPv4
# output -> bool

def validate(ip):
    flag = False

    # [0-2]{1}[0-5]{1}[0-5]{1}\.[0-2]{1}[0-5]{1}[0-5]{1}\.[0-2]{1}[0-5]{1}[0-5]{1}\.[0-2]{1}[0-5]{1}[0-5]{1}
    if re.match(
        r"""
        ^
        ((0[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])|[0-9])\.
        (([0-9][0-9][0-9])|([0-9]))\.
        (([0-9][0-9][0-9])|([0-9]))\.
        (([0-9][0-9][0-9])|([0-9]))
        $
       """, ip, flags=re.VERBOSE):
        flag = True

    return flag


def main():
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()
