정말 지저분하게 풀었던문제;
게임의 층수 N층이 존재하고 현재 유저들이 몇층에 있는지 stages안에 주어진다
게임 플레이 유저가 현재 층수를 클리어하지 못했을 확률을 계산하는 문제
확률은 위와 같다 

현재층의 유저 / 현재 층의 유저 + 층수보다 높은 유저수


1.딕셔너리 N개를 미리 담아주고 for문을 돌리면서 해당 번호의 values를 1씩 올려주고 index값을 초과하면 cnt를 올려준다
2.다음 포문에서 딕셔너리를 역순으로 돌리면서 value를 cnt에 넣어준뒤 현재 value / cnt를 해주면 확률 , 반복한다
3.확률을 모두 담아줬으면 딕셔너리를 value순으로 reverse정렬해준다
4.리스트에 딕셔너리의 keys를 순서대로 담아준뒤 리턴