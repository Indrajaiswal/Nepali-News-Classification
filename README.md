# 📰 Nepali News Classification

An end-to-end Natural Language Processing (NLP) and Machine Learning project for automatically classifying Nepali news articles into 12 different categories.

The project uses **TF-IDF for text feature extraction** and **Linear Support Vector Machine (SVM)** as the final classification model. A Streamlit web application is also provided for real-time news classification.

---

## 🚀 Live Demo

The application is deployed using Streamlit.

👉 Add your Streamlit Cloud URL here:

https://nepali-news-classification-hcjnm9j2q2xcdhrd3bek8a.streamlit.app/

---

## 📌 Project Overview

News websites publish a large amount of content every day across different categories. Manually categorizing these articles is time-consuming.

This project aims to automatically classify Nepali news articles into predefined categories using Natural Language Processing and Machine Learning.

### Categories

The model classifies news into the following 12 categories:

- Business
- Crime
- Economy
- Education
- Entertainment
- Global
- Health
- National
- Politics
- Science and Technology
- Society
- Sports

---

## 🎯 Objectives

The main objectives of this project are:

- Collect and prepare a Nepali news dataset
- Clean and preprocess Nepali text
- Perform exploratory data analysis
- Analyze news article characteristics
- Extract textual features using TF-IDF
- Train multiple machine learning classification algorithms
- Compare model performance
- Tune the best-performing model
- Save the trained model for deployment
- Build an interactive Streamlit application
- Deploy the application for real-time prediction

---

## 📊 Dataset

The project uses the **Nepali News Dataset** available on Hugging Face.

Dataset:

`spandyie/nepali-news-dataset`

The original dataset contains approximately **2.76 million news articles**.

For model development, a balanced subset was created.

### Processed Dataset

- Total articles: **96,000**
- Number of categories: **12**
- Articles per category: **8,000**

The processed dataset is balanced across all categories.

> The raw and processed CSV files are not included in this GitHub repository because of their large file sizes.

---

## 🔄 Project Workflow

```text
Nepali News Dataset
        ↓
Data Cleaning
        ↓
Remove Missing Values
        ↓
Remove Duplicates
        ↓
Select 12 Categories
        ↓
Balanced Sampling
        ↓
Exploratory Data Analysis
        ↓
Text Preprocessing
        ↓
TF-IDF Feature Extraction
        ↓
Train/Test Split
        ↓
Multiple ML Models
        ↓
Model Comparison
        ↓
Hyperparameter Tuning
        ↓
Linear SVM
        ↓
Model Saving
        ↓
Streamlit Application
        ↓
News Category Prediction
````

---

## 🧹 Data Preprocessing

The dataset was processed using the following steps:

Selected required columns
Removed missing news articles
Removed missing categories
Removed empty articles
Removed duplicate news articles
Selected 12 target categories
Created a balanced dataset
Cleaned newline and tab characters
Removed unnecessary whitespace
Combined relevant text features for model training

---

## 🔎 Exploratory Data Analysis

Several analyses were performed during EDA:

Category distribution
Category percentage distribution
Missing-value analysis
Duplicate analysis
News article character length
News article word count
Word count distribution
Character length distribution
Word count by category
Extremely long article detection

---
Dataset Distribution

Each category contains:
```text
8,000 articles
```
Therefore:

```text
12 × 8,000 = 96,000 articles
```


---
## 🧠 Feature Engineering

The main text representation used in this project is:

TF-IDF

Term Frequency-Inverse Document Frequency (TF-IDF) converts news articles into numerical feature vectors.

TF-IDF helps the model identify words that are important for distinguishing one category from another.

The vectorizer was trained only on the training data to avoid data leakage.


---
## 🤖 Machine Learning Models

The following algorithms were evaluated:

Multinomial Naive Bayes
Logistic Regression
Linear SVM
Random Forest
XGBoost

Model Comparison
| Model                   |   Accuracy |  Precision |     Recall |   F1 Score |
| ----------------------- | ---------: | ---------: | ---------: | ---------: |
| **Linear SVM**          | **74.41%** | **72.70%** | **74.41%** | **73.25%** |
| Logistic Regression     |     74.03% |     72.49% |     74.03% |     72.96% |
| XGBoost                 |     72.57% |     71.40% |     72.57% |     71.78% |
| Multinomial Naive Bayes |     69.65% |     67.68% |     69.65% |     67.74% |
| Random Forest           |     69.38% |     66.68% |     69.38% |     66.53% |


---
## Final Model

Linear SVM was selected as the final model because it achieved the highest overall performance.
```
Accuracy : 74.41%
Precision: 72.70%
Recall   : 74.41%
F1 Score : 73.25%
```

---
## ⚙️ Hyperparameter Tuning

GridSearchCV was used to tune the Linear SVM model.

The best parameter found was:
```
C = 1
```

Best cross-validation score:
```
0.7332
```

The tuned Linear SVM was selected as the final production model.


---
## 💾 Saved Models

The following trained components are saved in the models/ directory:
```
models/
├── linear_svm.pkl
├── tfidf_vectorizer.pkl
└── label_encoder.pkl
```

linear_svm.pkl

The trained Linear SVM classification model.

tfidf_vectorizer.pkl

The fitted TF-IDF vectorizer used to transform new articles.

label_encoder.pkl

The label encoder used to convert numerical predictions back into category names.


---
## 🌐 Streamlit Application

A Streamlit application was developed to allow users to enter Nepali news articles and receive a predicted category.

Application Features
Nepali news article input
Real-time prediction
Word count
Character count
Model information
Dataset information
Predicted category
Simple interactive interface
Example

Input:
```
नेपालले साफ च्याम्पियनसिप फुटबल प्रतियोगितामा
भारतलाई पराजित गरेको छ।
```
Prediction:
```
Sports
```

## 🖥️ Run the Application Locally

1. Clone the repository
```
git clone https://github.com/Indrajaiswal/Nepali-News-Classification.git
```
2. Navigate to the project
```
cd Nepali-News-Classification
```
3. Create a virtual environment
```
python -m venv venv
```
4. Activate the environment
Windows
```
venv\Scripts\activate
```

5. Install dependencies
```
pip install -r requirements.txt
```
6. Run Streamlit
```
streamlit run app.py
```
The application will open in your browser.


---
## 📁 Project Structure
```
Nepali-News-Classification/
│
├── data/
│   ├── raw/
│   │   └── README.md
│   │
│   └── processed/
│       └── README.md
│
├── models/
│   ├── linear_svm.pkl
│   ├── tfidf_vectorizer.pkl
│   └── label_encoder.pkl
│
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   └── ...
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---
## 🛠️ Technologies Used
Programming Language
 - Python
Data Processing
- Pandas
- NumPy
Data Visualization
- Matplotlib
- Seaborn
Machine Learning
- Scikit-learn
- XGBoost
NLP
- TF-IDF
- Nepali text preprocessing
Deployment
- Streamlit
Model Persistence
- Joblib
Dataset
- Hugging Face Datasets


---
## 📦 Main Python Libraries
```
pandas
numpy
scikit-learn
xgboost
matplotlib
seaborn
streamlit
joblib
datasets
```

---
## 📈 Model Performance

The final Linear SVM model achieved:
```
Accuracy : 74.41%
Precision: 72.70%
Recall   : 74.41%
F1 Score : 73.25%
```
The result demonstrates that traditional machine learning with TF-IDF can provide a strong baseline for Nepali text classification.


---
## ⚠️ Limitations

The project has several limitations:

The dataset contains noisy and diverse Nepali text.
Some categories have similar vocabulary.
TF-IDF does not understand deep semantic relationships between words.
News articles can be very long.
Some articles may contain information related to multiple categories.
The model may incorrectly classify ambiguous articles.



---
## 🔮 Future Improvements

Potential improvements include:

NepaliBERT or other Transformer-based models
Word embeddings
Advanced Nepali text normalization
Better handling of very long articles
Ensemble models
Data augmentation
More extensive hyperparameter tuning
Confidence calibration
Continuous model monitoring
Larger and more diverse training datasets



---
## 👨‍💻 Author

Indra Jaiswal

IT Graduate | Data Science & Machine Learning Enthusiast

Areas of interest:

Machine Learning
Natural Language Processing
Generative AI
Computer Vision
Data Analytics

---
## 📄 License

This project is intended for educational and portfolio purposes.



























