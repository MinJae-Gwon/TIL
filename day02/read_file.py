with open('ssafy.text','r',encoding='utf8') as f:
    lines = f.readlines()
    for line in reversed(lines):
        print(line.strip())