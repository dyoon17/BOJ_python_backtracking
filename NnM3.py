#15651. N과 M (3)

def solve(N, M):
    result = set()  # 중복 제거를 위한 set 생성

    def backtrack(sequence):
        if len(sequence) == M:  # 길이가 M인 수열이 완성되었을 때
            result.add(tuple(sequence))  # tuple로 변환하여 set에 추가
            return

        for i in range(1, N + 1):  # 1부터 N까지 숫자를 선택
            backtrack(sequence + [i])  # 현재 수를 추가한 새로운 수열로 재귀 호출

    backtrack([])  # 초기 상태로 시작
    for seq in sorted(result):  # 사전 순으로 정렬하여 출력
        print(" ".join(map(str, seq)))

# 입력 예시
N, M = map(int, input().split())
solve(N, M)
