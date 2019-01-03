blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']
a=0
b=0
ab=0
o=0
for i in blood_types:
    if i =='A':
        a+=1
    elif i=='B':
        b+=1
    elif i=='AB':
        ab+=1
    elif i=='O':
        o+=1
print(f'A형: {a}, B형: {b}, AB형: {ab}, O형: {o}')

####
print('A형: ',blood_types.count('A'))
print('B형: ',blood_types.count('B'))
print('AB형: ',blood_types.count('AB'))
print('O형: ',blood_types.count('o'))

####
result = {}
for blood_type in blood_types:
    if blood_type in result:
        result[blood_type]+=1
    else:
        result[blood_type]=1
