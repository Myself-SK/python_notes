def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


class UserString:
    def __init__(self, string):
        self.string = string

    def length(self):
        return len(self.string)

    def reverse(self):
        return self.string[::-1]
