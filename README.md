# 📊 Analysis of Ignored Fields

This project analyzes field inclusion/exclusion and ignore behavior across XML scenario files, using a set of Python scripts and Jupyter notebooks to compute field-level statistics and identify outlet configurations.


---

## 🧩 Scripts Overview

### 1. `fetchRelevantFields.py`

This script parses all XML files in the `/scenarios` directory and identifies fields based on their status in the XML and the properties file:

- **Excluded fields**: Found in the `excludes` section of XML
- **Ignored fields**: Defined in the properties file

#### 📄 Output Files

- `excIgnoredFields.txt`: Excluded **and** ignored fields
- `excNotIgnoredFields.txt`: Excluded but **not** ignored fields
- `incIgnoredFields.txt`: Included but **ignored** fields
- `incNotIgnoredFields.txt`: Included **and not** ignored fields

These files serve as the base for computing field occurrence statistics.

---

### 2. `FetchAllFieldsIncluded&Excluded.py`

This script consolidates the output of `fetchRelevantFields.py` to produce a master list of all relevant fields (included, excluded, ignored, not ignored).

#### 📄 Output

- `allFields.txt`: Master list of all relevant fields to analyze

---

### 3. `parsePdlRef.py`

Parses the PDL reference files and counts the number of times each field (from `allFields.txt`) appears.

#### 📄 Output

- `occByPdlRef.csv`: Field occurrence statistics from PDL references

---

### 4. Jupyter Notebooks (`*.ipynb`)

Two notebooks are used to compute and aggregate statistics from the output of `fetchRelevantFields.py`. They also identify outlets with `includes` and `excludes`.

#### 📄 Output Files

- `occIncludedIgnoredFields.csv`: Included and ignored fields
- `occExcludedIgnoredFields.csv`: Excluded and ignored fields
- `occIncludedNotIgnoredFields.csv`: Included but not ignored fields
- `occExcludedNotIgnoredFields.csv`: Excluded but not ignored fields
- `outletWithIncludes.csv`: List of outlets with `includes`
- `outletWithExcludes.csv`: List of outlets with `excludes`

---

## ✅ Python Setup

### 1. Install Python

Download Python from: https://www.python.org/downloads/  
> ☑️ Don’t forget to check “Add Python to PATH” during installation.

### 2. Install Dependencies

Run the following command from the project root:

```bash
pip install -r requirements.txt


