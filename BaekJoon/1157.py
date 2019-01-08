n = input()
n = n.lower()
alphabet_list = {}
max_num=0
max_al=''
for i in n:
    if i not in alphabet_list:
        alphabet_list[i]=1
    else:
        alphabet_list[i]+=1
value = list(alphabet_list.values())

for i in alphabet_list:
        if alphabet_list[i]>=max_num:
            max_num=alphabet_list[i]
            max_al=i
if value.count(max_num) >=2:
    print('?')
else :
    print(f'{max_al.upper()}')
