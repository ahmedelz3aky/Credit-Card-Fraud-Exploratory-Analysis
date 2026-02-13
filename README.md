
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

# Credit Card Fraud — Exploratory Analysis (تحليل استكشافي للاحتيال باستخدام بيانات البطاقات)

### نبذة
مشروع يهدف إلى استكشاف وتحليل بيانات معاملات بطاقات الائتمان لاستخراج أنماط قد تشير إلى سلوك احتيالي. يتضمن تنظيف البيانات، تحليل وصفّي، تصورات متعددة، وبعض تجارب النمذجة الأولية.

### المميزات
- معالجة وتنظيف البيانات وتسليم نسخة `cleaned_df.parquet` جاهزة للتحليل.
- دفتر عمل تفاعلي `code.ipynb` يحتوي على الشرح، الرسوم البيانية، والنتائج.
- تعليمات لإدارة الملفات الكبيرة باستخدام Git LFS.

### بنية المستودع (المهمة الحالية)
- `Home.py` — سكربت مساعد لتشغيل أجزاء من التحليل برمجياً
- `requirements.txt` — تبعيات Python للمشروع
- `code.ipynb` — دفتر Jupyter (مُخزن عبر Git LFS)
- `cleaned_df.parquet` — نسخة منظفة من البيانات (مُدارة عبر Git LFS)
- `credit_card_transactions.parquet` — البيانات الخام (مُدارة عبر Git LFS)

### متطلبات سابقة
- Python 3.8+
- Git
- Git LFS (لتحميل الملفات الكبيرة)

### تثبيت وتشغيل (موجز)
1. استنخِب المشروع:

```bash
git clone https://github.com/ahmedelz3aky/Credit-Card-Fraud-Exploratory-Analysis.git
cd Credit-Card-Fraud-Exploratory-Analysis
```

2. تثبيت Git LFS (مرة واحدة على الجهاز) وتشغيله:

```bash
# Windows (PowerShell)
choco install git-lfs -y   # إذا كان لديك Chocolatey
# أو نزِّل من https://git-lfs.github.com واتّبع التعليمات
git lfs install
```

3. سحب محتويات LFS (بعد استنساخ المستودع):

```bash
git lfs pull --all
```

4. إنشاء بيئة افتراضية وتثبيت التبعيات:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

5. فتح `code.ipynb` في Jupyter Lab / Notebook:

```bash
jupyter lab
```

### ملاحظات حول البيانات والخصوصية
- ملف `credit_card_transactions.parquet` يحتوي بيانات معاملات؛ تأكد من احترام أي شروط خصوصية أو قيود مشاركة تنطبق على البيانات قبل إعادة توزيعها.

### نصائح مُتعلقة بـ Git LFS
- GitHub يحدّد حجم الملفات المرفوعة عبر Git (100 MB)؛ لذلك تُدار الملفات الكبيرة هنا عبر Git LFS.
- لرفع ملفات كبيرة جديدة استخدم `git lfs track "*.parquet"` ثم أضِف وادفع كالمعتاد.

### الترخيص والاتصال
- إن أردت رفع تغييرات أو تبادل ملاحظات فتح issue أو راسلني عبر GitHub.

---
*README مُحدَّث: يشرح طريقة العمل، الاعتمادات، وتعليمات Git LFS لسحب الملفات الكبيرة.*
