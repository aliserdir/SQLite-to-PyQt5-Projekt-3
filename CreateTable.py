import sqlite3 as sql

def main():
    try: 
        conn = sql.connect('TelefonDaten.db')
        cur = conn.cursor()
        query = "CREATE TABLE if not exists Personen (id INT, vorname TEXT, nachname TEXT, stadt TEXT, telefon TEXT, email TEXT)"

        cur.execute(query)
        print("Table Created Succesfully")

    except sql.Error as e:
        print("There is a table or an error has occurred")

    finally:
        conn.close()
        
if __name__ == "__main__":
    main()