# Student Performance Prediction System

## Overview

This project is a **Student Performance Prediction System** that predicts whether a student will pass or fail based on various academic and personal features. The system uses machine learning with Support Vector Classifier (SVC) and provides a Flask web application for easy user interaction.

## Features

* Predict Pass/Fail for individual students.
* User-friendly web interface using Flask.
* Handles missing values and categorical data automatically.
* Saves trained model using Pickle for reuse.

## Dataset

* The dataset contains student details such as Study Hours, Attendance, Past Exam Scores, Parental Education Level, Internet Access, Extracurricular Activities, and Final Exam Score.
* Target variable: `Pass_Fail` (1 = Pass, 0 = Fail).

## Installation

1. Clone the repository.
2. Install required Python libraries:

```bash
pip install pandas numpy scikit-learn flask
```

3. Place `student_performance_dataset.csv` in the project folder.

## Usage

1. Run the data preprocessing and model training script to create `pass_fail_model.pkl`:

```bash
python app.py
```

2. Run the Flask application:

```bash
python app.py
```

3. Open a web browser and go to `http://127.0.0.1:5000/`.
4. Fill in the student details and click **Submit** to get the prediction.

## Folder Structure

```
Student_Performance_Prediction/
│
├── processed_data.csv
├── student_performance_dataset.csv
├── pass_fail_model.pkl
├── app.py
├── templates/
│   └── index.html
└── README.md
```

## Future Enhancements

* Add data visualization for student performance.
* Add authentication for teachers/admin.
* Batch prediction by uploading CSV files.
* Improve model accuracy using advanced ML algorithms like Random Forest or XGBoost.

## References

* [Scikit-learn Documentation](https://scikit-learn.org/)
* [Flask Documentation](https://flask.palletsprojects.com/)
* [Pandas Documentation](https://pandas.pydata.org/)
