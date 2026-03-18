from fastapi import APIRouter, UploadFile, File
import pandas as pd

router=APIRouter()

@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    df=pd.read_csv(file.file)
    rows,columns=df.shape
    return{
    "rows":rows,
    "columns":columns,
    "column_names":list(df.columns)
}