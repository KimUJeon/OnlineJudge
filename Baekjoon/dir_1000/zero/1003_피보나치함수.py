import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())

    zero = [1, 0]
    one = [0, 1]

    for _ in range(2, x+1):
        zero.append(one[-1])
        one.append(one[-1] + zero[-2])

    print(zero[x], one[x])

'''
어떻게 풀면 좋을지 고민하다가 0과 1이 발생하는데 있어 규칙성을 발견
https://night-knight.tistory.com/entry/%EB%B0%B1%EC%A4%801003-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%ED%95%A8%EC%88%98-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
다만 규칙성을 가지고 풀이할 방법이 떠오르지 않아 해당 블로그에서 동일한 규칙성을 가지고 풀이하는 것을 참고함
생각보다 간단한 문제
'''