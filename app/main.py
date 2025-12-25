from fastapi import FastAPI, Depends
import uvicorn 
from db_manager import get_db
from data_interactor import get_all_contacts, create_contact, update_contact,get_contact, delete_contact
from models.contact_model import ContactCreate, Contact_Read
from mysql.connector import MySQLConnection



app = FastAPI()


@app.get('/')
def test():
    return {"message": "welcome"}


@app.get('/contacts')
def get_contacts(db: MySQLConnection = Depends(get_db)):
    contacts = get_all_contacts(db)
    return contacts


@app.post('/contacts')
def add_contacts(contact: ContactCreate, db: MySQLConnection = Depends(get_db)):
    contact_id = create_contact(db, contact)
    if not contact_id:
        return {"message": "Contact not created, check logs"}
    else:
        return  {"message": "Contact created successfully",
                "id": contact_id}
    
    


@app.put('/contacts/{id}')
def update_contact_by_id(id:int, budy: dict, db: MySQLConnection = Depends(get_db)):
    contact = get_contact(db, id).model_dump()
    for k in budy: 
        if k in contact:
            contact[k] = budy[k]
    contact[id] = id
    u_contact = Contact_Read.model_validate(contact)
    is_update = update_contact(db, u_contact)
    return {"updated": is_update}

    


@app.delete('/contacts/{id}')
def delete_contact_by_id(id: int, db: MySQLConnection = Depends(get_db)):
    is_deleted = delete_contact(db, id)
    return {"deleted": is_deleted}

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)

