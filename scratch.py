report =  {'Random Forest': 0.8554361392492238, 'Decision Tree': 0.7490737179171063, 'Gradient Boosting': 0.8724122142081709, 'Linear Regression': 0.8796442012440289, 'XGBRegressor': 0.8230898008444014, 'CatBoosting Regressor': 0.8523560006768236, 'AdaBoost Regressor': 0.8414273671068674}
best_model_score = max(sorted(report.values()))
print(best_model_score)
print(list(report.keys())[3])
#print(list(report.keys())[                list(report.values()).index(best_model_score)            ])