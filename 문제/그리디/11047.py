# 동전 종류 N, 가치의 합 K, 필요한 동전 개수의 최솟값
# 사용할 수 있는 동전중 가장 비싼거 부터 처리?
# 가치 K보다 작은 동전 중 가장 큰거
# 가장 큰 동전 최대로 넣고, 다음 가장 큰 동전 최대로 넣고... 반복

def findMaxC(coins, K):
    for coin in coins[::-1]:
        if coin <= K:
            return coin
        
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coin_used = 0

while True:
    maxC = findMaxC(coins, K)
    coin_used += (K//maxC)
    K %= maxC
    
    if K == 0:
        break

print(coin_used)