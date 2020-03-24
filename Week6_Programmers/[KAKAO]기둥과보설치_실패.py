# 9.6점...
# build_frame = [x, y, a, b]
# a: 0 = 기둥, 1 = 보
# b: 0 = 삭제, 1 = 설치
def check(frame, ans):
    # 기둥인 경우
    if frame[2] == 0:
        if frame[1] == 0:  # 1. 바닥 위에 있어야댐
            return True
        try:  # 2. 보의 한쪽 끝 부분 위에 있어야댐
            if ans.index([frame[0]-1, frame[1], 1]) >= 0:
                return True
        except: cnt = 0
        try:  # 2. 보의 한쪽 끝 부분 위에 있어야댐
            if ans.index([frame[0]+1, frame[1], 1]) >= 0:
                return True
        except: cnt = 0
        try:  # 3. 다른 기둥 위에 있어야댐
            if ans.index([frame[0], frame[1]-1, 0]) >= 0:
                return True
        except:
            return False

    # 보인 경우
    else:
        try:  # 1. 한쪽 끝 부분이 기둥 위에 있어야댐(왼쪽)
            if ans.index([frame[0], frame[1]-1, 0]) >= 0:
                return True
        except: cnt = 0
        try:  # 1. 한쪽 끝 부분이 기둥 위에 있어야댐(오른쪽)
            if ans.index([frame[0]+1, frame[1]-1, 0]) >= 0:
                return True
        except: cnt = 0
        try:  # 2. 양쪽 끝 부분이 다른 보와 동시에 연결
            if ans.index([frame[0]-1, frame[1], 1]) >= 0 and ans.index([frame[0]+1, frame[1], 1]) >= 0:
                # 삭제할때 옆에 있는 보가 조건을 만족하지 않는 경우
                try:
                    ans.index([frame[0] - 1, frame[1] - 1, 0])
                    ans.index([frame[0] + 2, frame[1] - 1, 0])
                except:
                    return False
                return True
        except:
            return False


def solution(n, build_frame):
    answer = []  # 정렬
    arr = [[-1] * n for _ in range(n)]

    for frame in build_frame:
        # 설치하는 경우 설치 가능한지 체크
        if frame[3] == 1:
            print("설치", check(frame, answer), frame)
            if check(frame, answer):
                answer.append(frame[:3])

        # 삭제하는 경우 삭제 가능한지 체크
        else:
            print("삭제", check(frame, answer))
            if check(frame, answer):
                answer.pop(answer.index(frame[:3]))
        print(answer)

    answer.sort()
    return answer


# print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))