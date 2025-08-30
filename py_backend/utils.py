from fastapi import APIRouter
import requests
from sse_starlette.sse import EventSourceResponse

router = APIRouter()

@router.get("/functions/get_joke")
async def get_joke():
    try:
        joke_res = requests.get("https://v2.jokeapi.dev/joke/Programming")
        joke_data = joke_res.json()
        joke = (
            f"{joke_data['setup']} - {joke_data['delivery']}"
            if joke_data["type"] == "twopart"
            else joke_data["joke"]
        )
        return {"joke": joke}
    except Exception as e:
        print("Error fetching joke:", e)
        return {"error": "Could not fetch joke"}

@router.get("/functions/get_weather")
async def get_weather(location: str, unit: str = "celsius"):
    try:
        geo_res = requests.get(f"https://nominatim.openstreetmap.org/search?q={location}&format=json")
        geo_data = geo_res.json()
        if not geo_data:
            return {"error": "Invalid location"}
        lat, lon = geo_data[0]["lat"], geo_data[0]["lon"]
        weather_res = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m&temperature_unit={unit}")
        weather = weather_res.json()
        now = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC").json()["datetime"][:13] + ":00"
        index = weather["hourly"]["time"].index(now)
        current_temperature = weather["hourly"]["temperature_2m"][index]
        return {"temperature": current_temperature}
    except Exception as e:
        print("Error fetching weather:", e)
        return {"error": "Could not fetch weather"}

@router.post("/turn_response")
async def turn_response(request):
    async def event_generator():
        for i in range(10):
            yield {"event": "message", "data": f"Event {i}"}
    return EventSourceResponse(event_generator())
