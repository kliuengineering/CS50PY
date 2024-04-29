# requirements:
#               1) padding leading zeros when see fit
#               2) invalid input -> prompt again
#               3) every month -> <= 31 days


Months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


# utility function #1
def Print( parsed_date ):
    print(f"{parsed_date[0]}-{parsed_date[1]}-{parsed_date[2]}")


# utility function #2
def Padding( date ):
    for i in range( len(date) ):
        if len(date[i]) == 1:
            date[i] = "0" + date[i]
    return date


# interface
def Interface():
    parsed_date = None
    data_input = None

    while parsed_date == None:
        data_input = input("Date: ")

        parsed_date = ConversionTypeA(data_input)
        if parsed_date != None:
            Print(parsed_date)
            break

        parsed_date = ConversionTypeB(data_input)
        if parsed_date != None:
            Print(parsed_date)
            break


# converts MM/DD/YYYY to YYYY-MM-DD
def ConversionTypeA( date ):
    try:
        month, day, year = date.strip().split("/")
        date = [year, month, day]

        if Validation(date) == False:
            return

        date = Padding(date)
        return date

    except ValueError:
        return


# utility function #3
def SearchMonth( month ):
    flag = False
    for i in range( len(Months) ):
        if month == Months[i]:
            flag = i
            break
    return str(flag+1)


# utility function #4
def Validation( date ):
    flag = True

    if not ( int(date[1]) > 0 and int(date[1]) < 13 and int(date[2]) > 0 and int(date[2]) < 32 ) :
        flag = False

    return flag


# converts "Month D, YYYY" to YYYY-MM-DD
def ConversionTypeB( date ):
    try:
        month, day, year = date.strip().split(" ")

        if len(day) == 1:
            return
        day = day.strip(",")
        
        flag = SearchMonth( month )

        if flag != False:
            month = flag
            date = [year, month, day]

            if Validation(date) == False:
                return

            date = Padding( date )



            return date
        else:
            return

    except ValueError:
        return


def main():
    Interface( )


main()
