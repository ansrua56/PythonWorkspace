# num = int(input('Gbyte 입력 : '))
# select = int(input('1.byte 2.Kbyte 3.Mbyte >>> '))
# if select == 1 :
#     print(num, ':', num*1024*1024*1024, 'byte')
# elif select == 2 :
#     print(num, ':', num*1024*1024, 'byte')
# elif select == 3 :
#     print(num, ':', num*1024, 'byte')

# id = input('저장할 ID 입력 : ')
# pw = input('저장할 PW 입력 : ')
# print('인증 프로그램 입니다.\nID와 PW를 입력하세요.')
# checkID = input('ID 입력 : ')
# checkPW = input('PW 입력 : ')
# if checkID != id :
#     print('인증을 통과하지 못했습니다.')
# else :
#     if checkPW != pw :
#         print('인증을 통과하지 못했습니다.')
#     else :
#         print('인증 통과 했습니다.')

time = int(input('비행기 탈 시간을 입력하세요 : '))
price = 30000
if time <= 30 :
    print('요금은', price, '원 입니다.')
else :
    time -= 30
    a = time // 10
    b = time % 10
    if a == 0 or time == 10:
        print('요금은', price+5000, '원 입니다.')
    else :
        if b == 0 :
            price += a*5000
            print('요금은', price, '원 입니다.')
        else :
            price += (a+1)*5000
            print('요금은', price, '원 입니다.')