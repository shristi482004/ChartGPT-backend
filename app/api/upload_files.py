from fastapi import APIRouter, UploadFile, File
from app.services.dataset_services import analyze_dataset
import pandas as pd

router=APIRouter()

@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    df=pd.read_csv(file.file)
    
    result=analyze_dataset(df)

    return result