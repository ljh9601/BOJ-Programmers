

## Lv1. 연습문제 - 문자열 내 p와 y의 개수





![](/assets/img/문자열%20내%20p와%20y의%20개수.png)

이 문제 역시 쉬운 문제다. 바로 로직을 설명해보겠다.

> 
>
> 1. string을 모두 소문자로 바꾼다. (lower 함수 이용)
> 	
> 2. Count 함수를 이용해 p와 y의 개수를 세주고 비교한다!

<br>

소스코드는 다음과 같다.

```python
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
```



<br>

<br>

[문자열 내 마음대로 정렬하기 Github에서 보기](https://github.com/ljh9601/BOJ-Programmers/blob/master/Programmers/Lv1/문자열 내 마음대로 정렬하기.py)

