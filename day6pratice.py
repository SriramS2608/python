##################3tuples##################33
a = (10,20,30,40)
print(a)
print(type(a))


b = (21,234.35,'smith',(123,31),True,False)
print(b)
print(type(b))

###################indexing####################33
t1 = (900,100,400,500,98,14,(12,3),'smith')
print(t1[1])
print(t1[2])
print(t1[-2])
print(t1[-6])
print(t1[6])
print(t1[3])
print(t1[-3])
print(t1[-2][-2])
print(t1[9])
print(t1[5])


############slicing##########3333
t1 = (900,100,400,500,98,14,[10,20,30],'smith','martin')
print(t1[1:9:1])
print(t1[2:7:1])
print(t1[0:8:1])
print(t1[0::2])
print(t1[5:9:5])
print(t1[4:9:2])
print(t1[6:9:2])
print(t1[5:9:2])
print(t1[1:8:1])


#--------------------------------------------------------------
#                         sets
#---------------------------------------------------------------
s1 = {1,2,3,4}
print(s1)
print(type(s1))

s2 = {12,23.4,'smith',True,(2,3,4)}
print(s2)
print(type(s2))

s3 ={12,44,23,64,12}
print(s3)  #wont allow duplicate values(12)


############3indexing################33
#we cant directly apply indexing on sets soo,
a = {12,34.45,True,'smith',(234,43)}
li =list(a)
print(li)
print(li[3])
print(li[4])
print(li[-4])
print(li[2])

######slicing##################3
print(li[0:4:1])
print(li[0:5:2])
print(li[0:7:3])
print(li[4:0:-1])
print(li[0:7:3])


