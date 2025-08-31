import urllib.parse
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="IMG Generator")

@app.post("/generate-image", response_model=schemas.ImageResponse)
def generate_image(
    request: schemas.ImageRequest, db: Session = Depends(get_db)
):
    db_log = models.Log(prompt=request.prompt)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)

    encoded_prompt = urllib.parse.quote_plus(request.prompt)
    mock_url = f"https://example.com/generated_image?prompt={encoded_prompt}"

    return schemas.ImageResponse(image_url=mock_url)

@app.get("/")
def read_root():
    return {"message": "Welcome to IMG Generator"}