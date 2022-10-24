# for i in range(1, 31) :
#     if i % 5 != 0 :
#         print(i, end = '\t')
#     else :
#         print(i, end = '\n')

# num = int(input('숫자를 입력해주세요 : '))
# sum = 0
# for i in range(1, num+1) :
#     sum += i
# print('총합 :', sum)

# num = int(input('숫자를 입력해주세요 : '))
# sum1 = 0
# sum2 = 0
# for i in range(1, num+1) :
#     if i % 2 == 0 :
#         sum1 += i
#     else :
#         sum2 += i
# print('짝수 합 :', sum1, '\n홀수 합 :', sum2)

# sum = 0
# for i in range(1, 101) :
#     if i % 3 == 0 :
#         if i % 5 == 0 :
#             sum += i
#     else :
#         sum += i
# print(sum)

# num1 = int(input('숫자1 입력 : '))
# num2 = int(input('숫자2 입력 : '))
# sum = 0
# if num1 < num2 :
#     for i in range(num1, num2+1) :
#         sum += i
# else :
#     for i in range(num2, num1+1) :
#         sum += i
# print('총합 :', sum)

# money = 10
# for i in range(2, 31) :
#     money *= 2
# print(money)

st = "It is a fun Python class"
anum = 0
snum = 0
for i in st :
    if i == 'a' :
        anum += 1
    elif i == 's' :
        snum += 1
print('===결과===')
print('총 개수 :', len(st))
print('a 개수 :', anum)
print('s 개수 :', snum)