from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.dataset_services import analyze_dataset
import pandas as pd

router=APIRouter()

@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):

    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")
    
    try:
        df=pd.read_csv(file.file)

        if df.empty():
            raise HTTPException(status_code=400, detail="Uploaded CSV file is empty")
        
        result=analyze_dataset(df)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail='Error processing the uploaded file: ' + str(e))