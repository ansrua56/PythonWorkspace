# ls = [10, 20, 30]
# arr = [40, 50, 60]
# print(ls + arr)
# print()

# ls = [4, 8, 2, 7, 6]
# for i in range(len(ls)) :
#     if i < 4 :
#         for j in range(i+1, len(ls)) :
#             if ls[i] > ls[j] :
#                 temp = ls[i]
#                 ls[i] = ls[j]
#                 ls[j] = temp
# print(ls)

score = [82, 85, 76, 79, 96]
rank = [1, 1, 1, 1, 1]
for i in range(len(score)) :
    temp = score[i]
    for j in range(len(score)) :
        if temp < score[j] :
            rank[i] += 1
print(rank)