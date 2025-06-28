import cv2
import numpy as np
import face_recognition  # ✅ This was missing
from fastapi import UploadFile, HTTPException
from typing import List

def extract_face_encoding(file: UploadFile) -> List[float]:
    try:
        image_bytes = file.file.read()
        np_arr = np.frombuffer(image_bytes, np.uint8)

        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if image is None:
            raise HTTPException(status_code=400, detail="Invalid image file")

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print(f"Image shape: {rgb_image.shape}, dtype: {rgb_image.dtype}")

        encodings = face_recognition.face_encodings(rgb_image)
        if not encodings:
            raise HTTPException(status_code=400, detail="No face found in the image")

        return encodings[0].tolist()

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Image processing failed: {str(e)}")

    finally:
        await_file_close(file)


def await_file_close(file: UploadFile):
    try:
        if not file.file.closed:
            file.file.close()
    except Exception:
        pass


def calculate_match_percent(known_encoding: List[float], unknown_encoding: List[float]) -> float:
    known_np = np.array(known_encoding)
    unknown_np = np.array(unknown_encoding)
    distance = face_recognition.face_distance([known_np], unknown_np)[0]
    match_percent = (1.0 - distance) * 100
    return round(match_percent, 2)
