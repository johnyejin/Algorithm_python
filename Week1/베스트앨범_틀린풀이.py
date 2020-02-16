import collections


def solution(genres, plays):
    answer = []  # 4개

    # 1) 1,2등 장르 먼저 찾기
    genre_counter = collections.Counter(genres)  # 각 장르별 재생횟수
    for key in genre_counter:
        genre_counter[key] = 0

    for i in range(len(genres)):
        genre_counter[genres[i]] += plays[i]

    print(genre_counter.most_common(2))
    first = list(list(genre_counter.most_common(2))[0])[0]  # 1등 장르
    second = list(list(genre_counter.most_common(2))[1])[0]  # 2등 장르
    print(first, second)

    # 2) 해당 장르에서 1,2등 재생횟수 찾기 [재생횟수, 고유번호, 장르]
    # 1,2등 장르에 속하는 모든 곡을 따로 저장
    first_genre = []
    second_genre = []
    for i in range(len(genres)):
        if genres[i] == first:
            first_genre.append([plays[i], i, genres[i]])
        elif genres[i] == second:
            second_genre.append([plays[i], i, genres[i]])

    print(first_genre)
    print(second_genre)
    first_genre.sort(reverse=True)
    second_genre.sort(reverse=True)
    print(first_genre)
    print(second_genre)

    # 정답에 고유번호 추가
    # (해당 장르에 속한 곡이 1개인 경우 1개만 추가)
    if len(first_genre) == 1:
        answer.append(first_genre[0][1])
    else:
        # 해당 장르에서 횟수 같으면 고유번호 낮은거부터
        if first_genre[0][0] == first_genre[1][0] and first_genre[0][1] > first_genre[1][1]:
            answer.append(first_genre[1][1])
            answer.append(first_genre[0][1])
        else:
            answer.append(first_genre[0][1])
            answer.append(first_genre[1][1])

    if len(second_genre) == 1:
        answer.append(second_genre[0][1])
    else:
        # 해당 장르에서 횟수 같으면 고유번호 낮은거부터
        if second_genre[0][0] == second_genre[1][0] and second_genre[0][1] > second_genre[1][1]:
            answer.append(second_genre[1][1])
            answer.append(second_genre[0][1])
        else:
            answer.append(second_genre[0][1])
            answer.append(second_genre[1][1])

    return answer