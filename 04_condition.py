'''
if False:
    print('false')
else:
    print('true')
    


num = int(input('숫자 입력 ㄱ: '))

if num %2==1:
    print('홀수')
else:
    print('짝수')
'''
dust = int(input('미세먼지 농도 입력 : '))
if dust > 150:
    print('매우나쁨')
elif dust >80:
    print('나쁨')
elif dust >30:
    print('보통')
else:
    print('좋음')
    
odd =[]
even =[]
for i in range(1,11):
    if i %2==1:
        odd.append(i)
    else:
        even.append(i)

print(odd, even)