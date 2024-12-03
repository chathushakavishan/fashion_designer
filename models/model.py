import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.svm import SVC
from scipy.stats import uniform

# Load the dataset
df = pd.read_csv('fashion_data.csv')  

# Preview the dataset
print(df.head())

# Separate features and target
X = df[['Comfort', 'Fit & Sizing', 'Preferred Pieces', 'Design & Style', 'Material Quality']]
y = df['Fashion Type']

# Encode the target variable
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Define categorical and numerical columns
categorical_cols = ['Preferred Pieces', 'Design & Style', 'Material Quality']
numerical_cols = ['Comfort', 'Fit & Sizing']

# Preprocessing for numerical data
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Function to perform hyperparameter tuning and evaluation
def evaluate_model(model, param_distributions):
    clf = Pipeline(steps=[('preprocessor', preprocessor),
                          ('classifier', model)])
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    # Hyperparameter tuning using RandomizedSearchCV
    random_search = RandomizedSearchCV(clf, param_distributions, n_iter=50, cv=5, scoring='accuracy', n_jobs=-1, random_state=42)
    random_search.fit(X_train, y_train)

    # Print best parameters and score
    print("Best parameters found: ", random_search.best_params_)
    print("Best cross-validation accuracy: {:.2f}".format(random_search.best_score_))

    # Make predictions
    y_pred = random_search.predict(X_test)

    # Evaluate the model
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    return random_search.best_estimator_

# Define SVM model and hyperparameter space
svm_model = SVC()
svm_param_distributions = {
    'classifier__C': uniform(0.1, 10),
    'classifier__gamma': uniform(0.01, 1),
    'classifier__kernel': ['linear', 'rbf', 'poly']
}

print("Evaluating SVM model...")
best_svm = evaluate_model(svm_model, svm_param_distributions)

# Save the pipeline (preprocessor + model)
import joblib
joblib.dump(best_svm, 'fashion_model.pkl')

print("Best SVM model pipeline has been saved.")
