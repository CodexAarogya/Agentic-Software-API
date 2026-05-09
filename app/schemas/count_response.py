from pydantic import BaseModel
from app.schemas import customer, employee, office, order, orderDetail, payment, product, productLine

class CountResponse(BaseModel):

    customers: int
    orders: int
    products: int
    employees: int
    offices: int
    payments: int
    orderdetails: int
    productlines: int
    