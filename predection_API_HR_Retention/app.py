import numpy as np
#need to 'conda install flask' for this to work
from flask import Flask, abort, jsonify, request
import pickle


my_random_forest = pickle.load(open("hr_data_ml.pkl", "rb"))

app = Flask(__name__)

@app.route('/', methods=['POST'])
def make_predict():
    #all kinds of error checking should go here
    data = request.get_json(force=True)
    #convert our json to a numpy array
    predict_request = [data['nu'],data['ps1'],data['ps2'],data['ps3'],data['pm1'],data['pm2'],data['pm3'],data['sal'],data['p']] 
    predict_request = np.array(predict_request).reshape(1,-1)
    #np array goes into random forest, prediction comes out
    y_hat = my_random_forest.predict(predict_request)
    #return our prediction
    output = {'min_months_time_span': y_hat[0]*60}
    print(output)
    return jsonify(results=output)

if __name__ == '__main__':
    app.run()



