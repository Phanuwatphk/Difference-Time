from datetime import datetime, timedelta

monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#จำนวนวันในแต่ละเดือน

class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

def countLeapYears(d):
    years = d.y
    if (d.m <= 2):
        years -= 1
    return int(years / 4) - int(years / 100) + int(years / 400)

def getDifference(dt1, dt2):
    n1 = dt1.y * 365 + dt1.d
    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]
    n1 += countLeapYears(dt1)
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)

    return (n2 - n1)

print("Difference Time")

while True:
    print("="*50 + "\n1 = คำนวณหาความต่างวันที่")
    print("2 = คำนวณหาความต่างเวลา")
    print("3 = คำนวณหาความต่างวันที่และเวลา")
    print("0 = ออกจากโปรแกรม")
    A = input("ตัวเลือก : ")

    if A == '1':
        print("1 = เริ่มจากวันนี้\n2 = กรอกวันที่เริ่มต้นเอง")
        A = input("ตัวเลือก : ")

        if A == '1':#ความต่างวันที่
            td = datetime.now()
            dt = input("ใส่เวลาปลายทาง(วัน/เดือน/ปี) : ").split('/')
            d, m, y = [int(item) for item in dt]
            dt1 = Date(td.day, td.month, td.year)
            dt2 = Date(d, m, y)
            sum = getDifference(dt1, dt2)
        elif A == '2':
            d1 = input("ใส่เวลาต้นทาง(วัน/เดือน/ปี) : ").split('/')
            d, m, y = [int(item) for item in d1]
            d1 = Date(d, m, y)
            d2 = input("ใส่เวลาปลายทาง(วัน/เดือน/ปี) : ").split('/')
            d, m, y = [int(item) for item in d2]
            d2 = Date(d, m, y)
            sum = getDifference(d1, d2)
        print("ห่างกัน", sum, "วัน")

    elif A == '2':#ความต่างเวลา
        print("1 = เริ่มจากตอนนี้\n2 = กรอกเวลาเริ่มต้นเอง")
        A = input("ตัวเลือก : ")

        if A == '1':
            t1 = datetime.utcnow() + timedelta(hours = 7)
            t2 = datetime.strptime(input("ใส่เวลาปลายทาง(ชั่วโมง:นาที) : "), "%H:%M")
        elif A == '2':
            t1 = datetime.strptime(input("ใส่เวลาต้นทาง(ชั่วโมง:นาที) : "), "%H:%M")
            t2 = datetime.strptime(input("ใส่เวลาปลายทาง(ชั่วโมง:นาที) : "), "%H:%M")
        delta = t2 - timedelta(hours = t1.hour, minutes = t1.minute)
        print("ห่างกัน", delta.hour, "ชั่วโมง", delta.minute, "นาที")

    elif A == '3':#ความต่างวันที่และเวลา
        print("1 = เริ่มจากตอนนี้\n2 = กรอกเวลาเริ่มต้นเอง")
        A = input("ตัวเลือก : ")
        if A == '1':
            d1 = datetime.utcnow() + timedelta(hours = 7)
            d2 = datetime.strptime(input("ใส่เวลาปลายทาง(วัน/เดือน/ปี ชั่วโมง:นาที) : "), "%d/%m/%Y %H:%M")
            dt1 = Date(d1.day, d1.month, d1.year)
            dt2 = Date(d2.day, d2.month, d2.year)
        elif A == '2':
            d1 = datetime.strptime(input("ใส่เวลาต้นทาง(วัน/เดือน/ปี ชั่วโมง:นาที) : "), "%d/%m/%Y %H:%M")
            d2 = datetime.strptime(input("ใส่เวลาปลายทาง(วัน/เดือน/ปี ชั่วโมง:นาที) : "), "%d/%m/%Y %H:%M")
            dt1 = Date(d1.day, d1.month, d1.year)
            dt2 = Date(d2.day, d2.month, d2.year)
        sum = getDifference(dt1, dt2)
        tsum = d2 - timedelta(hours = d1.hour, minutes = d1.minute)
        """sec = t_cal(dt1, dt2)
        hours = sec // (60 * 60)
        sec %= sec // (60 * 60)
        min = sec // 60"""
        print("ห่างกัน", sum, "วัน", tsum.hour, "ชั่วโมง", tsum.minute, "นาที")
  
    elif A == '0':#ออกจากโปรแกรม
        break

    else:#กรอกเลขอื่น
        print("\nกรอกตัวเลขผิด\nใส่ตัวเลข 0-3")