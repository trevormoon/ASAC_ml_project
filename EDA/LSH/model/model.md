```
rf
다 넣었을 때
              precision    recall  f1-score   support

           0       0.91      0.87      0.89      5988
           1       0.30      0.61      0.40       963
           2       0.08      0.57      0.14        51
           3       0.91      0.77      0.84      6874

    accuracy                           0.80     13876
   macro avg       0.55      0.71      0.57     13876
weighted avg       0.87      0.80      0.83     13876

태그, posit, nega, reco 제외
              precision    recall  f1-score   support

           0       0.81      0.65      0.72      7144
           1       0.12      0.38      0.18       607
           2       0.04      0.29      0.07        49
           3       0.68      0.65      0.67      6076

    accuracy                           0.64     13876
   macro avg       0.41      0.49      0.41     13876
weighted avg       0.72      0.64      0.67     13876

SMOTE
              precision    recall  f1-score   support

           0       0.77      0.65      0.71      6900
           1       0.65      0.78      0.71      4855
           2       0.92      0.88      0.90      6072
           3       0.62      0.66      0.64      5476

    accuracy                           0.74     23303
   macro avg       0.74      0.75      0.74     23303
weighted avg       0.75      0.74      0.74     23303

SMOTE + tag
              precision    recall  f1-score   support

           0       0.83      0.69      0.75      7076
           1       0.74      0.85      0.79      5066
           2       0.97      0.94      0.96      5971
           3       0.64      0.72      0.68      5190

    accuracy                           0.80     23303
   macro avg       0.80      0.80      0.79     23303
weighted avg       0.80      0.80      0.80     23303
```

```
xgb
다 넣었을 때
              precision    recall  f1-score   support

           0       0.90      0.91      0.91      5668
           1       0.64      0.77      0.70      1629
           2       0.49      0.74      0.59       232
           3       0.93      0.85      0.89      6347

    accuracy                           0.86     13876
   macro avg       0.74      0.82      0.77     13876
weighted avg       0.88      0.86      0.87     13876

태그, posit, nega, reco 제외
              precision    recall  f1-score   support

           0       0.83      0.66      0.73      7238
           1       0.13      0.44      0.20       584
           2       0.04      0.54      0.07        26
           3       0.68      0.66      0.67      6028

    accuracy                           0.65     13876
   macro avg       0.42      0.57      0.42     13876
weighted avg       0.73      0.65      0.68     13876

SMOTE
              precision    recall  f1-score   support

           0       0.80      0.65      0.71      7185
           1       0.52      0.72      0.61      4226
           2       0.85      0.79      0.82      6299
           3       0.64      0.67      0.65      5593

    accuracy                           0.70     23303
   macro avg       0.70      0.71      0.70     23303
weighted avg       0.72      0.70      0.71     23303

SMOTE + tag
              precision    recall  f1-score   support

           0       0.82      0.68      0.74      6953
           1       0.61      0.75      0.67      4802
           2       0.89      0.84      0.87      6137
           3       0.64      0.69      0.67      5411

    accuracy                           0.74     23303
   macro avg       0.74      0.74      0.74     23303
weighted avg       0.75      0.74      0.74     23303
```

```
lgbm
다 넣었을 때
              precision    recall  f1-score   support

           0       0.90      0.91      0.91      5633
           1       0.65      0.77      0.70      1667
           2       0.51      0.75      0.61       236
           3       0.93      0.85      0.89      6340

    accuracy                           0.86     13876
   macro avg       0.75      0.82      0.78     13876
weighted avg       0.87      0.86      0.87     13876

태그, posit, nega, reco 제외
              precision    recall  f1-score   support

           0       0.84      0.65      0.73      7367
           1       0.12      0.50      0.19       471
           2       0.03      0.50      0.06        22
           3       0.68      0.66      0.67      6016

    accuracy                           0.65     13876
   macro avg       0.42      0.58      0.41     13876
weighted avg       0.75      0.65      0.69     13876

SMOTE
              precision    recall  f1-score   support

           0       0.80      0.64      0.71      7328
           1       0.47      0.68      0.55      3980
           2       0.82      0.75      0.78      6316
           3       0.65      0.66      0.65      5679

    accuracy                           0.68     23303
   macro avg       0.68      0.68      0.67     23303
weighted avg       0.71      0.68      0.69     23303

SMOTE + tag
              precision    recall  f1-score   support

           0       0.81      0.69      0.74      6831
           1       0.60      0.73      0.65      4765
           2       0.88      0.83      0.85      6180
           3       0.65      0.69      0.67      5527

    accuracy                           0.73     23303
   macro avg       0.73      0.73      0.73     23303
weighted avg       0.75      0.73      0.74     23303
```