def Calendar():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    if month > 12 or month < 0:
        return "Incorrect value"
    if month == 1:
        alldays = 0
        days = 31
        name = "January"
    elif month == 2:
        alldays = 31
        if year % 4 == 0:
            days = 29
        else:
            days = 28
        name = "February"
    elif month == 3:
        alldays = 59
        days = 31
        name = "Mart"
    elif month == 4:
        alldays = 90
        days = 30
        name = "April"
    elif month == 5:
        alldays = 120
        days = 31
        name = "May"
    elif month == 6:
        alldays = 151
        days = 30
        name = "June"
    elif month == 7:
        alldays = 181
        days = 31
        name = "July"
    elif month == 8:
        alldays = 212
        days = 31
        name = "August"
    elif month == 9:
        alldays =243
        days = 30
        name = "September"
    elif month == 10:
        alldays = 273
        days = 31
        name = "October"
    elif month == 11:
        alldays = 304
        days = 30
        name = "November"
    elif month == 12:
        alldays = 334
        days = 31
        name = "December"

    vy = (year - 1 - year % 4) / 4
    ydays = int((vy * 2 + (year - 1 - vy)) % 7)
    mdays = int(alldays % 7)
    firstday = (ydays + mdays) % 7

    a = f"    {name}     {year}" + "\n"
    a += "Mo  Tu  We  Th  Fr  Sa  Su" + "\n"
    for i in range(1, days + 1 + firstday):
        if i <= firstday:
            a += "\t"
        else:
            if i % 7 == 0:
                if i < 10 + firstday:
                    a += " " + str(i - firstday) + "\n"
                else:
                    a += str(i - firstday) + "\n"
            else:
                if i < 10 + firstday:
                    a += " " + str(i - firstday) + "\t"
                else:
                    a += str(i - firstday) + "\t"
    return f"{a}"

while True:
    print(Calendar())
