"""A singleton counter.
   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value
   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""


class Counter:
    """Counter in Singleton pattern."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__count = 1
        return cls._instance

    @property
    def count(self):
        """a property: readonly
        :return count"""
        return self.__count

    def increment(self):
        """add 1 to current count
        :return count + 1"""
        self.__count += 1
        return self.__count

    def __del__(self):
        del self.__count

    def __str__(self):
        return f"{self.__count}"


if __name__ == "__main__":
    s1 = Counter()
    s2 = Counter()

    # Test Singleton
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
