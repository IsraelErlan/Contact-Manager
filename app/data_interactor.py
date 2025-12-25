from models.contact_model import ContactCreate, Contact_Read
import mysql.connector



def create_contact(db, contact: ContactCreate): # -> int | None
    cursor = db.cursor()
    try:
        cursor.execute('''
            INSERT INTO Contacts 
            (first_name, last_name, phone_number) VALUES (%s, %s, %s) ''',
                (contact.first_name, contact.last_name, contact.phone_number)
                        )    
        db.commit()
        return cursor.lastrowid
    
    except mysql.connector.IntegrityError as e:
        print("Phone number already exist")
        db.rollback()
        return

    except mysql.connector.Error as e:
        print("Mysql error:", e)
        raise

    finally:
        cursor.close()
    



def get_contact(db, contact_id):
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute('''
                                SELECT * 
                                FROM Contacts
                                WHERE id = %s
                                ''' ,
                            (contact_id,))
        row = cursor.fetchone()
        if row is None:
            print("contact not found")
            return None
        
        return Contact_Read(**row)
    
    except mysql.connector.Error as e:
        print("Mysql error:", e)
        raise

    finally:
        cursor.close()


def get_all_contacts(db):
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute('''
                        SELECT * 
                        FROM Contacts
                        ''')
        rows = cursor.fetchall()
        return [Contact_Read(**row) for row in rows]
        
    except mysql.connector.Error as e:
        print("Mysql error:", e)
        raise

    finally:
        cursor.close()
    
    

def update_contact(db, contact: Contact_Read) -> bool:
    cursor = db.cursor()
    try: 
        cursor.execute('''
                    UPDATE Contacts 
                    SET first_name = %s, last_name = %s, phone_number = %s
                    WHERE id = %s
                    ''', 
                    (contact.first_name, contact.last_name, contact.phone_number, contact.id))
        
        row_count = cursor.rowcount
        db.commit()
        return row_count > 0
    
    except mysql.connector.Error as e:
        print("Mysql error:", e)
        db.rollback()
        raise

    finally:
        cursor.close()
    



def delete_contact(db, contact_id: int) -> bool:
    cursor = db.cursor()
    try:
        cursor.execute('''
                    DELETE FROM Contacts 
                    WHERE id = %s
                    ''',
                    (contact_id,))
        row_count = cursor.rowcount
        db.commit()
        return row_count > 0
    
    except mysql.connector.Error as e:
        print("Mysql error:", e)
        db.rollback()
        raise

    finally:
        cursor.close()
    

