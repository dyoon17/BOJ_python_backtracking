#15649. N과 M (1)

def solve(N, M):
    def backtrack(used, sequence):
        if len(sequence) == M:  # 길이가 M인 수열이 완성된 경우
            print(" ".join(map(str, sequence)))  # 출력
            return
        
        for i in range(1, N + 1):  # 1부터 N까지 숫자 탐색
            if i not in used:  # 중복 여부 확인
                backtrack(used | {i}, sequence + [i])  # 숫자를 추가하고 재귀 호출

    backtrack(set(), [])  # 초기값으로 빈 집합과 빈 리스트에서 시작

# 입력 예시
N, M = map(int, input().split())
solve(N, M)
