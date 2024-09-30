def stack(li):
    stack = []  # 괄호를 담을 스택 생성

    for i in li:
        if i == '(':  # '('일 때 스택에 추가
            stack.append(i)
        elif i == ')':  # ')'일 때
            if stack:  # 스택이 비어있지 않다면
                stack.pop()  # 짝이 맞으므로 pop
            else:  # 스택이 비어있다면 짝이 맞지 않음
                return "NO"
    
    if not stack:  # 모든 괄호가 짝을 맞췄다면
        return "YES"
    else:  # 스택이 비어있지 않다면 짝이 맞지 않음
        return "NO"

a = int(input())  # 테스트 케이스 개수 입력
for i in range(a):
    l = list(input())  # 문자열을 리스트로 변환하여 입력 받음
    print(stack(l))  # 결과 출력