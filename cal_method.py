class Person:
    def __init__(self,age):
        self.age=age
    def __add__(self,other):
        return f'합은 {self.age + other.age}'

p1 = Person(40)
p2 = Person(20)
print(p1+p2)


scores=[]
count = int(input("총 학생 수를 입력하세요"))

for i in range(1, count+1):
    score={}
    score["name"] = input("학생의 이름을 입력하세요")
    score["kor"] = int(input("{0} 학생의 국어 점수를 입력하세요".format(score["name"])))

    score["mat"] = int(input("{0} 학생의 수학 점수를 입력하세요".format(score["name"])))
    score["eng"] = int(input("{0} 학생의 영어 점수를 입력하세요".format(score["name"])))
    scores.append(score)

for score in scores:
    total=0
    for key in score:
        if key !="name":
            total+=score[key]
    print(f'{score["name"]} => 총점: {total}, 평균:{total/3}')

kor_total, mat_total, eng_total =0,0,0
for score in scores:
    for key in score:
        if key=="kor":
            kor_total+=score["key"]
        elif key=="mat":
            mat_total+=score["key"]
        elif key=="eng":
            eng_total+=score["key"]
print(f'{kor_total}, {mat_total}, {eng_total}')