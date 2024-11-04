딕셔너리를 공부해보자!

사람은 누구든지 "이름" = "홍길동", "생일" = "몇 월 며칠" 등과 같은 방식으로 그 사람이 가진 정보를 나타낼 수 있다.
파이썬은 영리하게도 이러한 대응 관계를 나타낼 수 있는 딕셔너리(dictionary) 자료형을 가지고 있다. 
이번에는 이 자료형에 대해 알아보자.

요즘 사용하는 대부분의 언어도 이러한 대응 관계를 나타내는 자료형을 가지고 있는데 이를 딕셔너리라고 하고, 
‘연관 배열(associative array)’또는 ‘해시(hash)’라고도 한다.

딕셔너리는 단어 그대로 ‘사전’이라는 뜻이다. 즉 "people"이라는 단어에 "사람", "baseball"이라는 단어에
"야구"라는 뜻이 부합되듯이 딕셔너리는 Key와 Value를 한 쌍으로 가지는 자료형이다. 
예컨대 Key가 "baseball"이라면 Value는 "야구"가 될 것이다.

딕셔너리는 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다. 
이것이 바로 딕셔너리의 가장 큰 특징이다. baseball이라는 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 
모두 검색하는 것이 아니라 baseball이라는 단어가 있는 곳만 펼쳐 보는 것이다.

딕셔너리의 기본 모습.
{Key1: Value1, Key2: Value2, Key3: Value3, ...}
Key와 Value의 쌍 여러 개가 {}로 둘러싸여 있다. 각각의 요소는 Key: Value 형태로 이루어져 있고 쉼표(,)로 구분되어 있다.

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
위에서 Key는 각각 'name', 'phone', 'birth', 각각의 Key에 해당하는 Value는 
'pey', '010-9999-1234', '1118'이 된다.

위의 딕셔너리 dic의 정보
key   ㅣ value
name  ㅣ pey
phone ㅣ 010-9999-1234
birth ㅣ 1118
key로 정숫값 1,value로 문자열 'hi'를 사용한 예이다.

py = {1:"hi")
또한 다음 예처럼 Value에 리스트도 넣을 수 있다.
py = {'a':[1,2,3]}

#닥셔너리 쌍 추가, 삭제하기 
딕셔너리 쌍을 추가 또는 삭제하는 방법을 살펴보자, 먼저 딕셔너리에 쌍을 추가해 보자.

딕셔너리 쌍 추가하기
py = {1:'a'}
py[2] = 'b'
py
{1:'a',2:'b'}
{1: 'a'} 딕셔너리에 a[2] = 'b'와 같이 입력하면
딕셔너리 py에 Key와 Value가 각각 2와 'b'인 {2: 'b'} 딕셔너리 쌍이 추가된다.

py['name'] = 'pey'
py
{1:'a',2:'b','name':'pey'}
딕셔너리 py에 {'name':'pey'}

py[3] = [1,2,3]
py
{1:'a',2:'b','name':'pey',3:[1,2,3]}
key는 3, Value는 [1,2,3]을 가지는 한 쌍이 또 추가되었다.

딕셔너리 요소 삭제하기
del py[1]
py
{2:'b','name':'pey',3:[1,2,3]}

#딕셔너리를 사용하는 방법
‘딕셔너리는 주로 어떤 것을 표현하는 데 사용할까?’라는 의문이 들 것이다. 
예를 들어 4명의 사람이 있다고 가정하고 각자의 특기를 표현할 수 있는 좋은 방법에 대해서 생각해 보자. 
리스트나 문자열로는 표현하기가 매우 까다로울 것이다. 
하지만 파이썬의 딕셔너리를 사용하면 이 상황을 표현하기가 정말 쉽다.

{"김연아": "피겨스케이팅", "류현진": "야구", "손흥민": "축구", "박서진": "파이썬"}
사람 이름과 특기를 한쌍으로 묶은 딕셔너리이다. 정말 간편하지 않는가?

#딕셔너리에서 key를 사용해 Value 얻기
python = {'pey': 10, 'julliet': 99}
python['pey']
10
python['julliet']
99
리스트나 튜플, 문자열은 요솟값을 얻고자 할 때 인덱싱이나 슬라이싱 기법 중 하나를 사용했다. 하지만 딕셔너리는 단 1가지 방법뿐이다. 
그것은 바로 Key를 사용해서 Value를 구하는 방법이다. 
위 예에서 'pey'라는 Key의 Value를 얻기 위해 python['pey']를 사용한 것처럼 어떤 Key의 Value를 얻기 위해서는 '딕셔너리_변수_이름[Key]'를 사용해야 한다.

몇 가지 예를 더 살펴보자
py = {1:'a',2:'b'}
py[1]
'a'
py[2]
'b'
먼저 py 변수에 {1: 'a', 2: 'b'} 딕셔너리를 대입하였다. 위 예에서 볼 수 있듯이 py[1]은 'a' 값을 리턴한다. 
여기에서 py[1]이 의미하는 것은 리스트나 튜플의 py[1]과는 전혀 다르다. 딕셔너리 변수에서 [] 안의 숫자 1은 두 번째 요소를 나타내는 것이 아니라 Key에 해당하는 1을 나타낸다.
앞에서도 말했듯이 딕셔너리는 리스트나 튜플에 있는 인덱싱 방법을 적용할 수 없다. 따라서 py[1]은 딕셔너리 {1: 'a', 2: 'b'}에서 Key가 1인 것의 Value인 'a'를 리턴한다. 
py[2] 역시 마찬가지이다.
이번에는 a라는 변수에 앞의 예에서 사용한 딕셔너리의 Key와 Value를 뒤집어 놓은 딕셔너리를 대입해 보자.
>>> py = {'a': 1, 'b': 2}
>>> py['a']
1
>>> py['b']
2
역시 py['a'], py['b']처럼 Key를 사용해서 Value를 얻을 수 있다. 
정리하면, 딕셔너리 py는 py[Key]로 Key에 해당하는 Value를 얻는다.

다음 예는 이전에 한 번 언급한 딕셔너리인데, Key를 사용해서 Value를 얻는 방법을 잘 보여 준다.

dic = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
dic['name']
'pey'
dic['phone']
'010-9999-1234'
dic['birth']
'1118'

# 딕셔너리 만들 때 주의할 사항
딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점에 주의해야 한다. 
다음 예에서 볼 수 있듯이 동일한 Key가 2개 존재할 경우, 1: 'a' 쌍이 무시된다.

py = {1:'a',1:'b')
py
{1:'b'}

이렇게 Key가 중복되었을 때 1개를 제외한 나머지 Key: Value 값이 모두 무시되는 이유는 Key를 통해서 Value를 얻는 딕셔너리의 특징 때문이다. 
즉, 딕셔너리에는 동일한 Key가 중복으로 존재할 수 없다.

또 1가지 주의해야 할 점은 Key에 리스트는 쓸 수 없다는 것이다. 하지만 튜플은 Key로 쓸 수 있다. 
딕셔너리의 Key로 쓸 수 있느냐, 없느냐는 Key가 변하는(mutable) 값인지, 변하지 않는(immutable) 값인지에 달려 있다. 
리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다.
다음 예처럼 리스트를 Key로 설정하면 리스트를 키 값으로 사용할 수 없다는 오류가 발생한다.

py = {[1,2] : 'hi'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
단, Value에는 변하는 값이든, 변하지 않는 값이든 아무 값이나 넣을 수 있다.

딕셔너리 관련 함수
딕셔너리를 자유자재로 사용하기 위해 딕셔너리가 자체적으로 가지고 있는 관련 함수를 사용해 보자.

key 리스트 만들기 -keys
py = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
py.keys()
dict_keys(['name', 'phone', 'birth'])
py.keys()는 딕셔너리 py의 key만을 모아 dict_keys 객체를 리턴한다.

dict_keys 객체는 다음과 같이 사용할 수 있다. 리스트를 사용하는 것과 별 차이는 없지만, 
리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.

>>> for i in py.keys():
...    print(i)
...
name
phone
birth
print(k)를 입력할 때 들여쓰기를 하지 않으면 오류가 발생하므로 주의하자.
for 문 등 반복 구문에 대해서는 03장에서 자세히 살펴본다.

dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
list(py.keys())
['name','phone','birth']

Value 리스트 만들기 - values 
py.values()
dict_values(['pey','010-9999-1234','1118'])
key를 얻는 것과 마찬가지 방법으로 Value만 얻고 싶다면 values 함수를 사용하면 된다. values 함수를 호출하면 dict_values 객체를 리턴한다.

key,Value 쌍 얻기 - items
py.items()
dict_items([('name','pey'),('phone','010-9999-1234'),('birth','1118')])
items 함수는 key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴한다.

key: Value 쌍 모두 지우기 - clear
py.clear()
py
{}
clear 함수는 딕셔너리 안의 모든 요소를 삭제한다,
빈 리스트를 [], 빈 튜플을 ()로 표현하는 것과 마찬가지로 빈 딕셔너리도 {}로 표현한다.

key로 Value얻기 - get
py = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
py.get('name')
'pey'
py.get('phone')
'010-9999-1234'
get(x) 함수는 x라는 Key에 대응되는 Value를 리턴한다. 앞에서 살펴보았듯이 a.get('name')은 a['name']을 사용했을 때와 동일한 결괏값을 리턴한다.

다만, 다음 예제에서 볼 수 있듯이 a['nokey']처럼 딕셔너리에 존재하지 않는 키로 값을 가져오려고 할 경우, 
a['nokey'] 방식은 오류를 발생시키고 a.get('nokey') 방식은 None을 리턴한다는 차이가 있다. 어떤 것을 사용할 것인지는 여러분의 선택에 달려 있다.

여기에서 None은 ‘거짓’이라는 뜻이라고만 알아 두자.

py = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(py.get('nokey'))
None
print(py['nokey’])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'nokey'
딕셔너리 안에 찾으려는 Key가 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때는 get(x,'디폴트 값')을 사용하면 편리하다.

py.get('nokey','foo')'
'foo'
딕셔너리 py에는 'nokey'에 해당하는 key가 없다. 따라서 디폴트 값인 'foo'를 리턴한다.

해당 key가 딕셔너리 안에 있는지 조사하기 - in 
py = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
'name' in py
True
'email' in py
False
'name' 문자열은 a 딕셔너리의 Key 중 하나이다. 따라서 'name' in a를 호출하면 참(True)을 리턴한다. 
이와 반대로 'email'은 a 딕셔너리 안에 존재하지 않는 Key이므로 거짓(False)을 리턴한다.








