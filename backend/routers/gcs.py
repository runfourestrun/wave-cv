from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from pydantic import BaseModel, Field
from dto.gcs import upload_to_gcs

router = APIRouter(prefix="/gcs", tags=["gcs"])

#Todo: This is supposed to wrap a service that sends a picture to roboflow for inference.... not what upload_to_gcs is currently doing!
class GCSUploadInput(BaseModel):
    bucket: str = Field(..., description="GCS bucket to upload to")
    folder: str = Field(..., description="GCS folder to upload to")

@router.post("/upload")
async def upload(file: UploadFile = File(...), input: GCSUploadInput = Depends()):
    try:
        result = upload_to_gcs(file, input.bucket, input.folder)
        return {"message": f"File uploaded successfully to {result}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))