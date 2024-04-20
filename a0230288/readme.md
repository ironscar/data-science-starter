# Data Science Starter (a0230288)

## Machine Learning Framework

- data collection
- data modelling (iterative)
  - problem definition - what are we trying to solve
    - will simple code work and if so, don't use ML
    - if ML, figure out if the problem you have is supervised, unsupervised, transfer or reinforcement learning
    - if supervised, you have pre-existing labels and includes classification and regression
    - if unsupervised, you dont have pre-existing labels and includes clustering
    - if transfer, use a pre-existing model to train a new model without incurring the full training cost
    - if reinforcement, have a scoring system for each action taken by the model
  - data - what kind of data do we have
    - structured (tabular) or unstructured (image/audio/video)
    - static (doesn't change) or streaming (keeps updating)
  - evaluation - what is success for us
    - accuracy, precision, recall are common classification metrics
    - mean absolute error, mean square error are common regression metrics
  - features - what are the features of the data
    - Numerical or categorical features
    - Deriving features from existing features is called feature engineering
  - modelling - what ML model should be used
    - data splitting refers to splittiing data set into training (70%), validation (15%) and test (15%) sets
    - then we choose a pre-existing model and train it on training data
      - random forest and gradient boosting models work best for structured data
      - deep and transfer learning models work best for unstructured data
    - then we tune a model on the validation data (includes hyperparameter optimization)
      - random forest allows tuning the number of trees
      - neural netwoks allow tuning the number of layers
    - then we test the model to evaluate it on the test data
      - we can do this for multipe models and compare those to find the best one
      - models need to have been trained and then tested on same sets of training and test data
      - compare on training time / prediction time in addition to the evaluation critirea
    - evaluate models and address overfitting/underfitting which can happen due to incorrect data splitting and mismatch respectively
      - we can address underfitting by trying an advanced model, reduce features, train longer or increase model hyperparameters
      - we can address overfitting by trying a less-advanced model or collect more data
  - experimentation - how to improve and what to use next
- deployment

---

## Tools

- Basic setup needs `Python` (which is cpython, there are others like jython, pypy and ironpython as well)
- To write code, we use `Jupyter` notebooks
- data analysis needs `pandas` and `numpy`
- data visualization needs `matplotlib`
- modelling needs `TensorFlow`, `PyTorch` and `ScikitLearn`

---

## Python basics

- To run python scripts, we can create a file `{filename}.py` and run it by `py {filename}.py`
- We are going to be using Python 3.10.2

---

## References

- ML Playground: https://ml-playground.com/
- Teach ML Project: https://teachablemachine.withgoogle.com/train

---
