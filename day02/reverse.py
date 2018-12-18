#1.한번에 read/write 실행
# with open('ssafy.text', 'r',encoding='utf8') as f:
   
#     lines = f.readlines()
#     with open('ssafy_reverse.text', 'w', encoding='utf8') as u:
#         u.writelines(lines)

    
#2.read/write 각각
with open('ssafy.text', 'r',encoding='utf8') as f:
    lines = f.readlines()

lines.reverse()

with open('ssafy_reverse.text', 'w', encoding='utf8') as f:
    f.writelines(lines)
