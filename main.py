# Importing necessary modules
from flask import Flask, request, jsonify
import data_processing as dp
import model as mdl
import nlp
import ehr_integration as ehr
import user_interface as ui
import security as sec

app = Flask(__name__)

@app.route('/')
def home():
    return ui.home()

@app.route('/api/v1/health_check', methods=['POST'])
def health_check():
    data = request.get_json()
    sec.validate_request(data)
    processed_data = dp.process_data(data)
    prediction = mdl.predict(processed_data)
    response = nlp.generate_response(prediction)
    return jsonify(response)

@app.route('/api/v1/ehr_integration', methods=['POST'])
def ehr_integration():
    data = request.get_json()
    sec.validate_request(data)
    ehr_data = ehr.get_ehr_data(data)
    return jsonify(ehr_data)

@app.route('/api/v1/medication_reminder', methods=['POST'])
def medication_reminder():
    data = request.get_json()
    sec.validate_request(data)
    reminder = ui.set_reminder(data)
    return jsonify(reminder)

@app.route('/api/v1/diet_exercise', methods=['POST'])
def diet_exercise():
    data = request.get_json()
    sec.validate_request(data)
    diet_plan, exercise_routine = ui.get_diet_exercise(data)
    return jsonify({'diet_plan': diet_plan, 'exercise_routine': exercise_routine})

@app.route('/api/v1/telehealth', methods=['POST'])
def telehealth():
    data = request.get_json()
    sec.validate_request(data)
    appointment = ui.schedule_appointment(data)
    return jsonify(appointment)

@app.route('/api/v1/education', methods=['POST'])
def education():
    data = request.get_json()
    sec.validate_request(data)
    educational_content = ui.get_educational_content(data)
    return jsonify(educational_content)

if __name__ == '__main__':
    app.run(debug=True)
