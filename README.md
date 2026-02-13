
# Credit Card Fraud Exploratory Analysis

## الوصف
مشروع تحليل استكشافي لبيانات معاملات بطاقات الائتمان بهدف فهم أنماط الاحتيال. يتضمن تنظيف البيانات، تصور النتائج، وملاحظات مبدئية.

## الملفات المضمنة في المستودع
- `Home.py` — سكربت مساعد
- `requirements.txt` — تبعيات المشروع
- `code.ipynb` — (موجود لكن يُدار عبر Git LFS) دفتر Jupyter يحتوي على كامل التحليل
- `cleaned_df.parquet` — (موجود لكن يُدار عبر Git LFS) نسخة منظفة من البيانات
- `credit_card_transactions.parquet` — (موجود لكن يُدار عبر Git LFS) ملف البيانات الأصلي

> ملاحظة: الملفات الكبيرة (`.ipynb` كبير، وملفات `.parquet`) مخزنة باستخدام Git LFS لتفادي حدود GitHub على أحجام الملفات.

## كيفية استنساخ المشروع وسحب الملفات الكبيرة
1. استنخِب المستودع:

```bash
git clone https://github.com/ahmedelz3aky/Credit-Card-Fraud-Exploratory-Analysis.git
cd Credit-Card-Fraud-Exploratory-Analysis
```

2. تأكد من تثبيت Git LFS (مرة واحدة على جهازك):

```bash
# Windows (PowerShell)
choco install git-lfs -y   # إذا كان لديك Chocolatey
# أو حمّله من https://git-lfs.github.com واتبع تعليمات التثبيت
git lfs install
```

3. بعد التثبيت، اسحب الملفات وتهيئ LFS تلقائياً عند سحب المستودع:

```bash
git lfs pull --all
```

4. افتح `code.ipynb` في Jupyter Lab/Notebook بعد تفعيل البيئة الافتراضية إن أردت:

```bash
python -m venv .venv
.\.venv\Scripts\activate   # PowerShell/Windows
pip install -r requirements.txt
jupyter lab  # أو jupyter notebook
```

## ملاحظة حول الملفات الكبيرة
- إذا رغبت في إزالة تتبع ملف من LFS أو رفع نسخة بديلة، راجع توثيق Git LFS.

## تاريخ الرفع والتنظيف
- تم رفع المشروع إلى GitHub مع استبعاد/إدارة الملفات الكبيرة بواسطة Git LFS.


# Credit Card Fraud — Exploratory Analysis

## Overview
This repository contains an exploratory analysis of credit card transactions aimed at identifying patterns that may indicate fraudulent activity. The project includes data cleaning, descriptive analysis, visualizations, and initial modeling experiments.

## Highlights
- Cleaned dataset ready for analysis: `cleaned_df.parquet` (managed with Git LFS)
- Interactive analysis notebook: `code.ipynb` (managed with Git LFS)
- Original dataset: `credit_card_transactions.parquet` (managed with Git LFS)

## Repository structure
- `Home.py` — helper script to run portions of the analysis programmatically
- `requirements.txt` — Python dependencies
- `code.ipynb` — Jupyter notebook with the full EDA (tracked via Git LFS)
- `cleaned_df.parquet` — cleaned dataset used in the notebook (tracked via Git LFS)
- `credit_card_transactions.parquet` — original/raw dataset (tracked via Git LFS)

## Requirements
- Python 3.8+
- Git
- Git LFS (required to download large files)

## Quick start
1. Clone the repository:

```bash
git clone https://github.com/ahmedelz3aky/Credit-Card-Fraud-Exploratory-Analysis.git
cd Credit-Card-Fraud-Exploratory-Analysis
```

2. Install and initialize Git LFS (one-time setup on your machine):

```bash
# Windows (PowerShell)
choco install git-lfs -y    # if you use Chocolatey
# or download from https://git-lfs.github.com and follow instructions
git lfs install
```

3. Download LFS objects (after cloning):

```bash
git lfs pull --all
```

4. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.\.venv\Scripts\activate   # PowerShell/Windows
pip install -r requirements.txt
```

5. Start Jupyter and open the analysis notebook:

```bash
jupyter lab
```

## Data privacy and usage
The `credit_card_transactions.parquet` dataset contains transaction-level data. Make sure you have the right to access and use this data and follow any applicable privacy or compliance requirements before sharing it.

## Notes on Git LFS
- GitHub enforces a 100 MB file limit for regular Git objects; large assets here are stored using Git LFS.
- To add large files in future, track them before adding:

```bash
git lfs track "*.parquet"
git add .gitattributes
git add <large-file>
git commit -m "Add large file via Git LFS"
git push origin main
```

## License & contact
If you want to contribute or report issues, please open an issue or contact the repository owner on GitHub.

---
*This README was updated to provide an English, professional overview and clear Git LFS instructions.*
