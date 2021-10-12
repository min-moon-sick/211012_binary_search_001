# 211012_binary_search_001

이진 탐색은 배열 내부의 데이터가 정렬되어야만 사용할 수 있는 알고리즘이다

이진 탐색은 위치를 나타내는 변수 3개를 사용하는데 탐색하고자 하는 범위의 시작점, 끝점, 그리고 중간점이다

찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는다

## 개념 이해

![image](https://user-images.githubusercontent.com/88085974/136873023-6e114941-259c-4ec1-bfb2-5ec5c2d4cdff.png)

인덱스 기준으로 중간 지점을 찾는다.

9/2 = 4.5  이므로 소수점은 버리고 데이터를 확인할 때,

i[4] = 8 을 나타낸다

![image](https://user-images.githubusercontent.com/88085974/136873712-97c476ca-5724-4dea-8b08-b4d6c43fbe43.png)

찾으려는 데이터 4와 비교했을 때 값이 크기 때문에

중간 지점인 i[4]보다 앞의 인덱스인 i[3]을 끝점으로 놓고 다시 중간 지점을 찾는다

3/2 = 1.5  이므로 소수점을 버리고 데이터를 확인할 때,

i[1] = 2 이다.

![image](https://user-images.githubusercontent.com/88085974/136873724-497af4ed-8237-45b1-a711-794adcd97e00.png)

찾으려는 데이터 4와 비교 했을 때 값이 작기 때문에 이때 시작점을 중간 지점인 i[1]보다 뒤에 놓는다

## example code


def binary_search(array, target, start, end):

  if start > end:

    return None

  mid = (start + end ) // 2
  
  if array[mid] == target:

    return mid

  elif array[mid] > target:
    
    return binary_search(array,target,start, mid-1)
  
  else:
    
    return binary_search(array,target,mid+1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split))

result = binary_search(array, target, 0, n-1)

if result == None:
  
  print("원소가 존재하지 않습니다.")
else:
  
  print(result + 1)


## example_001 - 30m

![image](https://user-images.githubusercontent.com/88085974/136877160-24c18564-0c65-45a8-abf4-c843a148d9ae.png)

![image](https://user-images.githubusercontent.com/88085974/136877180-c8f54e61-940c-430e-aa5c-c6646b12efb7.png)

