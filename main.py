def calculator(a,b, mode="add"):
    # mode에 따라서 연산을 변경하는 로직구현
    if mode == "add":
        print('bbbbb')
    elif mode == "sub":
        pass
    elif mode == "mul":
        pass
    elif mode == "div":
        pass
    else:
        print("정확한 연산을 넣어주세요.")
        
        


a,b = map(int, input())

calculator(a,b,mode="add")