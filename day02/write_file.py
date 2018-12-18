# f = open('ssafy.text','w') #w:write, r: read, a: append
# f.write('This is SSAFY')
# f.close() #꼭 추가

with open('ssafy.text','w',encoding='utf8') as f:
    # for i in range(10):
    #     f.write(f'This is \"SSAFY\", {i}\n')
    
    f.writelines(['1\n','2\n','3\n'])
