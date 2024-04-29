class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0
        self.cookie_emoji = u"\U0001F36A"

    def __str__(self):
        string = ""
        for i in range(self.size):
            string += self.cookie_emoji
        return string

    def deposit(self, n):
        if n > self.capacity - self.size:
            raise ValueError("ERROR: jar overflow...")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("ERROR: jar underflow...")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("ERROR: jar capacity < 0 ...")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("ERROR: cookie count is < 0 ...")
        self._size = size


def Debug():
    var = u"\U0001F36A"
    string = ""
    for i in range(5):
        string += var
    print(string)


def main():
    # Debug()
    jar = Jar()
    print("jar capacity -> ", jar.capacity)
    print("jar size now -> ", jar.size)

    add = 5
    jar.deposit(add)
    print(f"added {add} cookies, jar size now -> ", jar.size)
    print(f"cookie emoji -> ", jar)


if __name__ == "__main__":
    main()
