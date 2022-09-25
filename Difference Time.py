from datetime import *

monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#จำนวนวันในแต่ละเดือน

class Date:
    def __init__(self, d, m, y):#ประกาศเพื่อรับข้อมูลไปคำนวณให้มันง่ายขึ้น
        self.d = d
        self.m = m
        self.y = y

def countLeapYears(d):#คำนวนปีปีอธิกสุรทิน
    years = d.y
    if (d.m <= 2):
        years -= 1
    return int(years / 4) - int(years / 100) + int(years / 400)

def getDifference(dt1, dt2):#หาความต่างระหว่างวัน
    n1 = dt1.y * 365 + dt1.d#หาจำนวณวันทั้งหมดของข้อมูลชนิด ปี + วัน
    for i in range(0, dt1.m - 1):#เอาเวลาที่เป็นวันทั้งหมดของ (ปี + วัน) บวกด้วยจำนวนวันของเดือนทั้งหมด
        n1 += monthDays[i]
    n1 += countLeapYears(dt1)#คำนวนปีปีอธิกสุรทิน
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)

    return (n2 - n1)#return ความห่างระหว่างวัน

print("Difference Time")  #ชื่อโปรแกรม

while True:
    print("=" * 50 + "\n1 = คำนวณหาความต่างวันที่")
    print("2 = คำนวณหาความต่างเวลา")
    print("3 = คำนวณหาความต่างวันที่และเวลา")
    print("0 = ออกจากโปรแกรม")
    A = input("ตัวเลือก : ")

    if A == '1':#ความต่างวันที่
        print("1 = เริ่มจากวันนี้\n2 = กรอกวันที่เริ่มต้นเอง")
        A = input("ตัวเลือก : ")

        if A == '1':#เริ่มจากวันนี้
            td = datetime.now()#return เวลาปัจจุบัน
            dt = input("ใส่วันที่ปลายทาง(วัน/เดือน/ปี) : ").split('/')#เก็บข้อมูลโดยแยกระหว่างวัน เดือน ปีด้วย "/"
            d, m, y = [int(item) for item in dt]#กรอกวัน เดือน ปีจาก dt ใส่ d, m, y
            d1 = Date(td.day, td.month, td.year)#กำหนดค่าวันที่ของปัจจุบันใส่ออบเจ็ค Date เพื่อคำนวณ
            d2 = Date(d, m, y)#กำหนดค่าวันที่ที่รับเข้ามาใส่ออบเจ็ค Date เพื่อคำนวณ
        elif A == '2':#กรอกวันที่เริ่มต้นเอง
            d1 = input("ใส่วันที่ต้นทาง(วัน/เดือน/ปี) : ").split('/')
            d, m, y = [int(item) for item in d1]
            d1 = Date(d, m, y)
            d2 = input("ใส่วันที่ปลายทาง(วัน/เดือน/ปี) : ").split('/')
            d, m, y = [int(item) for item in d2]
            d2 = Date(d, m, y)
        sum = getDifference(d1, d2)#หาความต่างวันที่
        m = 0
        s = sum#ระยะห่างทั้งหมด(วัน)
        y = sum // 365#หาจำนวนปีที่ห่าง
        sum %= 365#เอาเวลาที่หาปีออก
        sum -= 30 + (monthDays[d1.m - 1] - 30)#เอาวันในเดือนแรกออก
        m += 1#เพิ่มตัวนับเดือน
        i = 0
        while True:
            if d1.m > 12:#ถ้าเดือนที่คิดเกินธันวาคม
              d1.m = 0#เดือนที่หนึ่งในปีใหม่
              i = 0
            if sum < monthDays[d1.m + i]:#วันที่ที่เหลือหาจำนวนเดือนไม่ได้แล้ว
                break
            sum -= 30 + (monthDays[d1.m + i] - 30)#หาจำนวนเดือน
            m += 1
            i += 1
        print("ห่างกัน", y, "ปี", m, "เดือน", sum, "วัน (%d วัน)" % s)#แสดงผล

    elif A == '2':#ความต่างเวลา
        print("1 = เริ่มจากตอนนี้\n2 = กรอกเวลาเริ่มต้นเอง")
        A = input("ตัวเลือก : ")

        if A == '1':#เริ่มจากตอนนี้
            t1 = datetime.utcnow() + timedelta(hours = 7)#return เวลาปัจจุบันของประเทศไทย(UTC+7) เข้าออบเจ็ค datetime แล้วเก็บไว้ใน t1
            t2 = datetime.strptime(input("ใส่เวลาปลายทาง(ชั่วโมง:นาที) : "), "%H:%M")#รับข้อมูลเวลาเข้าออบเจ็ค datetime แล้วเก็บไว้ใน t2
        elif A == '2':#กรอกเวลาเริ่มต้นเอง
            t1 = datetime.strptime(input("ใส่เวลาต้นทาง(ชั่วโมง:นาที) : "), "%H:%M")
            t2 = datetime.strptime(input("ใส่เวลาปลายทาง(ชั่วโมง:นาที) : "), "%H:%M")
        delta = t2 - timedelta(hours=t1.hour, minutes=t1.minute)#เอาเวลาปลายทาง(t2) - เวลาต้นทาง(t1) แล้วเก็บไว้ใน delta
        print("ห่างกัน", delta.hour, "ชั่วโมง", delta.minute, "นาที")#แสดงผล

    elif A == '3':#ความต่างวันที่และเวลา
        print("1 = เริ่มจากวันนี้\n2 = กรอกวันที่และเวลาเริ่มต้นเอง")
        A = input("ตัวเลือก : ")

        if A == '1':#เริ่มจากตอนนี้
            d1 = datetime.utcnow() + timedelta(hours = 7)#return เวลาปัจจุบันของประเทศไทย(UTC+7) เข้าออบเจ็ค datetime แล้วเก็บไว้ใน t1
            d2 = datetime.strptime(input("ใส่วันที่และเวลาปลายทาง(วัน/เดือน/ปี ชั่วโมง:นาที) : "), "%d/%m/%Y %H:%M")#นำเข้าข้อมูล วัน เดือน ปีและเวลา(วัน/เดือน/ปี ชั่วโมง:นาที)
            dt1 = Date(d1.day, d1.month, d1.year)#เก็บวันที่ปัจจุบันใส่ออบเจ็ค Date แล้วเก็บไว้ในตัวแปร dt1
            dt2 = Date(d2.day, d2.month, d2.year)#เก็บวันที่นำเข้าใส่ออบเจ็ค Date แล้วเก็บไว้ในตัวแปร dt2
        elif A == '2':#กรอกเวลาเริ่มต้นเอง
            d1 = datetime.strptime(input("ใส่วันที่และเวลาต้นทาง(วัน/เดือน/ปี ชั่วโมง:นาที) : "), "%d/%m/%Y %H:%M")
            d2 = datetime.strptime(input("ใส่วันที่และเวลาปลายทาง(วัน/เดือน/ปี ชั่วโมง:นาที) : "), "%d/%m/%Y %H:%M")
            dt1 = Date(d1.day, d1.month, d1.year)
            dt2 = Date(d2.day, d2.month, d2.year)
        sum = getDifference(dt1, dt2)#หาความต่างวันที่
        tsum = d2 - timedelta(hours=d1.hour, minutes=d1.minute)#เอาเวลาปลายทาง(จาก d2) - เวลาต้นทาง(จาก d1) แล้วเก็บไว้ในtsum
        m = 0
        s = sum#ระยะห่างทั้งหมด(วัน)
        y = sum // 365#หาจำนวนปีที่ห่าง
        sum %= 365#เอาเวลาที่หาปีออก
        sum -= 30 + (monthDays[dt1.m - 1] - 30)#เอาวันในเดือนแรกออก
        m += 1#เพิ่มตัวนับเดือน
        i = 0
        while True:
            if dt1.m > 12:#ถ้าเดือนที่คิดเกินธันวาคม
              d1.m = 0#เดือนที่หนึ่งในปีใหม่
              i = 0
            if sum < monthDays[dt1.m + i]:#วันที่ที่เหลือหาจำนวนเดือนไม่ได้แล้ว
                break
            sum -= 30 + (monthDays[dt1.m + i] - 30)#หาจำนวนเดือน
            m += 1
            i += 1
        print("ห่างกัน", y, "ปี", m, "เดือน", sum, "วัน (%d วัน)" % s, tsum.hour, "ชั่วโมง", tsum.minute, "นาที")#แสดงผล

    elif A == '0':#ออกจากโปรแกรม
        break

    else:#กรอกเลขอื่นที่หน้าเมนู
        print("\nกรอกตัวเลขผิด\nใส่ตัวเลข 0-3")