loopvalue = int(input())
result = []
for i in range(loopvalue):
    a,b,c = map(float, input().split())
    value = (a*2+b*3+c*5) / 10
    result.append(f'{value:.1f}')

for i in result:
    print(i)