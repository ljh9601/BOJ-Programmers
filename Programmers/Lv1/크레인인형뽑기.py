def solution(board, moves):
    stack = []
    ans = 0
    for val in moves:
        val -= 1
        for i in range(len(board)):
            if board[i][val] :
                if not stack :
                    stack.append(board[i][val])
                else :
                    if stack[-1] != board[i][val]:
                        stack.append(board[i][val])  
                    else :
                        stack.pop()
                        ans += 2
                board[i][val] = 0
                break
    return ans