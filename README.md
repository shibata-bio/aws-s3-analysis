# AWS S3 Data Analysis

A data analysis project that demonstrates how to build a simple cloud-based data processing pipeline using **AWS S3** and **Python**.

The project retrieves CSV files stored in Amazon S3, analyzes the data with pandas, and visualizes the results using matplotlib.

---

## 📌 Overview

This project was created to learn how cloud storage can be integrated into a Python-based data analysis workflow.

### Workflow

1. Upload CSV files to Amazon S3
2. Retrieve the files using boto3
3. Analyze the data with pandas
4. Visualize the results using matplotlib

---

## 🛠 Tech Stack

- Python
- AWS S3
- boto3
- pandas
- matplotlib
- Git / GitHub

---

## 📂 Project Structure

```
aws-s3-analysis/
│
├── data/
├── src/
│   ├── s3_analysis.py
│   └── s3_graph.py
├── images/
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

```bash
pip install -r requirements.txt

python s3_analysis.py
python s3_graph.py
```

---

## 📖 What I Learned

- Using Amazon S3 as cloud storage
- Accessing AWS services with boto3
- Building a data analysis workflow with pandas
- Visualizing data using matplotlib
- Managing Python projects with Git and GitHub

---

## 🔮 Future Improvements

- Add automated data processing
- Deploy the project using AWS Lambda
- Create an interactive dashboard with Streamlit
