def solution(book_time):
    book_time.sort()
    hotel_room = []

    for N, M in book_time:
        after = int(N[0:2]) * 60 + int(N[-2:])
        before = int(M[0:2]) * 60 + int(M[-2:])

        for i in range(len(hotel_room)):
            if hotel_room[i] <= after:
                hotel_room[i] = before + 10
                before = 0
                break

        if before:
            hotel_room.append(before + 10)
    return len(hotel_room)