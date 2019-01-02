a = input()
b = input()
c = input()

res = str(int(a)*int(b)*int(c))
count=0
for i in range(10):
    count=res.count(str(i))
    print(count)
    count=0

