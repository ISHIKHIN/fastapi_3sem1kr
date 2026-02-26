from pydantic import BaseModel, Field, field_validator

# задание 1.4

class User(BaseModel):
    name: str
    age: int

# задание 2

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50,
                      description="Имя от 2 до 50 символов")
    message: str = Field(..., min_length=10, max_length=500,
                         description="Сообщение от 10 до 500 символов")

    @field_validator('message')
    @classmethod
    def check_forbidden_words(cls, message: str) -> str:

        forbidden_words = ['кринж', 'рофл', 'вайб']

        message_lower = message.lower()
        print(message_lower)
        for word in forbidden_words:
            if word in message_lower:
                raise ValueError(f'Использование недопустимых слов: "{word}"')

        return message