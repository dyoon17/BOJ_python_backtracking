#15652. N과 M (4)

def solve(N, M):
    def backtrack(start, sequence):
        if len(sequence) == M:  # 길이가 M인 수열이 완성된 경우
            print(" ".join(map(str, sequence)))  # 출력
            return
        
        for i in range(start, N + 1):  # 현재 숫자부터 N까지 탐색
            backtrack(i, sequence + [i])  # 같은 숫자를 중복 선택할 수 있으므로 start를 그대로 전달

    backtrack(1, [])  # 초기값으로 시작 숫자를 1로 설정하고 빈 리스트에서 시작

# 입력 예시
N, M = map(int, input().split())
solve(N, M)
