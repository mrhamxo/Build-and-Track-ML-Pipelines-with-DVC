
# Build and Track ML Pipeline with DVC

This repository contains a complete end-to-end Machine Learning pipeline built using **DVC** for experiment tracking, reproducibility, and modular pipeline management.

The project covers:
- Data ingestion
- Data preprocessing
- Feature engineering
- Model building
- Model evaluation

---

## Project Structure

```
├── data\_ingestion.py
├── data\_preprocessing.py
├── feature\_engineering.py
├── model\_building.py
├── model\_evaluation.py
├── dvc.yam
├── requirements.txt
├── model.pkl
├── metrics.json
└── README.md
````

---

## Build & Track ML Pipelines with DVC

### How to run?

```bash
# Create a virtual environment
conda create -n ml_test python=3.12 -y
conda activate ml_test

# Install dependencies
pip install -r requirements.txt
````

---

### DVC Commands

```bash
# Initialize Git
git init

# Initialize DVC
dvc init    

# Run the full pipeline
dvc repro

# Visualize the pipeline
dvc dag

# Show metrics
dvc metrics show
```

---

## Pipeline Stages (from `dvc.yaml`)

1. **Data Ingestion** → `data/raw/train.csv`, `data/raw/test.csv`
2. **Data Preprocessing** → `data/processed/train_processed.csv`, `data/processed/test_processed.csv`
3. **Feature Engineering** → `data/features/train_bow.csv`, `data/features/test_bow.csv`
4. **Model Building** → `model.pkl`
5. **Model Evaluation** → `metrics.json`

---

## Example DVC DAG

After running:

```bash
dvc dag
```

You should see a visual representation of your pipeline stages and dependencies.

---

## Metrics

All evaluation metrics are stored in `metrics.json` after running the pipeline:

---
