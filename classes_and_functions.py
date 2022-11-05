class Time:
    '''

    '''


time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def print_time(time):
    print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))


def is_after(t1, t2):
    t1_sec = t1.hour * 3600 + t1.minute * 60 + t1.second
    t2_sec = t2.hour * 3600 + t2.minute * 60 + t2.second
    return t1_sec > t2_sec


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum


noon_time = Time()
noon_time.hour = 12
noon_time.minute = 0
noon_time.second = 0

end_time = Time()
end_time.hour = 13
end_time.minute = 49
end_time.second = 0

print(is_after(end_time, noon_time))
