# 🚢 Titanic Survival Prediction Project

This project is a complete end-to-end **Data Science and Machine Learning solution** using the Titanic dataset. It includes:
- 🧪 Exploratory Data Analysis (EDA)
- 🧠 Machine Learning modeling
- 🌐 A Flask web application to predict passenger survival

---

## 📁 Project Structure

titanic_project/  
├── app.py # Flask backend  
├── model/  
│ └── model.pkl # Trained Random Forest model  
├── templates/  
│ └── index.html # Frontend HTML form  
├── static/  
│ └── style.css  
├── train.csv # Titanic dataset  
├── titanic_colab_eda.ipynb # EDA + Model training notebook  
└── README.md  


---

## 📌 About the Dataset

- **Source**: [Kaggle - Titanic: Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data?select=train.csv)
- **Goal**: Predict whether a passenger survived based on features like age, gender, fare, class, etc.

---

## 📊 EDA & Feature Engineering (Colab)

The notebook performs:

- 🔍 Null value analysis & imputation
- 📈 Distribution plots (Age, Fare, Gender, Pclass)
- 🧠 Feature extraction:
  - `Title` from Name
  - `FamilySize` = `SibSp + Parch`
  - `IsAlone` flag
  - `Deck` from Cabin
- 🔢 Label Encoding (Sex, Embarked, Title, Deck)
- 🔗 Correlation heatmap
- ✅ Logistic Regression & Random Forest models
- 📈 Model Evaluation (accuracy, classification report, confusion matrix)

---

## 🔮 Model Summary

- Best model: **Random Forest Classifier**
- Accuracy: ~82% on test split
- Exported as `model.pkl` for web use

---

## 🌐 Flask Web App

A simple yet effective web interface built using Flask:
- Input passenger details
- Get predicted survival status in real-time

### 🧪 Inputs Required:
| Feature      | Format                    |
|--------------|---------------------------|
| Pclass       | 1 / 2 / 3                 |
| Sex          | 0 = Male, 1 = Female       |
| Age          | Float                     |
| Fare         | Float                     |
| Embarked     | 0 = S, 1 = C, 2 = Q        |
| FamilySize   | Integer                   |
| IsAlone      | 0 / 1                     |
| Title        | Encoded Integer           |
| Deck         | Encoded Integer           |

### 📦 To Run Locally:

```bash
# Install requirements
pip install flask joblib pandas scikit-learn seaborn matplotlib

# Run the server
python app.py
