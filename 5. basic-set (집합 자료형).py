set 집합 자료형을 공부해 보자

집랍(set)은 집랍에 관련된 것을 쉽게 처리하기 위해 만든 자료형이다.

집합 자료형 만들기
집합 자료형은 다음과 같이 set 키워드를 사용해 만들 수 있다.
py = set([1,2,3])
py
{1,2,3}
위와 같이 set()의 괄호 안에 리스트를 입력하여 만들거나 다음과 같이 문자열을 입력하여 만들 수도 있다.

py_2 = set("Hello")
py_2
{'e','h','l','o'}
비어 있는 집합 자료형은 py = set()로 만들 수 있다

# 집합 자료형의 특징
그런데 위에서 살펴본 set("Hello")의 결과가 좀 이상하지 않은가? 분명 "Hello" 문자열로 set 자료형을 만들었는데 생성된 자료형에는 l 문자가 하나 빠져 있고 순서도 뒤죽박죽이다.
그 이유는 set에 다음과 같은 2가지 특징이 있기 때문이다.


중복을 허용하지 않는다.
순서가 없다(Unordered).
set은 중복을 허용하지 않는 특징 때문에 데이터의 중복을 제거하기 위한 필터로 종종 사용된다.

리스트나 튜플은 순서가 있기(ordered) 때문에 인덱싱을 통해 요솟값을 얻을 수 있지만, set 자료형은 순서가 없기(unordered) 때문에 인덱싱을 통해 요솟값을 얻을 수 없다. 
이는 마치 전에 살펴본 딕셔너리와 비슷하다. 딕셔너리 역시 순서가 없는 자료형이므로 인덱싱을 지원하지 않는다.

만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한 후에 해야 한다,

>>> py = set([1, 2, 3])
>>> py_1 = list(s1)
>>> py_1
[1, 2, 3]
>>> py_1[0]
1
>>> py = tuple(s1)
>>> py
(1, 2, 3)
>>> py[0]
1

#교집합,합집합,차집합 구하기
set 자료형을 정말 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때이다.
먼저 다음과 같이 2개의 set자료형을 만든 후 따라 해 보자. py에는 1부터 6까지의 값, py_1은 4부터 9까지의 값을 주었다.
py = set([1,2,3,4,5,6])
py_1 = set([4,5,6,7,8,9])

교집합 구하기
py와 py_1의 교집합을 구해 보자. 다음과 같이 '&"를 이용하면 교집합을 간단히 구할 수 있다.
py & py_1
{4,5,6}
또는 다음과 같이 intersection 함수를 사용해도 결과는 동일하다.

py.intersection(s2)
{4, 5, 6}

#합집합 구하기
이번에는 합집합을 구해 보자. ‘|’를 사용하면 합집합을 구할 수 있다. 이때 4, 5, 6처럼 중복해서 포함된 값은 1개씩만 표현된다.

py|py_1
{1,2,3,4,5,6,7,8,9}
union 함수를 사용해도 된다.

py.union(py_1)
py_1.union(py)을 사용해도 결과는 동일하다.

차집합 구하기
마지막으로 차집합을 구해 보자. -(빼기)를 사용하면 차집합을 구할 수 있다.
py-py_1
{1,2,3}
py_1-py
{8,9,7}
difference 함수를 사용해도 차집합을 구할 수 있다.
py.difference(s2)
{1, 2, 3}
py_1.difference(s1)
{8, 9, 7}

# 집합 자료형 관련 함수
값 1개 추가하기 - add
이미 만들어진 set자료형에 값을 추가할 수 있다. 1개의 값만 추가 add할 떄는 다음과 같이 하면 된다.

# 값 여러 개 추가하기 - update
여러 개의 값을 한꺼번에 추가(update)할 떄는 다음과 같이 하면 된다.
py = set([1, 2, 3])
py.update([4, 5, 6])
py
{1, 2, 3, 4, 5, 6}

특정 값 제거하기 - remove
특정 갑을 제거하고 싶을 때는 다음과 같이 하면 된다.
py = set([1, 2, 3])
py.remove(2)
py
{1, 3}







