# AWSのS3を操作するためのライブラリ
import boto3

# データ分析用ライブラリ
import pandas as pd


# =========================
# S3設定
# =========================

# 使用するS3バケット名
bucket = "titanic-data-suguru-2026"

# S3上に保存されているCSVファイル名
key = "aws_s3_analysis.csv"

# ダウンロード後のローカルファイル名
local_file = "downloaded.csv"


# =========================
# S3へ接続
# =========================

# boto3でS3クライアントを作成
s3 = boto3.client("s3")


# =========================
# S3からCSVをダウンロード
# =========================

# S3内のCSVをローカルに保存
s3.download_file(bucket, key, local_file)

print("S3からCSVをダウンロードしました")


# =========================
# CSV読み込み
# =========================

# pandasでCSVを読み込む
df = pd.read_csv(local_file)

print("\n=== 読み込んだデータ ===")
print(df)


# =========================
# データ型変換
# =========================

# value列を数値型に変換
# （文字列のままだと平均計算できない）
df["value"] = pd.to_numeric(df["value"])


# =========================
# 統計情報表示
# =========================

print("\n=== 統計情報 ===")
print(df.describe())


# =========================
# 平均値計算
# =========================

average = df["value"].mean()

print("\n平均値:", average)