import numpy as np
import pandas as pd
import pickle
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score, classification_report

# Load model
clf = pickle.load(open('model.pkl', 'rb'))

# Load test data
test_data = pd.read_csv('./data/features/test_bow.csv')
X_test = test_data.iloc[:, :-1].values
y_test = test_data.iloc[:, -1].values

# Predictions
y_pred = clf.predict(X_test)
y_pred_proba = clf.predict_proba(X_test)[:, 1]

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_proba)
class_report = classification_report(y_test, y_pred, output_dict=True)

# Save metrics
metrics_dict = {
    'accuracy': accuracy,
    'precision': precision,
    'recall': recall,
    'auc': auc,
    'classification_report': class_report
}

with open('metrics.json', 'w') as file:
    json.dump(metrics_dict, file, indent=4)
