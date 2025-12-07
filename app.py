from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model_svc = pickle.load(open('pass_fail_model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        
        Student_ID = int(request.form['Student_ID'])
        Gender = int(request.form['Gender'])
        Study_Hours_per_Week = int(request.form['Study_Hours_per_Week'])
        Attendance_Rate = int(request.form['Attendance_Rate'])
        Past_Exam_Scores = int(request.form['Past_Exam_Scores'])
        Parental_Education_Level = int(request.form['Parental_Education_Level'])
        Internet_Access_at_Home = int(request.form['Internet_Access_at_Home'])
        Extracurricular_Activities = int(request.form['Extracurricular_Activities'])
        Final_Exam_Score = int(request.form['Final_Exam_Score'])

        features = np.array([[Student_ID, Gender, Study_Hours_per_Week,
                              Attendance_Rate, Past_Exam_Scores,
                              Parental_Education_Level,
                              Internet_Access_at_Home,
                              Extracurricular_Activities,
                              Final_Exam_Score]])

       
        prediction = model_svc.predict(features)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
