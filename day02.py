# name = input("이름 입력 : ")
# age = input("나이 입력 : ")
# print("결과 출력 :", name, "님의 나이는", age, "살 입니다.")

# year = int(input("올해의 년도를 입력하세요 : "))
# birth = int(input("당신이 태어난 년도를 입력하세요 : "))
# print("당신의 나이는", year-birth+1, "입니다.")

# first = float(input("첫 번째 물건의 무게를 입력하세요 : "))
# second = float(input("두 번째 물건의 무게를 입력하세요 : "))
# print("현재 엘리베이터의 허용 무게는", 600-first-second, "입니다.")

# height = int(input("키를 입력하세요 : "))
# print("표준 체중은", (height-100)*0.9, "입니다.")

# height = int(input("키를 입력하세요 : "))
# weight = int(input("현재 체중을 입력하세요 : "))
# avgweight = (height - 100) * 0.9
# print("표준 체중은", avgweight, "이고 비만도는", (weight/avgweight)*100, "입니다.")

name = input("학생 이름 : ")
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
math = int(input("수학 점수 : "))
sum = int(kor + eng + math)
a = "학생정보"
print(f"{a:=^50}")
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*54)
print(name, "\t", kor, "\t", eng, "\t", math, "\t", sum, "\t", round(sum/3, 2))