# Requirements:
    # input -> date of birth
    # output -> minutes till today
    # rounding -> nearest int
    # translate int -> English, no "and" connectives
    # OOP
    # error handling -> sys.exit()
        # error defines as -> not ISO format YYYY-MM-DD

# Assumptions:
    # 1) born at midnight
    # 2) today is at midnight, use datetime.date.today

# Expected output:
    # input(2022-04-27), output(One million, fifty-one thousand, two hundred minutes) // 1051200 + 1440


from datetime import date
from datetime import timedelta
import sys
import time
import re
import inflect


MINS_PER_YEAR = 525600
MINS_PER_DAY = 1440
LEAP_YEAR_MARGIN = 1440


def main():
    # Debug()
    dob = input("Date of Birth: ")
    result = Start(dob)
    print(result)


# interface
def Start(dob):
    dob_validated = Validate(dob)
    CheckError(dob_validated)
    # print(dob_validated)

    dob_computed = Calculate(dob_validated)
    # print(dob_computed)

    days_parsed = int( Parse(dob_computed) )
    # print(days_parsed)

    minutes_passed = Transform(days_parsed)
    # print(minutes_passed)

    result = StripAnd(minutes_passed)
    return result


# 2. performs computation
def Calculate(dob_validated):
    today = date.today()
    dob = date.fromisoformat(dob_validated)
    rc = str(abs( today-dob ))
    return rc


# 3. parses the user input into manageable forms
def Parse(dob_computed):
    pattern = r"^([0-9]+)\s.+$"
    matches = re.search(pattern, dob_computed, flags=re.VERBOSE)
    return matches.group(1)


# 1. validates the user input
def Validate(dob_validated):
    rc = -1

    pattern = r"""
                ^
                \d{4}-\d{2}-\d{2}
                $
               """

    match = re.match(pattern, dob_validated, re.VERBOSE)
    if match:
        rc = dob_validated

    return rc


# 4. transform the days into minutes
def Transform(days_parsed):
    # print(days_parsed)
    minutes = days_parsed * MINS_PER_DAY
    p = inflect.engine()
    rc = str(p.number_to_words(minutes)).capitalize() + " minutes"

    return rc


# utility -> check errors (None flag)
def CheckError(rc):
    if rc == -1:
        sys.exit("Invalid date")


# utility -> strip away "and" words
def StripAnd(string):
    pattern = r"\sand[^\strillion][^\sbillion][^\smillion][^\sthousand][^\shundred]"
    replacement = r","
    temp = re.sub(pattern, replacement, string)
    pattern2 = r"\sand"
    replacement2 = r""
    rc = re.sub(pattern2, replacement2, temp)
    return rc


def Debug():
    today = date.today()                                            # <class "datetime.date">
    chosen_date = date.fromisoformat("2024-04-26")                  # <class "datetime.date">
    print( f"type of today is {type(today)}, and type of chosen date is {type(chosen_date)}")

    print( f"today's date is -> {today}" )
    print( f"chosen date is -> {chosen_date}" )

    delta = abs(today - chosen_date)
    print( f"the delta date type is -> { type(delta) }" )

    parsed = str(delta)
    print( f"{str(delta), parsed}" )

    pattern = "^([0-9])+.+$"
    matches = re.search(pattern, parsed, flags=re.VERBOSE)
    print("matched object group 1 is -> ", matches.group(1))


if __name__ == "__main__":
    main()
