def imt():
    a = (float(input("Your height in cm: ")))/100
    b = float(input("Your weight in kg: "))
    i = b/(a*a)
    if i <= 16:
        print("Выраженный дефицит массы тела")
    if 16 < i <= 18.5:
        print("Недостаточная (дефицит) масса тела")
    if 18.5 < i <= 24.99:
        print("Норма")
    if 25 < i <= 30:
        print("Избыточная масса тела (предожирение)")
    if 30 < i <= 35:
        print("Ожирение первой степени")
    if 35 < i <= 40:
        print("Ожирение второй степени")
    if 40 < i:
        print("Ожирение третьей степени (морбидное)")


imt()
