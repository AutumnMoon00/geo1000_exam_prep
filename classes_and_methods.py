# class Time():
#
#     def __str__(self):
#         text = ''
#         return text
#
#     def print_time(self):
#         print("" % ())
#

class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # def __add__(self, other):
    #     seconds = self.time_to_int() + other.time_to_int()
    #     return int_to_time(seconds)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()


def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time


start = Time()
start.hour = 9
start.minute = 45
start.second = 00
start.print_time()

end = start.increment(1337)
end.print_time()
print(end.is_after(start))
