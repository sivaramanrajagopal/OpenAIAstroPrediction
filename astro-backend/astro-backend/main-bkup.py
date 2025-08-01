from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from astrology import get_planet_positions, generate_gpt_prompt, get_astrology_interpretation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict")
def predict(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    data = get_planet_positions(dob, tob, lat, lon, tz_offset)
    prompt = generate_gpt_prompt(data)
    interpretation = get_astrology_interpretation(prompt)
    return {"chart": data, "interpretation": interpretation}
