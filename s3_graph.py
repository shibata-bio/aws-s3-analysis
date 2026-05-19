import boto3
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# S3設定
# =========================

bucket = "titanic-data-suguru-2026"
key = "aws_s3_analysis.csv"
local_file = "downloaded.csv"

# =========================
# S3接続
# =========================

s3 = boto3.client("s3")

# CSVダウンロード
s3.download_file(bucket, key, local_file)

# CSV読み込み
df = pd.read_csv(local_file)

# 数値型へ変換
df["value"] = pd.to_numeric(df["value"])

# =========================
# グラフ作成
# =========================

plt.plot(df["id"], df["value"])

plt.xlabel("ID")
plt.ylabel("Value")
plt.title("AWS S3 Data Analysis")

# 画像保存
plt.savefig("graph.png")

print("グラフ保存完了")