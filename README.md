# FUTURE_ML_02 — Smart Support Ticket Classification & Prioritization System

## 📌 Project Overview

This project is developed as part of the **Future Interns Machine Learning Internship Task 2**.

The objective of this project is to build an **AI-powered Support Ticket Classification and Prioritization System** using Natural Language Processing (NLP) and Machine Learning techniques.

The system automatically:

* Reads customer support ticket descriptions
* Classifies tickets into categories
* Predicts ticket priority levels
* Helps businesses improve support operations and response efficiency

---

# 🎯 Business Problem

Modern companies receive thousands of support tickets daily through:

* Emails
* Helpdesk portals
* Customer complaint systems
* Service platforms

Manual ticket sorting creates several problems:

* Delayed urgent issue handling
* Increased support backlog
* Poor ticket routing
* Reduced customer satisfaction

This project automates support ticket processing using Machine Learning to improve operational efficiency.

---

# 🚀 Solution Overview

The system uses:

* NLP preprocessing
* TF-IDF feature extraction
* Machine Learning classification models

to automatically:
✅ Classify support tickets
✅ Predict ticket priorities
✅ Improve ticket routing efficiency

---

# 📂 Dataset Used

Dataset: **Customer Support Tickets Dataset**

Dataset contains:

* Ticket Descriptions
* Ticket Types
* Ticket Priorities
* Ticket Status
* Ticket Channels
* Customer Satisfaction Ratings

Dataset Features:

* 8,469 rows
* 17 columns
* Real-world customer support ticket data

---

# 🛠️ Technologies & Libraries Used

## Programming Language

* Python

## NLP Libraries

* NLTK
* Scikit-learn

## Machine Learning

* Logistic Regression
* TF-IDF Vectorization

## Visualization

* Matplotlib
* Seaborn
* WordCloud

## Deployment

* Streamlit

---

# 📊 Project Workflow

## 1️⃣ Data Collection

Imported customer support ticket dataset for NLP analysis and classification.

---

## 2️⃣ Data Preprocessing

Performed:

* Missing value handling
* Duplicate removal
* Text cleaning
* Lowercasing
* Stopword removal
* Lemmatization
* Punctuation removal

---

## 3️⃣ Exploratory Data Analysis (EDA)

Analyzed:

* Ticket category distribution
* Ticket priority distribution
* Common support issues
* Frequent complaint keywords

Visualizations were created to understand support operations patterns.

---

## 4️⃣ NLP Feature Engineering

Used:

### TF-IDF Vectorization

to convert text into numerical features for machine learning models.

---

## 5️⃣ Ticket Category Classification

Built a Machine Learning model to classify support tickets into categories such as:

* Technical Issue
* Billing
* Account Access
* General Query
* Refund Request

---

## 6️⃣ Priority Prediction

Built a separate ML model to predict ticket priority levels:

* High
* Medium
* Low

This helps support teams prioritize urgent customer issues.

---

## 7️⃣ Model Evaluation

Evaluated the models using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

## 8️⃣ Streamlit Dashboard

Developed an interactive dashboard where users can:

* Enter support ticket text
* Predict ticket category
* Predict priority level
* View business benefits

---

# 📈 Key Features Implemented

✅ NLP Text Cleaning
✅ Stopword Removal
✅ Lemmatization
✅ TF-IDF Vectorization
✅ Ticket Classification
✅ Priority Prediction
✅ Confusion Matrix Visualization
✅ Word Cloud Visualization
✅ Interactive Streamlit Dashboard
✅ Business Insights

---

# 📊 Visualizations Included

The project includes:

* Ticket Category Distribution
* Priority Distribution
* Word Cloud of Common Complaint Terms
* Confusion Matrix
* Classification Performance Reports

---

# 💡 Business Insights

## Key Findings

* Technical issues were the most common support requests.
* High-priority tickets require immediate escalation.
* Automated ticket routing significantly reduces manual workload.
* NLP-based systems improve customer response efficiency.

## Business Recommendations

* Automate ticket categorization to reduce support delays.
* Use AI-based prioritization for urgent issue handling.
* Route tickets automatically to specialized support teams.
* Monitor high-priority ticket patterns to improve service quality.

---

# 🎫 Example Prediction

## Input Ticket

```text id="nrlutq"
"My payment failed and I cannot access my account."
```

## Model Output

```text id="9p6y2n"
Predicted Category: Billing Issue
Predicted Priority: High
```

---

# 🚀 Streamlit Dashboard Features

The dashboard provides:

* Ticket text input
* Automatic category prediction
* Priority prediction
* Business benefit explanation
* User-friendly interface

---

# 📷 Project Screenshots

Add screenshots here:

* Dashboard Interface
* Prediction Output
* Confusion Matrix
* Word Cloud
* Ticket Distribution Charts

---

# 📁 Project Structure

```text id="6h0h3k"
FUTURE_ML_02/
│
├── data/
│   └── customer_support_tickets.csv
│
├── notebooks/
│   └── support_ticket_classification.ipynb
│
├── dashboard/
│   └── app.py
│
├── models/
│   ├── category_model.pkl
│   ├── priority_model.pkl
│   └── tfidf.pkl
│
├── outputs/
│   ├── charts/
│   ├── confusion_matrix/
│   └── reports/
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── presentation.pptx
```

---

# ▶️ How to Run the Project

## Step 1 — Install Dependencies

```bash id="v4e1uh"
pip install pandas numpy matplotlib seaborn scikit-learn nltk streamlit wordcloud joblib
```

---

## Step 2 — Run Jupyter Notebook

```bash id="x3c7xj"
jupyter notebook
```

Open:

```text id="jlwmre"
support_ticket_classification.ipynb
```

---

## Step 3 — Run Streamlit Dashboard

```bash id="jlwmrf"
streamlit run app.py
```

---

# 📌 Future Improvements

Possible future enhancements:

* Deep Learning NLP Models (BERT)
* Real-Time Ticket Monitoring
* Automatic Ticket Routing
* Sentiment Analysis
* Multi-language Support
* Cloud Deployment

---

# 🎯 Internship Task Objective Achieved

This project successfully fulfills all requirements of:

### Future Interns — Machine Learning Task 2

Including:

* NLP preprocessing
* Text classification
* Priority prediction
* Feature extraction
* ML model evaluation
* Business insights
* Interactive deployment

---

# 👨‍💻 Author

**MYLAVARAPU CHETAN SAI PAVAN KUMAR**

Machine Learning Intern — Future Interns

---

# 📬 Contact

* LinkedIn:https://www.linkedin.com/in/chetan-mylavarapu-554847336
* GitHub:https://github.com/Chetan1013

---

# ⭐ Acknowledgements

Special thanks to:

* Future Interns
* Open-source NLP community
* Kaggle Dataset Contributors
