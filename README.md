# AWS S3 Data Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/AWS_S3-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 📖 Overview

This project demonstrates how to build a simple cloud-based data analysis pipeline using **AWS S3** and **Python**.

CSV files stored in Amazon S3 are retrieved using **boto3**, processed with **pandas**, and visualized using **matplotlib**.

This project helped me understand how cloud services can be integrated into data analysis workflows and serves as a foundation for learning data engineering.

---

## ⭐ Key Features

- Uploading and retrieving CSV files with Amazon S3
- Accessing AWS resources using boto3
- Data preprocessing and analysis using pandas
- Data visualization using matplotlib
- Building an end-to-end cloud data analysis workflow

---

## 🏗 Workflow

<p align="center">
  <img src="images/workflow.png" alt="AWS S3 Data Analysis Workflow" width="700">
</p>

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Cloud | AWS S3 |
| Libraries | boto3, pandas, matplotlib |
| Version Control | Git / GitHub |

---

## 📂 Project Structure

```text
aws-s3-analysis/
│
├── data/
│   └── sample.csv
│
├── images/
│   ├── workflow.png
│   └── workflow2.png
│
├── src/
│   ├── s3_analysis.py
│   └── s3_graph.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Workflow

1. Upload a CSV file to Amazon S3
2. Retrieve the file using boto3
3. Load the dataset into pandas
4. Perform data preprocessing and exploratory data analysis
5. Visualize the results using matplotlib

---

## ▶️ How to Run

```bash
git clone https://github.com/shibata-bio/aws-s3-analysis.git

cd aws-s3-analysis

pip install -r requirements.txt

python src/s3_analysis.py
python src/s3_graph.py
```

---

## 📊 Results

This project successfully demonstrates:

- Uploading datasets to Amazon S3
- Retrieving cloud data using boto3
- Processing datasets with pandas
- Visualizing analytical results using matplotlib
- Building a reproducible cloud-based data analysis workflow

<p align="center">
  <img src="images/workflow2.png" alt="Analysis Result" width="700">
</p>

---

## 📖 What I Learned

- Built a cloud-based data analysis pipeline using AWS S3
- Learned how to connect Python applications with AWS services using boto3
- Improved data processing and analysis skills using pandas
- Created visualizations to communicate analytical results
- Organized a reproducible Python project using Git and GitHub

---

## 🔮 Future Improvements

- Automate the workflow using AWS Lambda
- Containerize the application using Docker
- Build an interactive dashboard with Streamlit
- Integrate Amazon Athena for SQL-based analysis

---

## 👤 Author

**Suguru Shibata**

- M.S. Student, Hiroshima University
- Interested in Data Science, Machine Learning, and Cloud Computing.

GitHub: https://github.com/shibata-bio
