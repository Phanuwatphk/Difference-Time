from datetime import datetime, timedelta
import math

monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#จำนวนวันในแต่ละเดือน

class Date:
    def __init__(self, d, m, y):#ประกาศเพื่อรับข้อมูลไปคำนวณให้มันง่ายขึ้น
        self.d = d
        self.m = m
        self.y = y

def countLeapYears(d):#คำนวณปีอธิกสุรทิน
    years = d.y
    if (d.m <= 2):
        years -= 1
    return int(years / 4) - int(years / 100) + int(years / 400)

def getDifference(dt1, dt2):#หาความต่างระหว่างวัน
    n1 = dt1.y * 365 + dt1.d#หาจำนวนวันทั้งหมดของข้อมูลชนิด ปี + วัน
    for i in range(0, dt1.m - 1):#เอาเวลาที่เป็นวันทั้งหมดของ (ปี + วัน) บวกด้วยจำนวนวันของเดือนทั้งหมด
        n1 += monthDays[i]
    n1 += countLeapYears(dt1)#คำนวณปีอธิกสุรทิน
    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)

    return int(math.fabs(n2 - n1))#return ความห่างระหว่างวัน

def cal_f1():#ความต่างวันที่
    print("1 = เริ่มจากวันนี้\n2 = กำหนดวันที่เอง")
    A = input("ตัวเลือก : ")

    if A == '1':#เริ่มจากวันนี้
        td = datetime.now()#return เวลาปัจจุบัน
        dt = input("ใส่วันที่ที่จะเทียบ (วัน/เดือน/ปี) : ").split('/')#เก็บข้อมูลโดยแยกระหว่างวัน เดือน ปีด้วย "/"
        d, m, y = [int(item) for item in dt]#กรอกวัน เดือน ปีจาก dt ใส่ d, m, y
        d1 = Date(td.day, td.month, td.year)#กำหนดค่าวันที่ของปัจจุบันใส่ออบเจ็ค Date เพื่อคำนวณ
        d2 = Date(d, m, y)#กำหนดค่าวันที่ ที่รับเข้ามาใส่ออบเจ็ค Date เพื่อคำนวณ
    elif A == '2':#กำหนดวันที่เอง
        d1 = input("ใส่วันที่ที่ 1 (วัน/เดือน/ปี) : ").split('/')
        d, m, y = [int(item) for item in d1]
        d1 = Date(d, m, y)
        d2 = input("ใส่วันที่ที่ 2 (วัน/เดือน/ปี) : ").split('/')
        d, m, y = [int(item) for item in d2]
        d2 = Date(d, m, y)
    sum = getDifference(d1, d2)#หาความต่างวันที่
    m = 0
    s = sum#ระยะห่างทั้งหมด(วัน)
    y = sum // 365#หาจำนวนปีที่ห่าง
    sum %= 365#เอาเวลาที่หาปีออก
    if sum < 30 + (monthDays[d1.m - 1] - 30):#จำนวนวันไม่พอหาเดือน
        print("ห่างกัน", y, "ปี", m, "เดือน", sum, "วัน (%d วัน)" % s)#แสดงผล
        return 0#ออกจากฟังก์ชั่น
    sum -= 30 + (monthDays[d1.m - 1] - 30)#เอาวันในเดือนแรกออก
    m += 1#เพิ่มตัวนับเดือน
    i = 0
    while True:
        if d1.m + i > 11:#ถ้าเดือนที่คิดเกินธันวาคม
          d1.m = 0#เดือนที่หนึ่งในปีใหม่
          i = 0
        if sum < monthDays[d1.m + i]:#วันที่ที่เหลือหาจำนวนเดือนไม่ได้แล้ว
            break
        sum -= 30 + (monthDays[d1.m + i] - 30)#หาจำนวนเดือน
        m += 1
        i += 1
    print("ห่างกัน", y, "ปี", m, "เดือน", sum, "วัน (%d วัน)" % s)#แสดงผล

def cal_f2():#ความต่างเวลา
    print("1 = เริ่มจากตอนนี้\n2 = กำเวลาเอง")
    A = input("ตัวเลือก : ")

    if A == '1':#เริ่มจากตอนนี้
        t1 = datetime.utcnow() + timedelta(hours = 7)#return เวลาปัจจุบันของประเทศไทย(UTC+7) เข้าออบเจ็ค datetime แล้วเก็บไว้ใน t1
        t2 = datetime.utcnow().strptime(input("ใส่เวลาที่จะเทียบ (ชั่วโมง:นาที) : "), "%H:%M")#รับข้อมูลเวลาเข้าออบเจ็ค datetime แล้วเก็บไว้ใน t2
    elif A == '2':#กำหนดเวลาเอง
        t1 = datetime.strptime(input("ใส่เวลาที่ 1 (ชั่วโมง:นาที) : "), "%H:%M")
        t2 = datetime.strptime(input("ใส่เวลาที่ 2 (ชั่วโมง:นาที) : "), "%H:%M")
    if t2.hour > t1.hour:#เมื่อเวลาที่ 1 คืออดีตและเวลาที่ 2 คืออนาคต
        delta = t2 - timedelta(hours = t1.hour, minutes = t1.minute)#เอาเวลาที่ 2 (t2) - เวลาที่ 1 (t1) แล้วเก็บไว้ใน delta
    else:#เมื่อเวลาที่ 1 คืออนาคตและเวลาที่ 2 คืออดีต
        delta = t1 - timedelta(hours = t2.hour, minutes = t2.minute)#เอาเวลาที่ 1 (t1) - เวลาที่ 2 (t2) แล้วเก็บไว้ใน delta

    print("ห่างกัน", delta.hour, "ชั่วโมง", delta.minute, "นาที")#แสดงผล

def cal_f3():#ความต่างวันที่และเวลา
    print("1 = เริ่มจากวันที่และเวลาตอนนี้\n2 = กำหนดวันที่และเวลาเอง")
    A = input("ตัวเลือก : ")

    if A == '1':#เริ่มจากตอนนี้
        d1 = datetime.utcnow() + timedelta(hours = 7)#return เวลาปัจจุบันของประเทศไทย(UTC+7) เข้าออบเจ็ค datetime แล้วเก็บไว้ใน t1
        d2 = datetime.strptime(input("ใส่วันที่และเวลาที่จะเทียบ (วัน/เดือน/ปี ชั่วโมง:นาที) : "), "%d/%m/%Y %H:%M")#นำเข้าข้อมูล วัน เดือน ปีและเวลา(วัน/เดือน/ปี ชั่วโมง:นาที)
        dt1 = Date(d1.day, d1.month, d1.year)#เก็บวันที่ปัจจุบันใส่ออบเจ็ค Date แล้วเก็บไว้ในตัวแปร dt1
        dt2 = Date(d2.day, d2.month, d2.year)#เก็บวันที่นำเข้าใส่ออบเจ็ค Date แล้วเก็บไว้ในตัวแปร dt2
    elif A == '2':#กำหนดเวลาเอง
        d1 = datetime.strptime(input("ใส่วันที่และเวลาที่ 1 (วัน/เดือน/ปี ชั่วโมง:นาที) : "), "%d/%m/%Y %H:%M")
        d2 = datetime.strptime(input("ใส่วันที่และเวลาที่ 2 (วัน/เดือน/ปี ชั่วโมง:นาที) : "), "%d/%m/%Y %H:%M")
        dt1 = Date(d1.day, d1.month, d1.year)
        dt2 = Date(d2.day, d2.month, d2.year)
    sum = getDifference(dt1, dt2)#หาความต่างวันที่
    if d2 > d1:#เมื่อเวลาที่ 1 คืออดีตและเวลาที่ 2 คืออนาคต
        tsum = d2 - timedelta(hours = d1.hour, minutes = d1.minute)#เอาเวลาปลายทาง(จาก d2) - เวลาต้นทาง(จาก d1) แล้วเก็บไว้ในtsum
        if (d1.hour > d2.hour) or (d1.hour == d2.hour and d1.minute > d2.minute):#ตรวจหาวันว่าเวลามันข้ามไปอีกวันมั้ย
          sum -= 1
          tsum += timedelta(hours = 24)
    else:#เมื่อเวลาที่ 1 คืออนาคตและเวลาที่ 2 คืออดีต
        tsum = d1 - timedelta(hours = d2.hour, minutes = d2.minute)#เอาเวลาปลายทาง(จาก d2) - เวลาต้นทาง(จาก d1) แล้วเก็บไว้ในtsum
        if (d2.hour > d1.hour) or (d2.hour == d1.hour and d2.minute > d1.minute):#ตรวจหาวันว่าเวลามันข้ามไปอีกวันมั้ย
          sum -= 1
          tsum += timedelta(hours = 24)
    m = 0
    s = sum#ระยะห่างทั้งหมด(วัน)
    y = sum // 365#หาจำนวนปีที่ห่าง
    sum %= 365#เอาเวลาที่หาปีออก
    if sum < 30 + (monthDays[dt1.m - 1] - 30):#จำนวนวันไม่พอหาเดือน
        print("ห่างกัน", y, "ปี", m, "เดือน", sum, "วัน (%d วัน)" % s, tsum.hour, "ชั่วโมง", tsum.minute, "นาที")#แสดงผล
        return 0#ออกจากฟังก์ชัน
    sum -= 30 + (monthDays[dt1.m - 1] - 30)#เอาวันในเดือนแรกออก
    m += 1#เพิ่มตัวนับเดือน
    i = 0
    while True:
        if dt1.m + i > 11:#ถ้าเดือนที่คิดเกินธันวาคม
          d1.m = 0#เดือนที่หนึ่งในปีใหม่
          i = 0
        if sum < monthDays[dt1.m + i]:#วันที่ ที่เหลือหาจำนวนเดือนไม่ได้แล้ว
            break
        sum -= 30 + (monthDays[dt1.m + i] - 30)#หาจำนวนเดือน
        m += 1
        i += 1
    print("ห่างกัน", y, "ปี", m, "เดือน", sum, "วัน (%d วัน)" % s, tsum.hour, "ชั่วโมง", tsum.minute, "นาที")#แสดงผล

print("Difference Time")#ชื่อโปรแกรม

while True:
    print("=" * 50 + "\n1 = คำนวณหาความต่างวันที่")
    print("2 = คำนวณหาความต่างเวลา")
    print("3 = คำนวณหาความต่างวันที่และเวลา")
    print("0 = ออกจากโปรแกรม\n(กรอกปีเป็นคริสต์ศักราช)")
    A = input("ตัวเลือก : ")

    if A == '1':#ความต่างวันที่
        cal_f1()

    elif A == '2':#ความต่างเวลา
        cal_f2()

    elif A == '3':#ความต่างวันที่และเวลา
        cal_f3()

    elif A == '0':#ออกจากโปรแกรม
        break

    else:#กรอกเลขอื่นที่หน้าเมนู
        print("\nกรอกตัวเลขผิด\nใส่ตัวเลข 0-3")