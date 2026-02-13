def solution(genres, plays):

    answer = []
    
    # [복잡한 딕셔너리 구조 설계]
    # album_info = {
    #     "classic": {
    #         "total": 1450,
    #         "songs": [(800, 3), (500, 0), (150, 2)]
    #     },
    #     ...
    # }
    album_info = {}

    # 1. 데이터 구조화
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in album_info:
            album_info[genre] = {"total": 0, "songs": []}
        
        album_info[genre]["total"] += play
        album_info[genre]["songs"].append((play, i))

    # 2. 장르별 총 재생 횟수를 기준으로 장르명 정렬 (조건 1 충족)
    # 장르명을 리스트로 추출한 뒤 'total' 값을 기준으로 내림차순 정렬
    sorted_genres = sorted(album_info.keys(), 
                           key=lambda x: album_info[x]["total"], 
                           reverse=True)

    # 3. 정렬된 장르 순서대로 순회하며 곡 선택
    for genre in sorted_genres:
        # 해당 장르 내의 곡들을 정렬 (조건 2, 3 충족)
        # x[0](재생 횟수)는 내림차순(-), x[1](고유 번호)은 오름차순(+)
        current_genre_songs = sorted(album_info[genre]["songs"], 
                                     key=lambda x: (-x[0], x[1]))
        
        # 4. 최대 두 개까지 베스트 앨범에 추가 (조건 4 충족)
        answer.extend([song[1] for song in current_genre_songs[:2]])

    return answer