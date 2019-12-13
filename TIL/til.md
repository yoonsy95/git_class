# 마크다운 기초 문법

## 1. heading

제목은 #을 통해 가능함

제목 레벨: h1 ~ h6



# heading1

## heading2

### heading3

#### heading4

##### heading5

###### heading6

content



## 2. 목록

*을 통해 순서가 없는 목록을 작성할 수 있음

1. 을 통해 순서가 있는 목록을 작성할 수 있음

   

* 순서 없는 목록

* 목록 내용

  * tab:  next level
  * enter

  enter

* enter

enter // out list



1. 순서 있는 목록
2. 2nd

enter // out list



## 3. 인용문

\>를 통하여 인용문 작성할 수 있음

> 인용문 작성됨



## 4. 코드블럭

```python
# python에서 주석
print('hi')
def foo():
    print('hi')
```

```sql
-- sql command
```

``` js
//js command
```



## 5. link

이동: ctrl + click

[google](https://google.com)

[use markdown](https://gist.github.com/ihoneymon/652be052a0727ad59601)



## 6. img

drag + drop

![ANIMAL_96906_1502597587](imgs/ANIMAL_96906_1502597587.jpg)

![알파카에 대한 이미지 검색결과](imgs/_(41).jpeg)



- typora에서 이미지 호출시 github에서도 이미지 개지지 않게하기 위하여 아래와 같은 설정함

  - 파일 > 환경설정 > 이미지

    '특별한 동작 없음' -> `copy image to custom colder`

    ​		`./imgs`로 설정하면 해당 마크다운이 있는 폴더내의 `img` 폴더에 이미지 복사함

    체크박스에 아래 3개 모두 체크

    ​		로컬 이미지에 위 규칙을 적용

    ​		온라인 이미지에 위 규칙을 적용

    ​		가능하다면 상대적 경로 사용



## 7. 표

| no   | name   |
| ---- | ------ |
| 1    | 원주성 |
| 2    | 최정민 |



## 8.  기타

수직선(---)

---

*이텔릭체(기울임체)*

**bold**

~~cancel line~~





