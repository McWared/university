# Файл 5, завд. 9

# a) dd.mm.yy

dd = "24"
mm = "02"
yy = "06"

print (f"{dd}.{mm}.{yy}")

# б) dd/mm/yy

dd = "24"
mm = "02"
yy = "06"

print (f"{dd}/{mm}/{yy}")

# в) dd.mm.yyyy

dd = "24"
mm = "02"
yyyy = "2006"

print (f"{dd}/{mm}/{yyyy}")

# г) yyyy-mm-dd

dd = "24"
mm = "02"
yyyy = "2006"

print (f"{yyyy}-{mm}-{dd}")

# Файл 5, завд. 10

price = 99.99

print (f"{int(price)} грн {(price - int(price))*100} коп.")

# Файл 6, завд. 3

def findPerTriangle (a, b, c):
    result = a + b + c
    if a + b <= c or a + c <= b or b + c <= a:
        return "Такого трикутника не існує"
    return result

print (findPerTriangle (int(input("Сторона а = ")), int(input("Сторона b = ")), int(input("Сторона с = "))))