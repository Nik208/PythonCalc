print("Добро пожаловать в калькулятор.")
print("Введите операцию (+, -, *, /, //, %, **, ==, !=, >, <, >=, <=, and, or, not, &, |, ^, ~, <<, >>, in, not in, is, is not):")
Op = input()
if Op in ("+", "-", "*", "/", "//", "%", "**"):
    print("Введите первое число:")
    n1 = float(input())
    print("Введите второе число:")
    n2 = float(input())
    if Op == "+":
        Solution = n1 + n2
    elif Op == "-":
        Solution = n1 - n2
    elif Op == "*":
        Solutiont = n1 * n2
    elif Op == "/":            
        if n2 == 0:
            Solution = "Ошибка"
        else:
            Solution = n1 / n2
    elif Op == "//":
        if n2 == 0:
            Solution = "Ошибка"
        else:            
            Solution = n1 // n2
    elif Op == "%":
        if n2 == 0:
            Solution = "Ошибка"
        else:
            Solution = n1 % n2
    elif Op == "**":
        Solution = n1 ** n2
elif Op in ("==", "!=", ">", "<", ">=", "<="):
    print("Введите первое число:")
    n1 = float(input())
    print("Введите второе число:")
    n2 = float(input())
    if Op == "==":
        if n1 == n2:
            Solution = True
        else:
            Solution = False
    elif Op == "!=":
        if n1 != n2:
            Solution = True
        else:
            Solution = False
    elif Op == ">":
        if n1 > n2:
            Solution = True
        else:
            Solution = False
    elif Op == "<":
        if n1 < n2:
            Solution = True
        else:
            Solution = False
    elif Op == ">=":
        if n1 >= n2:
            Solution = True
        else:
            Solution = False
    elif Op == "<=":
        if n1 <= n2:
            Solution = True
        else:
            Solution = False
elif Op in ("and", "or", "not"):
    if Op == "not":
        print("Введите результат высказывания (True/False, 1/0)")
        n1 = input()
        if n1 in ("True", "true", "1"):
            Solution = False
        elif n1 in ("False", "false", "0"):
            Solution = True
        else:
            Solution = "Ошибка"
    if Op == "and":
        print("Введите результат первого высказывания (True/False, 1/0)")
        n1 = input()
        if n1 in ("True", "true", "1"):
            n1 = True
        elif n1 in ("False", "false", "0"):
            n1 = False
        else:
            n1 = "Ошибка"
        print("Введите результат второго высказывания (True/False, 1/0)")
        n2 = input()
        if n2 in ("True", "true", "1"):
            n2 = True
        elif n2 in ("False", "false", "0"):
            n2 = False
        else:
            n1 = "Ошибка"
        if n1 not in (True, False) or n2 not in (True, False):
            Solution = "Ошибка"
        else:
            Solution = n1 and n2
    if Op == "or":
        print("Введите результат первого высказывания (True/False, 1/0)")
        n1 = input()
        if n1 in ("True", "true", "1"):
            n1 = True
        elif n1 in ("False", "false", "0"):
            n1 = False
        else:
            n1 = "Ошибка"
        print("Введите результат второго высказывания (True/False, 1/0)")
        n2 = input()
        if n2 in ("True", "true", "1"):
            n2 = True
        elif n2 in ("False", "false", "0"):
            n2 = False
        else:
            n1 = "Ошибка"
        if n1 not in (True, False) or n2 not in (True, False):
            Solution = "Ошибка"
        else:
            Solution = n1 or n2
elif Op in ("&", "|", "^", "~", "<<", ">>"):
    if Op == "&":
        print("Введите первое число:")
        n1 = int(input())
        print("Введите второе число:")
        n2 = int(input())
        Solution = n1 & n2
    elif Op == "|":
        print("Введите первое число:")
        n1 = int(input())
        print("Введите второе число:")
        n2 = int(input())
        Solution = n1 | n2
    elif Op == "^":
        print("Введите первое число:")
        n1 = int(input())
        print("Введите второе число:")
        n2 = int(input())
        Solution = n1 ^ n2
    elif Op == "~":
        print("Введите число:")
        n1 = int(input())
        Solution = ~n1
    elif Op == "<<":
        print("Введите первое число:")
        n1 = int(input())
        print("Введите второе число:")
        n2 = int(input())
        Solution = n1 << n2
    elif Op == ">>":
        print("Введите первое число:")
        n1 = int(input())
        print("Введите второе число:")
        n2 = int(input())
        Solution = n1 >> n2
elif Op in ("in", "not in"):
    if Op == "in":
        print("Введите информацию")
        n1 = input()
        print("Введите вешь пренадлежности:")
        n2 = input()
        if n2 in n1:
            Solution = True
        else:
            Solution = False
    elif Op == "not in":
        print("Введите информацию")
        n1 = input()
        print("Введите вешь пренадлежности:")
        n2 = input()
        if n2 not in n1:
            Solution = True
        else:
            Solution = False
elif Op in ("is", "is not"):
    if Op == "is":
        print("Введите первое значение:")
        n1 = input()
        print("Введите второе значение:")
        n2 = input()
        Solution = n1 is n2
    elif Op == "is not":
        print("Введите первое значение:")
        n1 = input()
        print("Введите второе значение:")
        n2 = input()
        Solution = n1 is not n2
    print(Solution)
else:
    print("Ошибка")
