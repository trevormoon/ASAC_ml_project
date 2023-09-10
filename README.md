# STEAM 유저 리뷰 분석을 통한 게임의 성공 여부 예측

## 주제

게임 유통사(STEAM)에서 취합가능한 게임 정보를 활용하여 유저리뷰를 예측하는 알고리즘.

예측한 유저리뷰를 토대로 동일 장르의 게임과 비교하여 게임을 위한 가이드라인 제시

## 추진배경

게임의 매출과 유저의 리뷰 사이의 상관관계가 존재함. 

이에 따라서 게임의 정보를 토대로 유저의 리뷰를 예측할 수 있을 경우 게임의 성공에 대한 간접적 예측이 가능함.

STEAM에 새로 진입하는 게임에 대해서 유저들의 리뷰의 예측을 통해서 게임의 간접적 성공 여부를 확인 가능.

## REPOSITORY 디렉토리 구성

```bash
├── WEB CRAWLING
|   ├── STEAM CRAWLING
|   ├── STEAM CHART CRAWLING
|   ├── STEAM SPY CRAWLING
|   └── CRAWLING DATA
├── EXPLORATORY DATA ANALYSIS
|   ├── DATA CORREALATION
|   ├── DATA OUTLIER
|   ├── CATEGORICAL VARIABLE PREPROCESSING
|   └── VISUALIZATION
├── MACHINE LEARNING
|   ├── TRAINING DATA PREPROCESSING
|   ├── BASE MODEL SELECTION
|   ├── HYPER PARAMETER TUNING
|   └── FINAL MODEL SELECTION
└── GAME REPORT
    └── REPORT
```


## MACHINE LEARNING 모델링 및 학습

### 학습과정 SCHEMATICS
image
![슬라이드21](https://github.com/trevormoon/ASAC_ml_project/assets/126679650/59738f7a-6107-494c-80b4-1fc2e9737ac0)


### 프로젝트 결과물 최종 모델의 성능
image
![슬라이드27](https://github.com/trevormoon/ASAC_ml_project/assets/126679650/ad7a4427-eba9-4400-9e8c-adf17a6bf0c1)

### 예측 지표를 통한 게임 가이드라인 제시
![슬라이드29](https://github.com/trevormoon/ASAC_ml_project/assets/126679650/ddab9d53-a7bc-4f94-841e-3e7314368d47)
