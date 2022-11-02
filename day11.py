# s = set('안녕녕녕하세요')
# print(s)
# print(type(s))

import random
# score = 99
# result = 1
# while True :
#     print('1.게임시작 2.최고기록 확인 3. 종료')
#     menu = int(input('>>> : '))
#     num = random.randrange(1, 100)
#     if menu == 1 :
#         print('com :', num)
#         while True :
#             com = int(input('>>> : '))
#             if num > com :
#                 print('up')
#                 result += 1
#             elif num < com :
#                 print('down')
#                 result += 1
#             else :
#                 print('정답')
#                 break
#         if result < score :
#             print('최고기록 갱신')
#             score = result
#         result = 1
#     elif menu == 2 :
#         if score == 99 :
#             print('게임 먼저 진행하세요')
#         else :
#             print('최고 기록 :', score)
#     else :
#         break

score = 99
result = 0
while True :
    print('1.게임시작 2.최고기록 확인 3. 종료')
    menu = int(input('>>> : '))
    if menu == 1 :
        ls = []
        while True :
            for i in range(3) :
                s = random.randrange(1, 10)
                ls.append(s)
            if len(set(ls)) == 3 :
                break
        print('com :', ls)
        while True :
            strike = 0
            ball = 0
            out = 0
            com = []
            for i in range(3) :
                s = int(input('수 입력 : '))
                com.append(s)
            for i in range(3) :
                if ls[i] == com[i] :
                    strike += 1
                else :
                    num = 0
                    for j in range(3) :
                        if ls[j] == com[i] :
                            num += 1
                    if num > 0 :
                        ball += 1
                    else :
                        out += 1
            print(strike, '스트라이크,', ball, '볼,', out, '아웃')
            result += 1
            if strike == 3 :
                break
        print(result, '회', end='')
        if score > result :
            print(', 최고 기록 갱신')
            score = result
        else :
            print()
        result = 0
    elif menu == 2 :
        if score == 99 :
            print('게임 먼저 진행하세요')
        else :
            print('최고 기록 :', score)
    else :
        break