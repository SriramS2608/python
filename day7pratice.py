############dictionary #############################333
#-----------------------------------------------------------
d1 = {'a':24 , 'b':324}
print(d1)
print(type(d1))

data = {'ename':'smith','salary':874224,'job':'analyst'}
print(data)
print(data.keys())
print(data.values())
print(data.items())


employee = {'emp1':{'ename':'smith','sal':98392},
'emp2':{'ename':'martin','sal':23232},
'emp3':{'ename':'scott','sal':28323},
'emp4':{'ename':'allen','sal':32344}
}
print(employee['emp3']) 
print(employee['emp3'] ['ename'])           
print(employee['emp2'])
print(employee['emp4'],employee['emp3'])
print(employee['emp4']['ename'],employee['emp3']['sal'])
print(employee.keys())
print(employee.values())
print(employee.items())
