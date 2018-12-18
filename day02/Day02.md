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



* 파일 쓰기

```python
# f = open('ssafy.text','w') #w:write, r: read, a: append
# f.write('This is SSAFY')
# f.close() #꼭 추가

with open('ssafy.text','w',encoding='utf8') as f:
    f.write('This is SSAFY, with 이용했다')
```

