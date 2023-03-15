# 인하은행 atm1대 N명 줄서있음 1~N번호 
# i번 사람이 돈을 인출하는데 걸리는 시간 Pi분
#3 1 4 3 2 >> 3 4 8 11 13 >> 39분
# 1 2 3 3 4 << 1 3 6 9 13 >> 32분
# 총 대기시간이 최소가 되게
def sumData(data):
    sum = 0
    sum2 = 0
    for _ in data:
        sum += _
        sum2 += sum

    return sum2

N = int(input())
data = list(map(int, input().split()))
data.sort()

print(sumData(data))