def main():
    time = input("What time is it? ")
    time = convert(time)
    # print(time)

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")


def convert(time):
    hour, minute = time.strip().split(":")
    hour = int(hour)
    minute = int(minute)
    return hour + minute/60


if __name__ == "__main__":
    main()
