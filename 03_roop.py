'''
n=0
while n<5: #while은 종료조건을 알려줘야함
    print('저의 꿈은 한량입니다.')
    n+=1
    


foods = ['pizza', 'pasta', '떠뽀끼', '순대']

for food in foods: #for문은 제한조건 안에서 정해진 수만큼 돎
    print(food)


numbers = [1, 2, 3, 4, 5, 6]
#nubers에서 for문을 사용해 각각의 요소에 2를 곱해주세요
new_numbers = []
for i in numbers:
    result = i*2
    new_numbers.append(result)
    print (result, end=' ,')
    
print(new_numbers)

for i in range(1,10):
    for j in range(1,10):
        print(f'{i}*{j}={i*j}', end=' ')
    print()
'''