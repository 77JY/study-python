from collections import defaultdict
def solution(genres, plays):
    music = defaultdict(int)
    music_rank = defaultdict(list)
    answer = []
    for i in range(len(genres)):
        music[genres[i]] += plays[i]
        music_rank[genres[i]].append([plays[i], i])
    music = sorted(music.items(), key=lambda x: x[1], reverse=True)
    for name, _ in music:
        lists = music_rank[name]
        lists.sort(key=lambda x: x[0], reverse=True)
        answer.append(lists[0][1])
        if 1 < len(lists):
            answer.append(lists[1][1])
        
    return answer