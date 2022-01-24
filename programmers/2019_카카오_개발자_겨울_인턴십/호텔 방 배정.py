import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def find_room(room_dict, room):
    if room_dict[room] == 0:
        room_dict[room] = room + 1
        return room_dict[room] -1
    elif room_dict[room] != 0:
        room_dict[room] = find_room(room_dict, room_dict[room])
        return room_dict[room]
    
def solution(k, room_number):
    room_dict = defaultdict(lambda : 0)
    result = []
    for room in room_number:
        result.append(find_room(room_dict, room))
    return result