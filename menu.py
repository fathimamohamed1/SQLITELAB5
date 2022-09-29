"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3
db='first_db.sqlite'



with sqlite3.connect('first_db.sqlite') as conn:

    conn.execute('CREATE TABLE IF NOT EXISTS records ( name text , country text , number_of_catches int  )') 
    
    def main():
        menu_text = """
        1. Display all records
        2. Add new record
        3. Edit existing record
        4. Delete record 
        5. Quit
        """

        while True:
            print(menu_text)
            choice = input('Enter your choice: ')
            if choice == '1':
                display_all_records()
            elif choice == '2':
                add_new_record()
            elif choice == '3':
                edit_existing_record()
            elif choice == '4':
                delete_record()
            elif choice == '5':
                break
            else:
                print('Not a valid selection, please try again')

    def create_table():


        with sqlite3.connect(db) as conn:
          conn.execute('CREATE TABLE IF NOT EXISTS records ( name text , country text , number_of_catches int  )')
       
        conn.commit()
        conn.close()



    def display_all_records():
        conn=sqlite3.connect(db)
        results = conn.execute('SELECT * FROM records')
         
        for row in results:
            print(row) # row is a tuple
        print('displaying all records')


    def add_new_record():
        new_name= input('enter new name:')
        new_country= input ('enter a new country:')
        new_catches = int(input('enter the number_of_catches:'))

        with sqlite3.connect(db) as conn:   
         conn.execute(f'INSERT INTO records VALUES (?,?,?)', (new_name,new_country,new_catches))

        conn.commit()
        conn.close()
        print('Record has been added successfully')


    def edit_existing_record():
        update_name='Aaron'
        update_catches='88'

        with sqlite3.connect(db) as conn:   
         conn.execute( 'UPDATE records set number_of_catches = ? WHERE name =?', (update_name,update_catches))

        conn.commit()
        conn.close()
        print('Record has been updated successfully ') 


    def delete_record(name):
        with sqlite3.connect(db) as conn:   
         conn.execute("DELETE FROM records WHERE name = Chad", (name,))

        print('record has been deleted sucessfully ') 
        
        conn.commit()
        conn.close()
    if __name__ == '__main__':
        main()