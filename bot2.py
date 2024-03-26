# prediction function
#def ValuePredictor(to_predict_list):
#	to_predict = np.array(to_predict_list).reshape(1, 12)
#	loaded_model = pickle.load(open("model.pkl", "rb"))
#	result = loaded_model.predict(to_predict)
#	return result[0]

#@app.route('/result', methods = ['POST'])
#def result():
#	if request.method == 'POST':
#		to_predict_list = request.form.to_dict()
#		to_predict_list = list(to_predict_list.values())
#		to_predict_list = list(map(int, to_predict_list))
#		result = ValuePredictor(to_predict_list)	 
#		if int(result)== 1:
#			prediction ='Income more than 50K'
#		else:
#			prediction ='Income less that 50K'		
#		return render_template("result.html", prediction = prediction)
# backend.py (Flask example)
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive data and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Assuming JSON data is sent from frontend
    # Use data to make predictions with your LSTM model
    prediction = predict_with_lstm(data)
    return jsonify({'prediction': prediction})

# Function to make predictions using LSTM model
def predict_with_lstm(data):
    # Your LSTM model code here
    # This is just a placeholder
    return 'Some prediction'

if __name__ == '__main__':
    app.run(debug=True)
