10x10 사이즈의 그래프에서 이동 한 선이 처음일 경우 answer+1 하는문제

처음에 문제를 제대로 읽지못해서 모든 방향으로 처음 갈때 다 더해주는줄 알았다. 알고보니 그 선을 처음 지날 경우에만 더하는 문제였다

defaultdict에 간 방향을 문자열로 담는다 [좌우인가 상하인가]
모두 담겼으면 리스트로 변환후 set함수로 중복제거후 길이만큼 answer에 더하면된다