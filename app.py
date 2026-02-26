from fastapi import FastAPI
from models import *

app = FastAPI(title="Контрольная работа №1",
              description="Технологии разработки серверных приложений")


# задание 1.1
@app.get("/")
async def root():
    return {"message": "Ура ура победа победа. Добро пожаловать в моё приложение FastAPI!"}


# задание 1.3
@app.post("/calculate")
async def calculate(num1: float, num2: float):
    result = num1 + num2
    return {"result": result}


# задание 1.4
@app.get("/users")
async def get_user():
    user = User(name="Кирилл", age=19)
    return user


# задание 1.5
@app.post("/user")
async def check_adult(user: User):
    is_adult = user.age >= 18

    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }


# задание 2

feedback_storage = []

@app.post("/feedback")
async def create_validated_feedback(feedback: Feedback):
    feedback_storage.append(feedback)
    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }

@app.get("/feedbacks")
async def get_all_feedbacks():
    return {"feedbacks": feedback_storage}