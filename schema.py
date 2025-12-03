from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Literal

class EmployeeCreate(BaseModel):
    ID: int
    NAME: str
    GENDER: Literal["MALE", "FEMALE", "OTHER"]
    DOB: date
    DOJ: date
    DEPARTMENT: str
    DESIGNATION: str
    SALARY: int
    PHONE: str
    EMAIL: EmailStr

class PromotionCreate(BaseModel):
    ID: int
    NAME: str
    CURR_DESIGNATION: str
    CURR_SALARY: int
    ELIGIBLE_PROMOTION: str
