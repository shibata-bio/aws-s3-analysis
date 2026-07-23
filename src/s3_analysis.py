from pathlib import Path

import boto3
import pandas as pd


# =========================
# パス設定
# =========================

# プロジェクトのルートディレクトリ
BASE_DIR = Path(__file__).resolve().parent.parent

# ダウンロードしたCSVの保存先
DATA_DIR = BASE_DIR / "data"
LOCAL_FILE = DATA_DIR / "downloaded.csv"

# dataフォルダが存在しない場合は作成
DATA_DIR.mkdir(parents=True, exist_ok=True)


# =========================
# S3設定
# =========================

# 使用するS3バケット名
BUCKET_NAME = "titanic-data-suguru-2026"

# S3上に保存されているCSVファイル名
OBJECT_KEY = "aws_s3_analysis.csv"


# =========================
# S3へ接続
# =========================

s3 = boto3.client("s3")


# =========================
# S3からCSVをダウンロード
# =========================

try:
    s3.download_file(
        BUCKET_NAME,
        OBJECT_KEY,
        str(LOCAL_FILE),
    )
    print(f"S3からCSVをダウンロードしました: {LOCAL_FILE}")

except Exception as error:
    print(f"S3からのダウンロードに失敗しました: {error}")
    raise


# =========================
# CSV読み込み
# =========================

try:
    df = pd.read_csv(LOCAL_FILE)

except FileNotFoundError:
    print(f"CSVファイルが見つかりません: {LOCAL_FILE}")
    raise

except pd.errors.EmptyDataError:
    print("CSVファイルが空です")
    raise

except pd.errors.ParserError:
    print("CSVファイルの形式を読み取れませんでした")
    raise


print("\n=== 読み込んだデータ ===")
print(df)


# =========================
# データ確認・型変換
# =========================

if "value" not in df.columns:
    raise KeyError("CSVに 'value' 列がありません")

df["value"] = pd.to_numeric(df["value"], errors="coerce")

# 数値に変換できなかった行を除外
df = df.dropna(subset=["value"])


# =========================
# 統計情報表示
# =========================

print("\n=== 統計情報 ===")
print(df["value"].describe())


# =========================
# 平均値計算
# =========================

average = df["value"].mean()

print(f"\n平均値: {average:.2f}")