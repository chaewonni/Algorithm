def solution(genres, plays):
    answer = []
    
    genre_dict = {g : 0 for g in set(genres)}
    plays_dict = {g : [] for g in set(genres)}
    
    for i in range(len(genres)):
        genre_dict[genres[i]] += plays[i]
        plays_dict[genres[i]].append((i,plays[i]))
        
    for genre in sorted(genre_dict, key=lambda x: genre_dict[x], reverse=True):
        plays_sort = sorted(plays_dict[genre], key = lambda x: x[1], reverse=True)
        if len(plays_sort) == 1:
            answer.append(plays_sort[0][0])
        else:
            for i in range(2):
                answer.append(plays_sort[i][0])
        
    return answer