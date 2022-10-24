'''def solution(s):
    li = map(str, s.split())
    res = []
    ans = ''
    for i in li:
        i = i[0].upper()+i[1:].lower()
        res.append(i)
    for j in res:
        ans += j + " "
    ans = ans[:-1]
    return ans
s = " 3pe3ple   unFo4 4llowed me"
print(solution(s))'''
'''
왜 틀린지 모르겠다
'''

def solution(s):
    s = s.lower()
    flag = False
    if not s[0] in '0123456789':
        s = s[0].upper() + s[1:]
    for i in range(len(s)):
        if flag == True and s[i]!=' ':
            s = s[:i] + s[i].upper() + s[i+1:]
            flag = False
        if s[i] == ' ':
            flag = True
    answer = s
    return answer

s = " 3pe3ple   unFO4 4llowed me"
print(solution(s))