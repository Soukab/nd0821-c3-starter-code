# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- This model is created for the ML DevOps Nanodegree from Udacity
- Created on 03/03/2022
- Version 1.0
- We used a Random Forest Classifier in this project
- For more information about the model, please refer to Udacity Nanodegree program

## Intended Use
- This project is intended to show an example of deploying a Scalable ML Pipeline in Production
- Predict whether income exceeds $50K/yr based on census data

## Training Data
We have used 80% of the original dataset for the training purposes of the model.

## Evaluation Data
We have used 20% of the original dataset for evaluation purposes of the model.

## Metrics
We have used three metrics in this project; fbeta_score, precision_score and recall_score.
Precision: 0.784
Recall:0.623
fbeta:0.694

## Ethical Considerations
- The app is intended for learning purposes and a simple model was utilized. No new information is to be inferred or business decisions to be made.

- It is ,however, worth commenting on model fairness when the above metrics were computed on a given categorical 
  variable when its value is held fixed. Without loss of generality, considering category variable for
  example sex and race

## Caveats and Recommendations
- More feature engineering is worth exploring 
- More data would also help train the model even better, for example adding the company's name, size etc
