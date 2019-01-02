student = {'python': 80, 'algorithm':99, 'django':89,'flask':83}

sum=0
for i in student.values():
    sum+=i
print(sum/len(student))

####
print(sum(student.values())/len(student))