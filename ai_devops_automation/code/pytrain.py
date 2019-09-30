import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.externals import joblib
import argparse

import os


# command line arguments
parser = argparse.ArgumentParser(description='Train a model for iris classification.')
args = parser.parse_args()


# training set column names
cols = [
    "Sepal_Length",
    "Sepal_Width",
    "Petal_Length",
    "Petal_Width",
    "Species"
]
features = [
    "Sepal_Length",
    "Sepal_Width",
    "Petal_Length",
    "Petal_Width"
]

input_datadir = "ai_devops_automation/data/"
output_datadir = "ai_devops_automation/output/"

# import the iris training set
irisDF = pd.read_csv(os.path.join(input_datadir, "iris.csv"), names=cols)

# fit the model
lda = LinearDiscriminantAnalysis().fit(irisDF[features], irisDF["Species"])

# output a text description of the model
f = open(os.path.join(output_datadir, 'model.txt'), 'w')
f.write(str(lda))
f.close()

# persist the model
joblib.dump(lda, os.path.join(output_datadir, 'model.pkl'))