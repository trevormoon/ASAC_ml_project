# 전체 데이터 최종 전처리
- appid : 게임 고유 아이디
- 24_Hour_Peak : 최근 24시간의 최고 동접자 수
- All_time_peak : 출시 이후 최고 동접자 수
- positive : 긍정 리뷰 수
- negative : 부정 리뷰 수
- average_forever : 출시 이후 동접자 수 평균
- average_2weeks : 최근 2주의 동접자 수 평균
- median_forever : 출시 이후 동접자 수 중앙값
- median_2weeks : 최근 2주의 동접자 수 중앙값
- price : 게임 가격
- initialprice : 출시 가격
- genre : 장르
- num_lang : 지원 언어 개수
- required_age : 제한 연령
- is_free : 유/무료 여부
- dlc : 확장판 appid들  
- controller_support : 컨트롤러 지원 여부
- platforms : 지원 OS(windows, mac, linux)
- metacritic : 메타크리틱 점수
- recommendations : 게임 플레이 유저들의 추천 수
- achievements : 도전과제 개수
- Review : 리뷰 등급

  
### **전처리 방식**
**24_Hour_Peak**
- Invalid 값 0으로 대체

**All_time_peak**
- Invalid 값 average_forever값으로 대체

**genre**
- NaN값을 "N"으로 대체 

**Review**
- NaN값을 No user reviews로 대체 

**required_age**

- 한국의 연령 제한 기준에 맞춰 범주화 진행
  - 17세-19세 -> 18세 이용가
  - 14세-16세 -> 15세 이용가
  - 1세-13세 -> 12세 이용가
  - 전체 이용가 

- NaN값은 0(전체이용가)으로 대체 
  
- integer가 아닌 값들 ex) 18+, ALL
  - 18+ -> 18세 이용가
  - ALL -> 전체 이용가
  
**is_free**
- 0,False,True,1 등이 혼재되어 있는 상태에서 0/1로 범주화
  - 유료 게임 : 0
  - 무료 게임 : 1

- NaN값은 steam spy data의 price column과 비교
  - price != 0 -> 0
  - price == 0 -> 1

**dlc**
- 해당 게임의 확장판 게임에 대한 appid들을 dict형태로 제공
  - dict 내 appid 개수를 사용
  - NaN 값은 0으로 대체 

**controller_support**
- full,NaN으로 구성되어 있는 상태에서 0/1로 범주화
  - full -> 1
  - NaN -> 0 
    - 컨트롤러 미지원
  
**platforms**
- OS 이름을 key로 하고 boolean값을 value로 하는 dict 형태에서 OS별로 컬럼 재생성 및 지원 OS 수에 대한 컬럼 추가
- ```
  "platforms": {
        "windows": true,
        "mac": true,
        "linux": false
      }
    ```

- windows|mac|linux|platforms_num
    ---|---|---|---
    1|1|0|2
- NaN 값은 0으로 대체
- 

**metacritic**
- 메타크리틱 점수를 그대로 사용하지 않고 점수 존재 여부에 따라 metacritic_tf 컬럼 생성
  - 점수 존재 -> 1
  - NaN -> 0
  
**recommendations**
- NaN값을 0으로 대체

**achievements**
- NaN값을 0으로 대체




  