# Script to train machine learning model.

from sklearn.model_selection import train_test_split

# Add the necessary imports for the starter code.
import pandas as pd
from ml.data import process_data
from ml.model import train_model, compute_model_metrics, inference

# Add code to load in the data.
data = pd.read_csv(r"../data/clean_census.csv")

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# Process the test data with the process_data function.
X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)


# Train and save a model.
print(len(X_train[0]))
model = train_model(X_train, y_train)
pd.to_pickle(model, "../model/model.pkl")

# calculate the classification metrics on the entire test set
X_test, y_test, encoder, lb = process_data(
    test, categorical_features=cat_features, label="salary", training=False, encoder=encoder, lb=lb
)
predictions = inference(model, X_test)
precision, recall, fbeta = compute_model_metrics(y_test, predictions)
inf_path = '../model/model.info'
with open(inf_path, 'w') as f:
    f.write('Precision: %.3f\nRecall:%.3f\nfbeta:%.3f' %
            (precision, recall, fbeta))

#Saving the encoder and the LabelBinarizer for being used in the API later
pd.to_pickle(encoder, "../model/encoder.pkl")
pd.to_pickle(lb, "../model/lb.pkl")