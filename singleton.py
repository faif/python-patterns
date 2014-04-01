class MySingleton():

    __instance = None

    def __init__(self):
        self.__count = 0

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value

    @staticmethod
    def getInstance():
        if not MySingleton.__instance:
            MySingleton.__instance = MySingleton()
        return MySingleton.__instance


def main():
    s1 = MySingleton().getInstance()
    s1.count = 2
    print("Count of s1 is {}".format(s1.count))

    s2 = MySingleton().getInstance()
    print("Count of s2 is {}".format(s2.count))
    s2.count = 3

    print("Count of s1 is {} and count of s2 is {}".format(s1.count, s2.count))


if __name__ == '__main__':
    main()

### OUTPUT ###
# Count of s1 is 2
# Count of s2 is 2
# Count of s1 is 3 and count of s2 is 3