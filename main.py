def late(y0, m0, d0, y2, m2, d2):
    if y2 > y0:
        return 1
    elif y2 < y0:
        return 2
    elif m2 > m0:
        return 1
    elif m2 < m0:
        return 2
    elif d2 > d0:
        return 1
    elif d2 < d0:
        return 2
    else:
        return 0


def month_day(day, month, year):
    if late(year, month, day, 1582, 10, 4) == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 10000 != 0) or (year % 40000 == 0 and year % 100000000 != 0) or year % 400000000 == 0:
            mList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            mList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        if year % 4 == 0:
            mList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            mList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return mList[month - 1]


def next_day(y, m, d, w):
    if y == 1582 and m == 10 and d == 4:
        d = 15
    else:
        d += 1
        if d > month_day(d, m, y):
            m += 1
            d = 1
        if m > 12:
            y += 1
            m = 1
        if y == 0:
            y += 1
    w += 1
    w %= 7
    return y, m, d, w


def last_day(y, m, d, w):
    if y == 1582 and m == 10 and d == 15:
        d = 4
    else:
        d -= 1
        if d <= 0:
            m -= 1
            if m <= 0:
                y -= 1
                m = 12
            d = month_day(d, m, y)
        if m <= 0:
            y -= 1
            m = 12
        if y == 0:
            y -= 1
    w -= 1
    w %= 7
    return y, m, d, w


wList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
y0, m0, d0, w0 = eval(input('y0, m0, d0, w0 = '))
print('Baseline:', y0, m0, d0, w0)
y2, m2, d2 = eval(input('y2, m2, d2 = '))
day = 0
while True:
    if late(y0, m0, d0, y2, m2, d2) == 1:
        y0, m0, d0, w0 = next_day(y0, m0, d0, w0)
    elif late(y0, m0, d0, y2, m2, d2) == 2:
        y0, m0, d0, w0 = last_day(y0, m0, d0, w0)
    else:
        print(day, 'days.')
        break
    day += 1
    print('Day:', day, '\t', y0, m0, d0, wList[w0])

