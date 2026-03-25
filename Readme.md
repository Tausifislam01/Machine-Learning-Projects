# Student Performance Prediction - End-to-End ML Project

## Overview

This is a comprehensive end-to-end machine learning project that predicts student math performance (math scores) based on various demographic and academic factors. The project includes data ingestion, exploratory data analysis, data transformation, model training, and a FastAPI web application for making predictions.

## Project Features

- **Machine Learning Pipeline**: Automated data processing and model training workflow
- **Multiple ML Models**: Compares 7 different regression algorithms to find the best performer
- **REST API**: FastAPI-based web service for making predictions
- **Web UI**: HTML form interface for user-friendly predictions
- **Data Preprocessing**: Handles categorical encoding and feature scaling
- **Error Handling**: Custom exception handling and logging throughout the pipeline

## Dataset

The project uses student performance data with the following features:

**Input Features:**
- Gender (male/female)
- Race/Ethnicity (groups A-E)
- Parental Level of Education (various levels)
- Lunch Type (standard/free or reduced)
- Test Preparation Course (completed/none)
- Reading Score (0-100)
- Writing Score (0-100)

**Target Variable:**
- Math Score (to be predicted)

## Project Structure

```
Machine-Learning-Projects/
├── app.py                          # FastAPI application entry point
├── setup.py                        # Package setup configuration
├── requirements.txt                # Project dependencies
├── Readme.md                       # Project documentation
├── src/
│   ├── __init__.py
│   ├── exception.py               # Custom exception handling
│   ├── logger.py                  # Logging configuration
│   ├── utils.py                   # Utility functions
│   ├── components/
│   │   ├── data_ingestion.py      # Data loading and splitting
│   │   ├── data_transformation.py # Feature engineering and preprocessing
│   │   └── model_trainer.py       # Model training and evaluation
│   └── pipeline/
│       ├── train_pipeline.py      # Training workflow orchestration
│       └── predict_pipeline.py    # Inference pipeline
├── notebook/
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb   # Exploratory Data Analysis
│   ├── 2. MODEL TRAINING.ipynb              # Model experimentation
│   └── data/stud.csv              # Raw student data
├── artifacts/                     # Generated during training
│   ├── train.csv
│   ├── test.csv
│   ├── raw.csv
│   ├── model.pkl                  # Trained model
│   └── preprocessor.pkl           # Fitted preprocessor
├── templates/
│   └── index.html                 # Web UI for predictions
└── logs/                          # Application logs
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone or download the project:**
   ```bash
   cd Machine-Learning-Projects
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Training the Model

To train the model with your data:

```python
from src.pipeline.train_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.initiate_training()
```

Or run via command line:
```bash
python -m src.pipeline.train_pipeline
```

### 2. Running the Web Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The application will be available at:
- **Web UI**: http://localhost:8000/
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### 3. Making Predictions

**Via Web Form:**
1. Navigate to http://localhost:8000/
2. Fill in the student information
3. Click "Predict" to get the estimated math score

**Via REST API:**

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "female",
    "race_ethnicity": "group B",
    "parental_level_of_education": "bachelor'"'"'s degree",
    "lunch": "standard",
    "test_preparation_course": "none",
    "reading_score": 72,
    "writing_score": 74
  }'
```

## Dependencies

Key libraries used in this project:

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms
- **catboost**: Gradient boosting framework
- **xgboost**: XGBoost implementation
- **fastapi**: Modern web framework for APIs
- **uvicorn**: ASGI web server
- **seaborn & matplotlib**: Data visualization
- **dill**: Enhanced object serialization

See `requirements.txt` for complete list.

## Machine Learning Models

The project trains and compares the following models:

1. **Random Forest Regressor** - Ensemble method using decision trees
2. **Decision Tree Regressor** - Single tree-based model
3. **Gradient Boosting Regressor** - Iterative boosting approach
4. **Linear Regression** - Classical linear model
5. **K-Neighbors Regressor** - Instance-based learning
6. **XGBRegressor** - Extreme Gradient Boosting
7. **CatBoost Regressor** - Categorical Boosting

The model with the highest R² score is selected and saved for predictions.

## Project Workflow

```
Raw Data
   ↓
[Data Ingestion] → Split into train/test
   ↓
[Exploratory Data Analysis] → Understand patterns
   ↓
[Data Transformation] → Encode categorical features, scale numerical features
   ↓
[Model Training] → Train multiple models and evaluate
   ↓
[Model Selection] → Choose best performing model
   ↓
[Save Artifacts] → Store model and preprocessor
   ↓
[Prediction Pipeline] → Use trained model for predictions
```

## Project Notebooks

- **1. EDA STUDENT PERFORMANCE.ipynb**: Exploratory data analysis with visualizations and insights
- **2. MODEL TRAINING.ipynb**: Model experimentation and hyperparameter tuning

## Configuration

- **Train/Test Split**: 80/20 with random_state=42 for reproducibility
- **Data Directory**: Raw data is read from `notebook/data/stud.csv`
- **Artifacts Location**: All trained models and preprocessors are stored in `artifacts/`
- **Random State**: Fixed at 42 for reproducibility across runs

## Error Handling & Logging

- Custom exceptions are raised with detailed error messages
- Comprehensive logging tracks all pipeline steps
- Logs are saved in the `logs/` directory

## Author

MD. Tausif-Ul-Islam 
Email: tausifislam2001@gmail.com

## Project Status

This is a complete end-to-end ML pipeline ready for deployment and predictions on student performance data.