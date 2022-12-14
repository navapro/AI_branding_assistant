from fastapi import FastAPI, HTTPException
from call_gpt3 import generate_branding, generate_keywords
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
handler = Mangum(app)
MAX_INPUT_LENGTH = 32

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/generate_branding")
async def generate_branding_api(prompt: str):
    validate_input(prompt)
    result = generate_branding(prompt)
    return {"branding": result}

@app.get("/generate_keywords")
async def generate_keywords_api(prompt: str):
    validate_input(prompt)
    result = generate_keywords(prompt)
    return {"keywords": result}

@app.get("/generate_branding_and_keywords")
async def generate_branding_and_keywords_api(prompt: str):
    validate_input(prompt)
    branding = generate_branding(prompt)
    keywords = generate_keywords(prompt)
    return {"branding": branding, "keywords": keywords}

def validate_input(prompt):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(status_code = 400, detail = f"Length of input is too long, must be less than {MAX_INPUT_LENGTH} characters")

