# f = open('ssafy.text','w') #w:write, r: read, a: append
# f.write('This is SSAFY')
# f.close() #꼭 추가

with open('ssafy.text','w',encoding='utf8') as f:
    f.write('This is SSAFY, with 이용했다')