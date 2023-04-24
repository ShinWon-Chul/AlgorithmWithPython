def solution(players, callings):
    
    dict1 = {}
    dict2 = {}
    
    for i, player in enumerate(players):
        dict1[player] = i + 1
        dict2[i+1] = player
        
    for bplayer in callings:
        bi = dict1[bplayer]
        fi = bi - 1
        fplayer = dict2[fi]
        
        dict1[bplayer] = fi
        dict1[fplayer] = bi
        dict2[bi] = fplayer
        dict2[fi] = bplayer
    
    sorted(dict2)
    return list(dict2.values())