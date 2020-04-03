# 20점으로 실패
import operator

def solution(genres, plays):
    answer = []

    # 1. 많이 재생된 장르
    genreDic = dict()
    for i in range(len(plays)):
        if genres[i] in genreDic:
            genreDic[genres[i]] += plays[i]
        else:
            genreDic[genres[i]] = plays[i]

    genreDic = sorted(genreDic.items(), key=operator.itemgetter(1))
    firstGenre = genreDic[-1][0]
    secondGenre = genreDic[-2][0]
    # print(genreDic, firstGenre, secondGenre)

    # 2. 많이 재생된 노래
    firstSong = []
    secondSong = []
    for i in range(len(plays)):
        if genres[i] == firstGenre:
            firstSong.append([plays[i], i])
        elif genres[i] == secondGenre:
            secondSong.append([plays[i], i])

    # print(firstSong, secondSong)
    # 3. 낮은 고유번호
    firstSong = sorted(firstSong, key=lambda x: (-x[0], x[1]))
    secondSong = sorted(secondSong, key=lambda x: (-x[0], x[1]))
    # print(firstSong, secondSong)

    # answer에 추가
    for i in range(len(firstSong)):
        if i >= 2: break
        answer.append(firstSong[i][1])

    for i in range(len(secondSong)):
        if i >= 2: break
        answer.append(secondSong[i][1])

    return answer