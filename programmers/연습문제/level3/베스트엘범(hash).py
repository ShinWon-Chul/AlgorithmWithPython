from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(lambda : 0)
    new_plays = [[i, x] for i, x in enumerate(plays)]
    new_plays.sort(key = lambda x : x[1], reverse = True)
    
    for genre, play in zip(genres, plays):
        genre_dict[genre] += play
    sort_dict = sorted(genre_dict.items(), key = lambda x : x[1], reverse=True)
    target_genre = list(map(lambda x : x[0], sort_dict))
    
    for genre in target_genre:
        count = 0
        for index, play in new_plays:
            if genres[index] == genre:
                count += 1
                answer.append(index)
                if count == 2 :
                    break
    
    return answer