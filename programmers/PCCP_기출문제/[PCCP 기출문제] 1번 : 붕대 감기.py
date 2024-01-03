def solution(bandage, health, attacks):
    answer = 0
    success = 0
    init_health = health
    end_time = attacks[-1][0]
    for time in range(1, end_time + 1):
        # 몬스터가 공격하는 경우
        if time == attacks[0][0]:
            health -= attacks[0][1]
            success = 0
            attacks = attacks[1:]
        # 연속 성공 중인경우
        else:
            success += 1
            health += bandage[1]
            # 시전 시간까지 성공한 경우
            if success == bandage[0]:
                success = 0
                health += bandage[2]
            # 최대 채력을 넘어간 경우
            if health > init_health:
                # 체력을 최대 채력으로 낮추기
                health = init_health
        if health <= 0:
            return -1

    return health