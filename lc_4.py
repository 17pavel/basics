s = 'hello world'
res = ''
for i in s:
    print(i)
    if i != ' ':
        res += i

print(res)
# 2
s = 'hello world'
res = 0
for i in range(10):
    print(f"i={i}")
    res += i

print(res)
# 3
s = 'hello world'
for n, i in enumerate(s):
    print(f"{n} | {i}")
# 4
loop = 0
while True:
    if loop == 5:
        break
    print(s[loop])
    loop += 1

# 5

