리스트를 두개로 나눴을때 서로다른 숫자가 같은수로 나눠지는 경우의수를 맞추는 문제

리스트 [1, 2, 1, 3, 1, 4, 1, 2] 는 [1, 2, 1, 3], [1, 4, 1, 2]  또는 [1, 2, 1, 3, 1], [4, 1, 2] 이 두가지로 나눌때
서로다른 숫자가 똑같이 나뉘어진다

리스트의 길이가 100만이라 하나하나 세는것은 시간초과
하나의 딕셔너리는 리스트를 저장하고

1번 딕셔너리는 리스트 순서대로 숫자를 제거해나가며 2번 딕셔너리에 담아준다

만약 1번딕셔너리와 2번딕셔너리의 서로다른 숫자의 수가 일치하면그때부터 answer + 1

마지막에 리턴