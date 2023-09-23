def solution(record):
    user_id = {}
    user_visit = []
    user_history = []
    
    for i in record:
        user = i.split()
        if user[0] != "Change":
            user_visit.append([user[0], user[1]])
        if user[0] != "Leave":
            user_id[user[1]] = user[2]
    
    for stat, user in user_visit:
        if stat == 'Enter':
            user_history.append(f"{user_id[user]}님이 들어왔습니다.")
        else :
            user_history.append(f"{user_id[user]}님이 나갔습니다.")
    return(user_history)