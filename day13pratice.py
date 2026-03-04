#==================================================
#                  if statement
#====================================================

a = 98
b=45
if a>b:
    print(f'a:{a} is greater than b:{b}')

num =45
if num>0:
    print(f'the number {num} is positive')

a=34
if a%2 == 0:
    print(f'the number  {a} is even ')


a1=55
if a1%2 !=0:
    print(f'the number {a1} is odd')


num = 30
if num%3==0:
    print(f'the number divisible by 3')

numb = 45
if numb%5==0:
    print(f'the num is divisible by 5')

num =15
if num%3==0 and num%5==0:
    print(' the num is divisible by both 3 and 5')

stri = 'apple'
if stri[0] in 'aeiouAEIOU':
    print('the srting starts with vowels')

s1 ='microsoft'
if s1[0] not in 'aeiouAEIOU':
    print('string starts with consonents')

s2 = 'meta'
if s2[-1] in 'aeiouAEIOU':
    print('the name ends with vowels')


s3 = 'micromax'
if s3[-1] not in 'aeiouAEIOU':
    print('the number ends with consonents')


ch = 'Apple'
if 'A'<= ch <='Z':
    print('the name starts with uppercase')

ch = 'apple'
if 'a'<= ch <='z':
    print('the name starts with lowercase')

num = '9'
if '0'