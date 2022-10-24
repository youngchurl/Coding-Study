def solution(s):
    tmd = s.split()
    li = [int(i) for i in tmd]
    answer = str(min(li)) + " " + str(max(li))
    return answer
s = "1 5 2 -1 -5 -6"
print(solution(s))

'''
안풀려서 뭔가 했는데 
answer 부분에 str()로 덮어 주는걸 깜빡해서 int+str+int 문법 오류가 발생했다.
'''