while True:
    #두개의 숫자로 이루어진 사칙연산 수식을 입력
    # #꼭 띄어쓰기를 해야함 like 1 + 1 or 2 * 3
    입력식 = input("식을 입력하세요.\n""(주의, 두 개의 숫자로 이루어진 사칙연산(+,-,*,/)만 가능합니다. ex) 20 * 20)\n"
">")
    #입력식을 띄어쓰기를 기준으로 3개로 나누고 리스트에 선언
    #띄어쓰기를 기준으로 리스트값을 나누기 때문에 입력값에 무조건 띄어쓰기를 해야함
    list = 입력식.split(' ',3)

    if "+" in list[1]:
        result = int(list[0]) + int(list[2])
        print("{} {} {} = {}".format(list[0], list[1], list[2], result))    
    if "-" in list[1]:
        result = int(list[0]) - int(list[2])
        print("{} {} {} = {}".format(list[0], list[1], list[2], result))
    if "*" in list[1]:
        result = int(list[0]) * int(list[2])
        print("{} {} {} = {}".format(list[0], list[1], list[2], result))
    try:
        if "/" in list[1]:
            result = int(list[0]) / int(list[2])
            print("{} {} {} = {}".format(list[0], list[1], list[2], result))
            "/" in list[1] and "0" in list[2]
    except ZeroDivisionError:
                print("0으로 나눌 수 없습니다.")
                continue
    input_text = input(">계산을 그만하시겠습니까?(y/n): ")
    if input_text in ["N","n"]:
        continue
    if input_text in ["Y","y"]:
        print("계산을 종료합니다.")
        break