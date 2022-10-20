# 1
# num = int(input('숫자 입력 : '))
# if num % 3 == 0 :
#     print('입력한 숫자는 3의 배수입니다.')
# else :
#     print('입력한 숫자는 3의 배수가 아닙니다.')

# 2
# num = int(input('숫자 입력 : '))
# if num % 2 == 0 :
#     print('입력한 숫자는 짝수입니다.')
# else :
#     print('입력한 숫자는 홀수입니다.')

#3
# num1 = int(input('숫자 입력1 : '))
# num2 = int(input('숫자 입력2 : '))
# if num1 > num2 :
#     print(str(num1) + "이 " + str(num2) + "보다 큽니다.")
# elif num1 < num2 :
#     print(str(num1) + "이 " + str(num2) + "보다 작습니다.")
# else :
#     print('두 수는 동일합니다.')

#4
# num = int(input('숫자 입력 : '))
# if num < 0 :
#     print(str(num) + '의 절대값은 ' + str(num * -1) + '입니다.')
# else :
#     print(str(num) + '의 절대값은 ' + str(num) + '입니다.')

#5
# day = int(input('날짜를 입력해주세요 : '))
# if day % 7 == 1 :
#     print('월요일 입니다.')
# elif day % 7 == 2 :
#     print('화요일 입니다.')
# elif day % 7 == 3 :
#     print('수요일 입니다.')
# elif day % 7 == 4 :
#     print('목요일 입니다.')
# elif day % 7 == 5 :
#     print('금요일 입니다.')
# elif day % 7 == 6 :
#     print('토요일 입니다.')
# elif day % 7 == 0 :
#     print('일요일 입니다.')

#6
# num1 = int(input('숫자1 입력 : '))
# num2 = int(input('숫자2 입력 : '))
# num3 = int(input('숫자3 입력 : '))
# if num1 > num2 :
#     if num1 > num3 :
#         print(num1, '이 가장 큰 수')
#     else :
#         print(num3, '이 가장 큰 수')
# if num1 < num2 :
#     if num2 > num3 :
#         print(num2, '이 가장 큰 수')
#     if num2 < num3 :
#         print(num3, '이 가장 큰 수')

#7
# num1 = int(input('숫자1 입력 : '))
# num2 = int(input('숫자2 입력 : '))
# if num1 > num2 :
#     if num1 % 2 == 0 :
#         print(num1, '은 큰 수 이면서 짝수이다.')
# elif num1 < num2 :
#     if num2 % 2 == 0 :
#         print(num2, '는 큰 수 이면서 짝수이다.')

#8
num1 = int(input('숫자1 입력 : '))
num2 = int(input('숫자2 입력 : '))
sum = num1 + num2
if sum % 2 == 0 :
    if sum % 3 == 0 :
        print('두 수의 합은 짝수이면서 3의 배수이다.')