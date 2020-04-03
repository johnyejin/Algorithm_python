def solution(genres, plays):
    answer = []
    playDic = {}
    dic = {}

    for i in range(len(plays)):
        playDic[genres[i]] = playDic.get(genres[i], 0) + plays[i]
        dic[genres[i]] = dic.get(genres[i], []) + [(plays[i], i)]

    # print(playDic, dic)

    genreSort = sorted(playDic.items(), key=lambda x: -x[1])
    # print(genreSort)

    for (genre, totalPlay) in genreSort:
        dic[genre] = sorted(dic[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (_, idx) in dic[genre][:2]]

    return answer