# 💧 Water Potability Prediction

> An end-to-end machine learning project that predicts whether water is safe to drink, wrapped in a simple, interactive web app.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 📖 Overview

Access to safe drinking water is a basic human need — yet determining potability from raw chemical readings isn't something the average person can do at a glance. This project bridges that gap.

Using **9 water quality parameters** — pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, and Turbidity — a trained classification model predicts whether a water sample is **potable (safe to drink)** or **not potable**. The model is served through a clean, no-code **Streamlit web app**, so anyone can get an instant prediction just by entering values.

---

## 🗂️ Dataset

| Detail | Info |
|---|---|
| **Source** | [Water Quality Dataset — Kaggle](https://www.kaggle.com/datasets/adityakadiwal/water-potability) |
| **Samples** | 3,276 |
| **Features** | 9 numerical water quality parameters |
| **Target** | `Potability` → `0` = Not Potable, `1` = Potable |

---

## 🔬 Approach

**1. Exploratory Data Analysis**
Explored feature distributions, checked missing values, and visualized correlations. Missing values were found in `ph`, `Sulfate`, and `Trihalomethanes`. Interestingly, the correlation heatmap revealed **very weak linear relationships** between individual features and the target — a key insight that shaped model selection later on.

**2. Preprocessing**
- Missing values filled using **median imputation**
- Features scaled with `StandardScaler` (required for Logistic Regression; not needed for Random Forest)
- Stratified 80/20 train-test split to preserve class ratio

**3. Model Training**
Two classification models were trained and compared:
- Logistic Regression
- Random Forest Classifier

**4. Handling Class Imbalance**
The dataset skews toward "Not Potable" (~61% / 39%). Initial Logistic Regression results showed it predicting *only* the majority class. Applying `class_weight='balanced'` corrected this, improving minority-class recall for both models.

**5. Evaluation**

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression (balanced) | 52.6% | 41.6% | 53.1% | 46.7% |
| **Random Forest (balanced)** | **64.0%** | **55.3%** | 41.0% | **47.1%** |

**Random Forest was selected as the final model.** Because it can capture non-linear patterns, it outperformed Logistic Regression on this dataset, where feature-target relationships are weakly linear.

**6. Model Persistence**
The final model and scaler were saved using `joblib` for reuse without retraining.

**7. Web Application**
A Streamlit app loads the saved model and lets users input water parameters to receive an instant, human-readable prediction.

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone <your-repo-link>
cd betabytez-aiml-task1-hamza_iqbal
```

**2. Install dependencies**
```bash
pip install streamlit scikit-learn pandas numpy joblib matplotlib seaborn
```

**3. Launch the app**
```bash
streamlit run app.py
```

**4. Open in browser**
The app will automatically open at:
```
http://localhost:8501
```

---

## 📁 Project Structure

```
betabytez-aiml-task1-hamza_iqbal/
│
├── data/
│   └── water_potability.csv          # Raw dataset
│
├── water_potability_eda_model.ipynb   # EDA, preprocessing, training & evaluation
├── app.py                             # Streamlit web application
├── water_potability_model.pkl         # Saved trained model
├── scaler.pkl                         # Saved feature scaler
└── README.md                          # Project documentation
```

---

## 🛠️ Tech Stack

`Python` · `Pandas` · `NumPy` · `Scikit-learn` · `Matplotlib` · `Seaborn` · `Streamlit` · `Joblib`

---

## 👤 Author

**Hamza Iqbal**
BetaBytez Summer Internship 2026 — AI/ML Track, Task 1

---

<p align="center"><i>Built as part of the BetaBytez Summer Internship Program 2026 🚀</i></p>