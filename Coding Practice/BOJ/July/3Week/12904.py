# 12904번 A와 B
s = input()
t = input()
les = len(s)
let = len(t)
while True:
    if let == les:
        break
    elif t[-1] == 'A' and len(t)>=1:
        t = t[:len(t)-1]
        let -= 1
    elif t[-1] == 'B' and len(t)>=1:
        t = t[:len(t)-1]
        t = t[::-1]
        let -=1
if s==t:
    print(1)
else:
    print(0)

