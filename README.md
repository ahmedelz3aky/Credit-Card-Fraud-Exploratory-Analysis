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

## Data Description
The repository contains transaction-level data for credit card activity. Typical columns and content included in the datasets are:

- `transaction_id`: unique identifier for each transaction
- `timestamp` / `date`: transaction datetime
- `amount`: transaction amount (numeric)
- `merchant` / `merchant_category`: merchant name or category
- `cardholder_id` / `account_id`: anonymized identifier for the cardholder
- `location` / `country`: transaction location (when available)
- `is_fraud` or `label`: binary indicator (fraud / non-fraud) when provided

Notes:
- Column names and exact schema may differ between raw and cleaned files; inspect a sample via the notebook (cells 1–3) to confirm.
- Sensitive fields (if present) should be handled according to privacy rules; do not publish or share raw personal data.

## Notebook workflow (project steps included in `code.ipynb`)
The analysis notebook is organized to reproduce the full EDA and contains the following main steps:

1. Environment setup — import libraries and set display options.
2. Data loading — read raw/parquet files and show sample rows.
3. Initial data audit — examine schema, missing values, and basic statistics.
4. Data cleaning & preprocessing — handle missing values, type conversions, timestamp parsing, and deduplication.
5. Feature engineering — create time-based features, aggregated features, and categorical encodings.
6. Exploratory analysis & visualizations — distributions, time-series patterns, merchant/category summaries, and fraud-specific views.
7. Class imbalance handling — resampling strategies and baseline considerations for imbalanced fraud labels.
8. Baseline modeling (optional) — simple models (e.g., logistic regression, tree-based) and cross-validation to get baseline metrics.
9. Results & interpretation — evaluate model performance, present key visual findings, and summarize actionable insights.
10. Next steps & reproducibility notes — suggestions for advanced modeling, deployment, and data governance.

Each step contains code cells and short narrative notes to explain the reasoning and findings. You can run the notebook end-to-end or execute selected sections interactively.

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
