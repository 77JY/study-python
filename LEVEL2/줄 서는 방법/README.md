순열에 관한 문제
숫자 n이 들어올때 1부터 n까지 순서대로 리스트를 만들고 순열로 조합가능한 숫자중 k의 번째에 있는 순열을 리턴하는 문제

n의값이 20인데 20팩토리얼의 값이 너무 커서 순열의 조합을 그대로 만들면 시간이 초과되는 문제
숫자의 순서는 언제나 같기때문에 해당하는 숫자의 위치를 찾기위해선 팩토리얼 계산만 하면 된다
n - 1 의 팩토리얼로 현재 k - 1값을 나눈 값을 리스트에서 찾은뒤 담아주면 된다
