
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

 # Credit Card Fraud — Exploratory Analysis

 ## Project Overview
 This repository contains an exploratory data analysis (EDA) of credit card transactions to investigate patterns that may indicate fraudulent behavior. The analysis covers data cleaning, feature inspection, visualizations, and initial modeling experiments.

 ## Key Deliverables
 - `code.ipynb` — Jupyter notebook with the full EDA and visualizations (stored via Git LFS)
 - `cleaned_df.parquet` — cleaned dataset used in the notebook (tracked with Git LFS)
 - `credit_card_transactions.parquet` — original/raw transaction dataset (tracked with Git LFS)
 - `Home.py` — helper script for running parts of the analysis programmatically
 - `requirements.txt` — Python dependencies

 ## Repository Structure
 ```
 .
 ├─ Home.py
 ├─ requirements.txt
 ├─ code.ipynb              # tracked via Git LFS
 ├─ cleaned_df.parquet      # tracked via Git LFS
 └─ credit_card_transactions.parquet  # tracked via Git LFS
 ```

 ## Requirements
 - Python 3.8 or newer
 - Git
 - Git LFS (required to fetch large assets)

 ## Quick Start
 1. Clone the repository:

 ```bash
 git clone https://github.com/ahmedelz3aky/Credit-Card-Fraud-Exploratory-Analysis.git
 cd Credit-Card-Fraud-Exploratory-Analysis
 ```

 2. Install and initialize Git LFS (one-time setup):

 ```bash
 # Windows (PowerShell)
 choco install git-lfs -y    # if you have Chocolatey
 # or download/install from https://git-lfs.github.com
 git lfs install
 ```

 3. Download LFS objects:

 ```bash
 git lfs pull --all
 ```

 4. (Optional) Create a virtual environment and install dependencies:

 ```bash
 python -m venv .venv
 .\.venv\Scripts\activate   # PowerShell/Windows
 pip install -r requirements.txt
 ```

 5. Launch Jupyter Lab / Notebook and open `code.ipynb`:

 ```bash
 jupyter lab
 ```

 ## Data Privacy and Usage
 The datasets in this repository may contain sensitive transactional information. Ensure you have the legal right to access and use the data and comply with any privacy, governance, or contractual restrictions before sharing or publishing results.

 ## Working with Git LFS
 - GitHub limits standard Git pushes to files under 100 MB; large files in this repo are managed via Git LFS.
 - To add large files in the future:

 ```bash
 git lfs track "*.parquet"
 git add .gitattributes
 git add <large-file>
 git commit -m "Add large file via Git LFS"
 git push origin main
 ```

 ## Contributing
 Please open an issue or submit a pull request. For major changes, open an issue first to discuss the scope.

 ## License & Contact
 If you have questions or want to collaborate, create an issue or contact the repository owner on GitHub.

 ---
 *README updated: full English, professional, with clear Git LFS and setup instructions.*
python -m venv .venv
