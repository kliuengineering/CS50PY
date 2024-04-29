import re
import sys


def main():
    print(convert(input("Hours: ")))


# input -> 12 hour format
# output -> 24 hour format
# AM/PM are expected to be caplitalized
# raise ValueError -> not one of the following formats
#   9:00 AM to 5:00 PM
#   9 AM to 5 PM
def convert(s):
    try:
        s_validated = Validate(s)
        s_parsed = Parse(s_validated)
        s_converted = Convert(s_parsed)
    except:
        raise ValueError

    return s_converted


# 2 - responsible for parsing the input string
def Parse(string):
    rc = None

    if string != None:
        pattern = r"""
                        ^
                        (.+)\s(AM|PM)\sto\s(.+)\s(AM|PM)
                        $
                """
        matches = re.search(pattern, string, flags=re.VERBOSE)
        if matches:
            start_time, start_part, finish_time, finish_part = matches.group(1), matches.group(2), matches.group(3), matches.group(4)
            rc = [start_time, start_part, finish_time, finish_part]
            # print(rc)

    return rc


# 1 - responsible for validating the input
def Validate(string):
    rc = None
    # string = string.strip()
    pattern = r"""
                    ^
                    (1?[0-2]|[0-9])(:[0-5][0-9])?\s(AM|PM)\sto\s(1?[0-2]|[0-9])(:[0-5][0-9])?\s(AM|PM)
                    $
               """
    if re.match(pattern, string, flags=re.VERBOSE):
        rc = string
        # print(rc)

    return rc


# 3 - responsible for converting 12-h to 24-h
def Convert(array):
    rc = None

    if len(array) > 0:
        try:
            start_hour, start_minute = array[0].split(":")
            start_hour, start_minute = int(start_hour), start_minute
        except:
            start_hour = int(array[0])
            start_minute = "00"
        start_part = array[1]

        try:
            finish_hour, finish_minute = array[2].split(":")
            finish_hour, finish_minute = int(finish_hour), finish_minute
        except:
            finish_hour = int(array[2])
            finish_minute = "00"
        finish_part = array[3]

        start = CheckTime(start_hour, start_minute, start_part)
        finish = CheckTime(finish_hour, finish_minute, finish_part)

        rc = start + " to " + finish

    return rc


# 4 - utility function for #3
def CheckTime(hour, minute, part):
    rc = None

    # print(hour, minute, part)

    if part == "AM":
        if hour == 12:
            hour = 0
        hour = "0" + str(hour)
        minute = minute
        rc = hour + ":" + minute
    elif part == "PM":
        hour = str( hour + 12 )
        if hour == "24":
            hour = "12"
        minute = minute
        rc = hour + ":" + minute

    return rc


if __name__ == "__main__":
    main()
