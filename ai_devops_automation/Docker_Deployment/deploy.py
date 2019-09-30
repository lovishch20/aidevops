from sklearn.externals import joblib
import argparse
import flask
import os

# command line arguments
parser = argparse.ArgumentParser(description='Train a model for iris classification.')
#parser.add_argument('inmodeldir', type=str, help='Input directory containing the training set')
args = parser.parse_args()
app = flask.Flask(__name__)
port = int(os.getenv("PORT", 9099))

# attribute column names
#input_datadir =  "ai_devops_automation/output/"
# load the model
mymodel = joblib.load('model.pkl')

# make the inference
@app.route('/predict', methods=['POST'])
def predict():
    features = flask.request.get_json(force=True)['features']
    pred = mymodel.predict([features])
    pred_list = pred.tolist()
    response = {'result': pred_list}
    return flask.jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
