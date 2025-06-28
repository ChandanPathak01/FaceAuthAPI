from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, database, utils, auth

router = APIRouter(prefix="/register", tags=["Register"])

def get_db():
    db = database.sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("",status_code=201, response_model=schemas.USerOut)
async def register_user(
    name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    aadhaar: str = Form(...),
    face_image: UploadFile = File(...),
    token: dict = Depends(auth.verify_access_token),
    db: Session = Depends(get_db),
):
    existing_user = db.query(models.User).filter(models.User.aadhaar == aadhaar).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this Aadhaar already exist")
    encoding = utils.extract_face_encoding(face_image)
    user = models.User(name=name, phone=phone, email=email, aadhaar=aadhaar, face_encoding=str(encoding),)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user