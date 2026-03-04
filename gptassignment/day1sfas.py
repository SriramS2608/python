name = 'chinnu'
age = '5'
place = 'hassana'
print(f'hello,i am {name} from {place} and i am {age} years old')



#2
print(name.isidentifier())
print(age.isidentifier())
print(place.isidentifier())

#3
a = 234
print(a)
print(type(a))

b = 34.35
print(b)
print(type(b))

c = 12+34j
print(c)
print(type(c))

d = True
print(d)
print(type(d))


#4
a1 = 23+34j
a2 = 64+87j
print(a1+a2)


#5
msg = 'programming'
print(msg[0])
print(msg[2])
print(msg[-1])

#6
print(msg[0:5:])
print(msg[-4::])
print(msg[2:8:])

#7
msg = 'programming'
print(msg[::-1])

#8

msg = 'programming'
print(msg[::2])

#9
msg = 'programming'
print(msg[8:2:-1])

#10
data = [10, "python", 3.5, True, [1,2,3], (9,8)]
print(data[1])
print(data[2])
print(data[-2])


#11
data = [10, "python", 3.5, True, [1,2,3], (9,8)]
print(data[0:4:])
print(data[-3::1])
print(data[::2])


#12

data = [10, "python", 3.5, True, [1,2,3], (9,8)]
print(data[::-1])

#13
data = [10, "python", 3.5, True, [1,2,3], (9,8)]
print(data[-2][-2])

t = (100, 200, 300, "ram", (1,2), [10,20])
print(t[1])
print(t[3])
print(t[4])
#15
print(t[:3:])
print(t[2::])
print(t[::2])
#16
print(t[-2][-1])

#17
s = {10, 20, 30, 10, 40}
print(s)  #no duplicate values allowed

#18
s = {10, 20, 30, 10, 40}
li=list(s)
print(li)
print(li[0])
print(li[-1])
print(li[::-1])
#19
a = {23,31.42,'chinnu',(34,5,4)}
print(a)

#20
text = 'education'
print(text[::-1])
print(text[-3::])
print(text[0:7:2])
