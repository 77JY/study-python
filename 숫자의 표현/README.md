# 풀어본 방식

숫자의 표현
이중와일문으로 탐색 <- 진짜싫었음 이 방식은 진짜 싫었는데 많이 배우지 못한 나의 한계였음 ..
그나마 최적화 시킬려면 이제 2n + 1의 값이 매개변수의 값보다 커졌을때 조건을 중지시키는 방법이 나의 최선이였던게 너무 슬픔 ..

# 풀면서 생긴 문제

그냥 완전 반목탐색으로만 풀어버려서 풀리긴 했다 ..

# 해결방법

# 문제를 풀면서 느낀점

내가 몰랐었던 신기한 조건이 존재했다 ..
홀수 숫자의 경우 짝수로 나누었을때 나머지가 0 이면 , 짝수의 경우 홀수로 나누었을때 0이되면 위의 조건과 똑같이 성립된다 ..

남의코드 :
def expressions(num):
return len([i for i in range(1,num+1,2) if num % i is 0])
???
가독할수 있게 해석 :
def count_divisible_odd_numbers(num):
divisible_odd_count = 0

    for i in range(1, num + 1):
        if i % 2 == 1 and num % i == 0:
            divisible_odd_count += 1

    return divisible_odd_count
