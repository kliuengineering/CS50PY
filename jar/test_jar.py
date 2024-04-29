from jar import Jar


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    assert jar.cookie_emoji == u"\U0001F36A"


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5


def test_deposit_unsucessful():
    jar = Jar()
    try:
        jar.deposit(13)
    except ValueError:
        pass


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5


def test_withdraw_unsucessful():
    jar = Jar()
    jar.deposit(10)
    try:
        jar.withdraw(12)
    except ValueError:
        pass
