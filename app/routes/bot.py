from fastapi import APIRouter

router = APIRouter(prefix="/bot", tags=["Bot"])

@router.post("/")
def chatbot_response(query: str):
    # Simple bot response logic
    if "workout" in query.lower():
        return {"response": "Here's a suggested workout for you: Push-ups, Squats, and Plank!"}
    return {"response": "I'm here to help! Please ask your fitness-related questions."}
