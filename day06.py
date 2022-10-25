# for i in range(0, 5) :
#     for j in range(1, 6) :
#         print(j+(5*i), end='\t')
#     print()

# rice = 100000
# day = 0
# mouse = 2
# while(rice > 0) :
#     rice -= 20 * mouse
#     if day % 10 == 0 :
#         mouse *= 2
#     day += 1
# print('소요 일 :', day, '\n쥐 :', mouse)

money = int(input('요금을 투입 하세요 : '))
a = '커피 자판기'
while money > 0 :
    print(f'{a:=^30}\n', '1. 커피(200)\t', '2. 코코아(250)\t', '3. 반환\t', '4. 종료\n')
    menu = int(input('메뉴를 선택하세요>>> '))
    if menu == 1 :
        money -= 200
        if money >= 0 :
            print('맛있게 드세요')
        else :
            print('요금이 부족합니다')
    elif menu == 2 :
        money -= 250
        if money >= 0 :
            print('맛있게 드세요')
        else :
            print('요금이 부족합니다')
    elif menu == 3 :
        print('반환 금액 :', money)
    else :
        break