# Day02

## Git 설정(한번만 설정) 

* `git config --global user.name '~'`
* `git config --global user.email '~@gamil.com'`
* `git init` : git 초기화, git으로 관리하겠다.
* `git remote add origin 주소` 원격 저장소 등록
  * `git remote set-url origin 주소` : 원격 저장소 수정

## Git Commit & Push(지속 설정)

* `git status` : 현재 폴더의 git의 상태
* `git add .` : 현재 폴더의 변경 사항들을 commit하기 위해서 준비
* `git command -m 'day02'입니다.` : commit 변경 사항 저장. 메세지는 자유롭게 작성 가능 
* `git push -u origin master` : remote로 등록된 원격 저장소(remote repository)
  * 이후에는 `git push`만 입력해도 동작합니다.



* Markdown 기록할 것입니다.
  * Typora or VSCode

* GitHub Student Developer Pack



## 파일조작

* 500개 text 문서 생성

``` python
import os
import random
family = ['김','이','박','최','황','오','강','한','제갈','하','정','송','현','손','조']
given = ['길동','준','민준','소미','수진','지은','동해','민태','준호','세정','지훈','성우','성원']

for i in range(500):
    cmd = f"touch {str(i)}_{random.choice(family)}{random.choice(given)}.txt"
    #touch는 새로운 파일 하나 생성
    print(cmd)
    os.system(cmd)
```



* 파일 이름 바꾸기

```python
import os

os.chdir(r'C:\Users\student\MJ\day02\dummy')
#print(os.getcwd())

for filename in os.listdir('.'):
    #1. replace 함수 이용, 새로운 파일 이름 생성
    new_filename = filename.replace('지원자_지원자_', '합격자_')
    #2. os.rename 함수 이용, 파일 이름 변경
    os.rename(filename, new_filename)
```



*   파일쓰기

```python
with open('ssafy.text','w',encoding='utf8') as f:
    # for i in range(10):
    #     f.write(f'This is \"SSAFY\", {i}\n')
    
    f.writelines(['1\n','2\n','3\n'])
```



* 파일 읽기

```python
with open('ssafy.text','r',encoding='utf8') as f:
    lines = f.readlines()
    for line in reversed(lines):
        print(line.strip())
```



### Reverse Challenge

* 한번에 read/write 실행

```python
with open('ssafy.text', 'r',encoding='utf8') as f:
        lines = f.readlines()
     	with open('ssafy_reverse.text', 'w', encoding='utf8') as u:
         	u.writelines(lines)
```



* read/write 각각 실행

  ```python
  with open('ssafy.text', 'r',encoding='utf8') as f:
      lines = f.readlines()
  
  lines.reverse()
  
  with open('ssafy_reverse.text', 'w', encoding='utf8') as f:
      f.writelines(lines)
  
  ```



## CSV

* csv 쓰기

```python
lunch = {
    '둥지': '031-244-4567',
    '신가네': '032-395-9356',
    '이모네': '02-314-2245'
}

import csv

with open('lunch.csv', 'w', encoding='utf8',newline='') as f: #newline = 빈 줄 없이 출력
    csv_writer = csv.writer(f) #f는 파일 내용
    for item in lunch.items(): #리스트 [(key,value),...]
        csv_writer.writerow(item)
        #f.write(f'{item[0]}, {item[1]}\n') => csv_writer = csv.writer(f) 안쓸때
```



* csv 읽기

```python
import csv

with open('lunch.csv','r', encoding='utf8') as f:
    items = csv.reader(f) #한 줄씩 리스트 형태로 반환
    for item in items:
        print(item)
```

출력값 = 

둥지,031-244-4567

신가네,032-395-9356

이모네,02-314-2245



## Naver_Rank Challenge

* 실시간 검색어 1위 부터 10위 까지 출력 

```python
import requests
import bs4

response = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(response,'html.parser')
result = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a > span.ah_k')

for title in result:
    print(title.text)
```



* 헤더를 이용하여 사이트 속이기

```python
import requests
import bs4

h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

response = requests.get('https://www.melon.com/chart/index.htm',headers=h).text
print(response)
```

