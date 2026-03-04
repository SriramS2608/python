 #############18/02/2026##########################

 #-----------------------------------------------------------------------------
                            #type casting in python                            
#-------------------------------------------------------------------------------------

#INTEGER
#that works

a = 45
print(float(a))
print(complex(a))
print(bool(a))
print(str(a))

#won't works
a = 45
print(list(a))
print(tuple(a))
print(dict(a))
print(set(a))


#float datatype conversion


#works
b = 95.3
print(int(b))
print(bool(b))
print(complex(b))
print(str(b))

# wont works

b = 95.3

print(list(b))
print(tuple(b))
print(dict(b))
print(set(b))



# complex datatype conversion

#works
c = 9+5j
print(bool(c))
print(str(c))

#wont work
c = 9+5j
print(int(c))
print(float(c))
print(list(c))
print(tuple(c))
print(set(c))
print(dict(c))


#boolen datatype conversion
#works
d = True
print(int(d))
print(float(d))
print(complex(d))
print(str(d))

#won't work
d = True
print(list(d))
print(set(d))
print(dict(d))
print(tuple(d))


#string datatype conversion

#works
s = 'python'
print(bool(s))
print(set(s))
print(tuple(s))
print(list(s))

#wont works
s = 'python'
print(int(s))
print(float(s))
print(complex(s))
print(dict(s))


#list datatype collection

#works
l = [10,20,30,40]
print(str(l))
print(tuple(l))
print(set(l))
print(bool(l))

#wont works
l = [10,20,30,40]
print(int(l))
print(float(l))
print(complex(l))
print(dict(l))

#tuples datatype collection

#works
t = (10,20,30,40)
print(set(t))
print(list(t))
print(str(t))
print(bool(t))

#wont work
t =(10,20,30,40)
print(float(t))
print(int(t))
print(float(t))
print(dict(t))
print(complex(t))

#set datatype collection
s ={10,20,30,40,50}
print(str(s))
print(list(s))
print(tuple(s))
print(bool(s))

#wont work
print(int())
print(float())
print(complex())
print(dict())

#dictionary datatype collection
d = {'name':'kantha','age':100}
print(set(d))
print(list(d))
print(str(d))
print(tuple(d))
print(bool(d))
#wont work 
##remaining
