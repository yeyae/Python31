#for문과 함께 자주 사용하는 range 함수
add = 0
for i in range(1, 11):
    add = add + i
print(add)

#60점 이상이면 합격

marks = [90, 45, 20, 67, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))