from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from src.pipeline.predict_pipeline import PredictPipeline, CustomData

app = FastAPI(title="Student Performance Prediction API", version="1.0.0")

templates = Jinja2Templates(directory="templates")


class PredictionInput(BaseModel):
    gender: str = Field(..., example="female")
    race_ethnicity: str = Field(..., example="group B")
    parental_level_of_education: str = Field(..., example="bachelor's degree")
    lunch: str = Field(..., example="standard")
    test_preparation_course: str = Field(..., example="none")
    reading_score: float = Field(..., example=72)
    writing_score: float = Field(..., example=74)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})


@app.post("/predict")
def predict_api(payload: PredictionInput):
    data = CustomData(
        gender=payload.gender,
        race_ethnicity=payload.race_ethnicity,
        parental_level_of_education=payload.parental_level_of_education,
        lunch=payload.lunch,
        test_preparation_course=payload.test_preparation_course,
        reading_score=payload.reading_score,
        writing_score=payload.writing_score,
    )

    pred_df = data.get_data_as_data_frame()
    result = PredictPipeline().predict(pred_df)

    return JSONResponse(
        content={
            "predicted_math_score": float(result[0])
        }
    )


@app.post("/predict-form", response_class=HTMLResponse)
def predict_form(
    request: Request,
    gender: str = Form(...),
    race_ethnicity: str = Form(...),
    parental_level_of_education: str = Form(...),
    lunch: str = Form(...),
    test_preparation_course: str = Form(...),
    reading_score: float = Form(...),
    writing_score: float = Form(...),
):
    data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score,
    )

    pred_df = data.get_data_as_data_frame()
    result = PredictPipeline().predict(pred_df)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": round(float(result[0]), 2),
        },
    )
