from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('linear_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate_user_info', methods=['POST'])
def validate_user_info():
    try:
        # Get form data
        age = int(request.form['age'])
        gender = request.form['gender']
        ethnicity = request.form['ethnicity']
        parent_education = request.form['parent_education']
        study_time = request.form['study_time']
        absences = int(request.form['absences'])
        tutoring = request.form['tutoring']
        parental_support = request.form['parental_support']
        extracurricular = request.form['extracurricular']
        sports = request.form['sports']
        music = request.form['music']
        volunteering = request.form['volunteering']

        # Perform additional validation if needed
        if age not in [15, 16, 17, 18]:
            raise ValueError("Invalid age")
        # if age <= 0 or study_time < 0 or absences < 0:
        #     raise ValueError("Invalid input values")

        # Convert categorical inputs to numerical values (if necessary)
        gender = 1 if gender == 'female' else 0
        ethnicity = {'caucasian': 0, 'african-american': 1, 'asian': 2, 'other': 3}.get(ethnicity, -1)
        parent_education = {'none': 0, 'high-school': 1, 'some-college': 2, 'bachelors': 3, 'higher': 4}.get(parent_education, -1)
        tutoring = 1 if tutoring == 'true' else 0
        parental_support = {'none': 0, 'low': 1, 'moderate': 2, 'high': 3, 'very high': 4}.get(parental_support, -1)
        extracurricular = 1 if extracurricular == 'true' else 0
        sports = 1 if sports == 'true' else 0
        music = 1 if music == 'true' else 0
        volunteering = 1 if volunteering == 'true' else 0

        # Prepare input data for prediction
        input_data = np.array([[age, gender, ethnicity, parent_education, study_time, absences,
                                tutoring, parental_support, extracurricular, sports, music, volunteering]])
        
        # Scale the input data
        input_data_scaled = scaler.transform(input_data)

        # Predict GPA using the model
        predicted_gpa = model.predict(input_data_scaled)[0]

        # Return success response with prediction
        return jsonify({'valid': True, 'predicted_gpa': predicted_gpa})

    except (KeyError, ValueError) as e:
        return jsonify({'valid': False, 'message': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
