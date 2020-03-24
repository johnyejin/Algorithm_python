# 19.6점...
def check(frame, ans):
    x, y, what = frame
    # 기둥
    # 1. 바닥 위에 있어야댐
    # 2. 보의 한쪽 끝 부분 위에 있어야댐
    # 3. 다른 기둥 위에 있어야댐
    if what == 0:
        if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
            return True
    # 보
    # 1. 한쪽 끝 부분이 기둥 위에 있어야댐
    # 2. 양쪽 끝 부분이 다른 보와 동시에 연결
    else:
        if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans:
            return True
        if [x-1, y, 1] in ans and [x+1, y, 1] in ans:
            if [x-1, y-1, 0] in ans and [x+2, y-1, 0] in ans:
                return True


    return False


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, what, how = frame

        if how == 1:  # 설치
            print("설치", check([x, y, what], answer))
            if check([x, y, what], answer):
                answer.append([x, y, what])
        else:  # 삭제
            print("삭제", check([x, y, what], answer))
            if check([x, y, what], answer):
                answer.remove([x, y, what])
        print(answer)

    answer.sort()
    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	))