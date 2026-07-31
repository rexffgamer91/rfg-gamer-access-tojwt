from fastapi import FastAPI
from fastapi.responses import JSONResponse
import jwt
import datetime

app = FastAPI()

SECRET_KEY = "my_super_secret_key_123"
ALGORITHM = "HS256"

# ১. হোম রাউট
@app.get("/")
def home():
    return {
        "status": "online",
        "message": "JWT Generator API is running on Render!",
        "credit": "@RFG_GAMER"
    }

# ২. আসল সার্ভিস রাউট
@app.get("/accessTojwt")
def convert_access_to_jwt(access_token: str = None):
    if not access_token:
        return JSONResponse(
            status_code=400,
            content={
                "status": "failed",
                "message": "access_token parameter is required",
                "credit": "@RFG_GAMER"
            }
        )
    
    try:
        payload = {
            "access_token": access_token,
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
        }
        
        generated_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        
        return {
            "status": "success",
            "token": generated_jwt,
            "credit": "@RFG_GAMER"
        }
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "failed",
                "message": f"JWT generation failed: {str(e)}",
                "credit": "@RFG_GAMER"
            }
        )