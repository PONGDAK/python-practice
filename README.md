1. github repo 만들기 

   - github에서 repo 만들고 C9 터미널에 아래와 같은 명령어 설정 

    ```bash
   $ git config --global user.name 'Jaeseok Kim'
   $ git config --global user.email 'jaeseok@hphk.kr'
   $ git init
   $ git status
   $ git add .
   $ git status
   $ git commit -m "first commit"
   $ git remote add origin https://github.com/edujustin/TIL.git
   $ git push -u origin master
   
   # workspace README.md 파일 수정후 
   $ git status
   $ git add README.md
   $ git status
   $ git commit -m "added README.md"
   $ git push # 이제부터는 push 그대로
    ```

   

2. typora 설치 후 마크다운 기본 문법 학습

   ```markdown
   1. # 
   2. * * / _ _
   3. ** ** / __ __
   4. ~ ~ 
   5. 1. - 
   6. 링크: []()
   7. 이미지: ![]()
   8. 인라인 코드 강조: ` ` 
   9. ``` 전체 코드라인
   ​```
   10. ||||: 표
   11. 인용문: >
   12.수평선: --- / *** 
   
   
   ```

   

3. for / if 문 문제 풀이 

   [Python tutor](<http://pythontutor.com/>)

   ```python
   #1번
   even_numbers = []
   odd_numbers = []
   
   for i in range(1, 11):
       if i % 2: 
           odd_numbers.append(i)
       else:
           even_numbers.append(i)
           
   print(f'짝수 리스트: {even_numbers}, 홀수 리스트: {odd_numbers}')
   ```

   ```python
   numbers = [2, 4, 6, 7, 4, 3, 1, 2, 3]
   new_numbers = []
   
   for number in numbers:
       if number not in new_numbers:
           new_numbers.append(number)
   print(sorted(new_numbers))
   ```

   ```python
   for i in range(1, 101):      
       if i % 15 == 0:          
           print('FizzBuzz')   
       elif i % 3 == 0:         
           print('Fizz')        
       elif i % 5 == 0:         
           print('Buzz')        
       else:
           print(i)            
   ```

4. 함수의 4가지 형태

   - 인자/return O

     ```python
     def sum(a, b):
         result = a + b
         return result
     
     num = sum(2, 5)
     print(num) # 7
     print(type(num)) # int
     ```

     

   - 인자 O

     ```python
     def say(name, age):
         print(f'제 이름은 {name}이고, 나이는 {age}입니다.')
         
     a = say('justin', 19)
     print(a) 
     print(type(a)) 
     ```

     

   - 리턴 O

     ```python
     def say():
         return "Hi"
     
     a = say()
     print(a) 
     print(type(a))
     ```

     

   - 인자/return X

     ```python
     def say():
         print('안녕하세요. 제 이름은 justin입니다. 제 나이는 19살입니다.')
     
     a = say()
     print(a)
     print(type(a)) 
     ```

     

5. 위치 인자 / 기본값 

   ```python
   def my_func(a, b, c):
       print(f'첫번째는 {a} 두번째는 {b} 세번째는 {c}입니다.')
       return a + b + c
   
   a = my_func(1, 2, 3)
   print(a)
   print(type(a))
   ```

   ```python
   def greeting(name='justin'):
       print(f'{name} 안녕?')
       
   greeting()
   greeting('좌동철')
   ```
