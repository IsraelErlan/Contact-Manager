from pydantic import BaseModel

class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


class Contact_Read(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_number: str




