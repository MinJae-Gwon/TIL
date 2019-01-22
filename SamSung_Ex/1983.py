# 10 개의 평점을 총점이 높은 순서대로 부여하는데,

# 각각의 평점은 같은 비율로 부여할 수 있다.

# 예를 들어, N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.

# 입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고,

# 학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,

# K 번째 학생의 학점을 출력하는 프로그램을 작성하라.

score_list=['A+', 'A0', 'A-', 'B+', 'B0',"B-", 'C+', 'C0', 'C-','D0']
T=int(input())
for i in range(T):
    N,K=map(int,input().split())
    l=[]
    index_dic={}
    score_dic={}
    for j in range(N):
        m,f,a = map(int,input().split())
        sum_score = m*0.35+f*0.45+a*0.2
        l.append(sum_score)
        index_dic[j]=sum_score
    l.sort(reverse=True)
    
    for m in range(10):
        sl=l[int(N/10*m):int(N/10*(m+1))]
        for pair in sl:
            score_dic[pair]=score_list[m]
    
    res=score_dic[index_dic[K-1]]
    print(f'#{i+1} {res}')


    


   
