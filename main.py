from fastapi import FastAPI, HTTPException
import httpx
from schema import EmployeeCreate, PromotionCreate

app = FastAPI()

# -------------------------------------------------------------
# COMMON BASE URLS FOR ALL MICROSERVICES
# -------------------------------------------------------------
INCLUSION_URL = "http://localhost:8001"
FETCH_URL     = "http://localhost:8002"
DELETE_URL    = "http://localhost:8003"
UPDATE_URL    = "http://localhost:8004"


@app.get("/")
def home():
    return {"message": "API Gateway Running"}


# -------------------------------------------------------------
# 1. CREATE EMPLOYEE  → Inclusion Service (8001)
# -------------------------------------------------------------
@app.post("/employee")
async def create_employee(employee: EmployeeCreate):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{INCLUSION_URL}/employee",
            json=employee.model_dump(mode="json")
        )
        return response.json()


# -------------------------------------------------------------
# 2. CREATE PROMOTION  → Inclusion Service (8001)
# -------------------------------------------------------------
@app.post("/promotion")
async def create_promotion(promotion: PromotionCreate):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{INCLUSION_URL}/promotion",
            json=promotion.model_dump(mode="json")
        )
        return response.json()


# -------------------------------------------------------------
# 3. GET ALL EMPLOYEES → Fetch Service (8002)
# -------------------------------------------------------------
@app.get("/employee")
async def get_employees():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{FETCH_URL}/employee")
        return response.json()


# -------------------------------------------------------------
# 4. GET ALL PROMOTIONS → Fetch Service (8002)
# -------------------------------------------------------------
@app.get("/promotion")
async def get_promotions():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{FETCH_URL}/promotion")
        return response.json()


# -------------------------------------------------------------
# 5. GET EMPLOYEES BY SALARY (SALARY__lt) → Fetch (8002)
# -------------------------------------------------------------
@app.get("/employee/salary/{salary}")
async def get_employee_by_salary(salary: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{FETCH_URL}/employee/{salary}")
        return response.json()


# -------------------------------------------------------------
# 6. GET EMPLOYEES BY SALARY + DEPARTMENT  → Fetch (8002)
#     /employee/filter/sd?salary=50000&department=IT
# -------------------------------------------------------------
@app.get("/employee/filter/sd")
async def get_employee_filter(salary: int, department: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{FETCH_URL}/employee/filter/sd",
            params={"salary": salary, "department": department}
        )
        return response.json()


# -------------------------------------------------------------
# 7. GET EMPLOYEES ORDERED BY SALARY & ID → Fetch (8002)
# -------------------------------------------------------------
@app.get("/employee/order/fields")
async def get_employee_ordered():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{FETCH_URL}/employee/order/fields")
        return response.json()


# -------------------------------------------------------------
# 8. UPDATE EMPLOYEE  → Update Service (8004)
# -------------------------------------------------------------
@app.put("/employee")
async def update_employee(employee: EmployeeCreate):
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{UPDATE_URL}/employee",
            json=employee.model_dump(mode="json")
        )
        return response.json()


# -------------------------------------------------------------
# 9. DELETE EMPLOYEE → Delete Service (8003)
# -------------------------------------------------------------
@app.delete("/employee/{id}")
async def delete_employee(id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{DELETE_URL}/employee",
            params={"id": id}
        )
        return response.json()
