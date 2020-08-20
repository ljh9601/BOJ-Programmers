# LV1. 정렬 - K번째수



![](/Users/Janghaeng/Desktop/ljh9601.github.io/assets/img/K번째수.png)

이 문제는 설명할 게 그리 많지 않다. <br>

1. array를 i~j까지 slicing
2. slicing한 배열을 sort
3. k번째 원소를 return

<br> 하면 된다. Array 배열의 길이가 100 이하이므로 for문을 통해 돌면 된다. <br>하지만 길이가 수억이 될 때를 대비해 이진탐색을 통해 구현했다.<br><br>

코드를 첨부하고 포스팅을 마치도록 하겠다.

```python
def bsearch(left, right, kth):
    while left <= right :
        mid = (left + right) // 2
        if mid == kth :
            return newArr[mid]
        elif mid < kth :
            left = mid + 1
        else :
            right = mid - 1
    return -1

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start, end, kth = commands[i]
        newArr = array[start-1:end]
        newArr.sort()
        left = 0
        right = end - start
        answer.append(newArr[kth-1])
        
    return answer
```

<br>

[K번째수 Github에서 보기](https://github.com/ljh9601/BOJ-Programmers/blob/master/Programmers/Lv1/K번째%20수.py)