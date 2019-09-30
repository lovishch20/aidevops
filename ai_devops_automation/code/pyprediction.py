import pandas as pd
from sklearn import svm
from sklearn import model_selection
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
import argparse

import os

from pandas._libs import json

# command line arguments
parser = argparse.ArgumentParser(description='Train a model for iris classification.')
#parser.add_argument('indir', type=str, help='Input directory containing the training set')
#parser.add_argument('outdir', type=str, help='Output directory for the trained model')
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
metrics_file = "ai_devops_automation/output/eval.txt"
input_datadir = "ai_devops_automation/data/"
output_datadir = "ai_devops_automation/output/"

# import the iris training set
irisDF = pd.read_csv(os.path.join(input_datadir, "iris_test.csv"), names=cols)
mymodel = joblib.load(os.path.join(output_datadir, 'model.pkl')) 


x_train,x_test,y_train,y_test= model_selection.train_test_split(irisDF[features],irisDF["Species"],test_size=.5)
predictions=mymodel.predict(x_test)
#from sklearn.metrics import accuracy_score
auc=(accuracy_score(y_test,predictions))
with open(metrics_file, 'w') as fd:
    fd.write('AUC: {:4f}\n'.format(auc))


