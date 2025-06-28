from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database, utils, auth
import ast

router = APIRouter(prefix="/match", tags=["Face Match"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=schemas.MatchResult)
def match_face(
    aadhaar: str = Form(...),
    face_image: UploadFile = File(...),
    token: dict = Depends(auth.verify_access_token),
    db: Session = Depends(get_db),
):
    user = db.query(models.User).filter(models.User.aadhaar == aadhaar).first()
    if not user:
        raise HTTPException(status_code=404, detail="User with this Aadhaar not found")

    uploaded_encoding = utils.extract_face_encoding(face_image)
    stored_encoding = ast.literal_eval(user.face_encoding)
    match_percent = utils.calculate_match_percent(stored_encoding, uploaded_encoding)

    return {"user":user, "match_percent": match_percent}