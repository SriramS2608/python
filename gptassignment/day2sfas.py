a = {'santoor':234,'lifebouy':343,'mysoor':342}
print(a.keys())
print(a.values())
print(a['lifebouy'])
print(list(a))

#6
a = 34
print(int(a))
print(type(a))
a=23
b= float(a)
print(b)
print(type(b))
print(bool(a))
print(type(a))
print(str(a))
print(type(a))

a = 45.56
print(int(a))

s = '456'
b=int(s)
print(b)
print(b*10)

a = range(1,50,5)
print(list(a))

a = range(1,50,5)
b = list(a)
print(b[4])
print(b[-1])
print(b[3:7:])
print(b[::-1])

a = str(input('enter the value:'))
print(a[0])
print(a[-1])
print(a[::-1])
print(a[0::2])

dicta = {'std1':{'name':'ram','marks':'90'},
         'std2' :{'name':'laxmi','marks':'34'},
         'std3' :{'name':'manja','marks':'32'}
}
print(dicta['std2']['marks'])
print(dicta['std3']['name'])
d=dicta.keys()
print(d)
print(tuple(d))    

a = 45
b = 56 
print(a+b)

a =' laxmi'
print(4*a)

a ='laxmi'
b= ' is'
c = ' gay'
d = ' tlla'
print(a+b+c+d)

a = [34,55,23]
b = [65,78,23]
print(a+b)

a= 'laxmi'
b = 'kantha'
#print(a-b)

a = [34,78,23]
print(3*a)

a = eval ('10+5')
print(a)

a  = eval("python"*3)
print(a)

a =range(10,100,10)
b = list(a)
print(b[5])
print(b[-1])
print(b[::2])
print(b[::-1])


a = "100"
b = int(a)
print(b)
print(b*25)
c=float(b)
print(c)
d = str(b)
print(d)
print(type(d))


laks = {'name1':'laxmi','salary1':450000,
        'name2':'kantha','salary2':460000
        }
print(laks)

laks['salary1'] = laks['salary1'] +10000
print(laks)