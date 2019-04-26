'''
students = ['고상호', '양서연', '이승훈', '이원희']
print(students)
print(students[0])
print(students[1:])
print(students[:])
print(students[:2])

# print(dir(list))   dir 메서드로 이용가능한 메서드들 확인가능

a =['eat', 'more', 'SPAM!']
a.append('please')
print(a)


# print(dir(tuple))
tuple_ex1 = (1, 2)
tuple_ex2 = 1, 2
# print(tuple_ex1, tuple_ex2)
a=(1,)    #단일값 튜플은 뒤에 , 붙여줘야 튜플로 인식함
print(type(a))


tuple_ex = (1,2,3)
print(tuple_ex[1]) #튜플은 의도치않게 값이 변하는걸 방지하기위해 존재


print(list(range(5)))
print(list(range(5,8)))
print(list(range(1,10,2)))
'''