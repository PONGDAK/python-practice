'''
a= dict()
a= {'이름':'김재석','나이':19}

print(dir(dict))
a['취미']='강의'
print(a)
#각 지역번호가 담긴 딕셔너리를 만들어보세요 서울 -02/ 경기 -031 / 제주 -064
phone_book={'서울': '-02','경기':'-031','제주':'-064'}
print(phone_book.get('제주'),phone_book['제주']) #get으로 접근했을시 키값이 없으면 None을 리턴함, 두번째방식은 키값 없으면 에러생김

print(phone_book.items(), phone_book.keys(), phone_book.values())

print(phone_book.pop('서울'))
print(phone_book)
'''

set_a = {1, 2, 3}
set_b = {3, 6, 9}

