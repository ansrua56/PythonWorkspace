# for i in range(1, 1001) :
#     sum = 0
#     for j in range(1, i+1) :
#         if i % j == 0:
#             if i != j :
#                 sum += j
#     if sum == i :
#         print('완전수 :', sum)

# num = int(input('숫자를 입력하세요 :'))
# for i in range(1, num+1) :
#     count = 0
#     for j in range(1, i+1) :
#         if i % j == 0 :
#             count += 1
#     if count == 2 :
#         print(i)

rows = int(input('홀수의 줄 수를 입력 : '))
blank = ' '
star = '*'
for i in range(rows//2, -1, -1) :
    print(blank*i + star*(rows-i*2))
for i in range(1, rows//2+1) :
    print(blank*i + star*(rows-i*2))