
try:
    c = ""
    while c.upper() != "Q":
        a = int(input("첫번째 숫자 입력:"))
        b = int(input("두번째 숫자 입력:"))
        c = input("연산자 입력 Q(quit):")
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        print(a/b)
    elif c == "//":
        print(a//b)
    elif c == "**":
        print(a**b)
except:
    print("Please enter a mutu")


c.upper()
