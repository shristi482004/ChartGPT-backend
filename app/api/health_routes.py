from fastapi import APIRouter

router=APIRouter()

@router.get("/health")
def health_check():
    return {"status":"Chartgpt backend is healthy and running"}