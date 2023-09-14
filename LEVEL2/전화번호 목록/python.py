def solution(p_book):
    p_book.sort()
    for i in range(1, len(p_book)):
        if p_book[i].startswith(p_book[i-1]):
            return False
    return True