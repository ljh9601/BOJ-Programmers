from collections import deque



def solution(begin, target, words):
    q = deque()
    visited = []
    q.appendleft(begin)
    answer = 0
    while q :
        length = len(q)
        for _ in range(length):
            currentWord = q.popleft()
            if currentWord == target :
                return answer
            for i in range(len(words)):
                if words[i] in visited :
                    continue
                cnt = 0
                for j in range(len(begin)) :
                    if currentWord[j] != words[i][j] :
                        cnt += 1
                if cnt == 1:
                    q.append(words[i])
                    visited.append(words[i])
        answer += 1
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))