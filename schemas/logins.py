from pydantic import BaseModel, Field

class LoginCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)

    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "password": "password123"
            }
        }

class LoginResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class LoginMessageResponse(BaseModel):
    message: str
    login: LoginResponse

    class Config:
        schema_extra = {
            "example": {
                "message": "Login successful",
                "login": {
                    "id": 1,
                    "username": "johndoe"
                }
            }
        }