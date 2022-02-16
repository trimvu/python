
import pickle
    

phonebook_dict = {}


with open('phonebook_dict.pickle', 'rb') as fh:
    phonebook_dict = pickle.load(fh)

# with open('phonebook_dict.pickle', 'wb') as fh:
#     pickle.dump(phonebook_dict, fh)

phonebookUse = True

while phonebookUse: 
    
    choice = int(input("""
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit

What do you want to do (1-5)?
"""))


    if choice == 1: # look up an entry
        search = str(input('Name: '))
        if search in phonebook_dict:
            print(f'Found entry for {search}: {phonebook_dict[search]}')
        elif search not in phonebook_dict:
            print(f'{search} is not in the phonebook')
        
    elif choice == 2: # set an entry
        setName = str(input("Name: "))
        setNumber = str(input("Number: "))
        phonebook_dict[setName] = setNumber
        print(f"Entry stored for {setName}.")
        
    elif choice == 3: # delete an entry
        search = str(input('Name: '))
        if search in phonebook_dict:
            del phonebook_dict[search]
            print(f'Deleted entry for {search}')
        
    elif choice == 4: # list all entries
        for x in phonebook_dict:
            print(f'Entry found for {x}: {phonebook_dict[x]}')
    
    elif choice == 5: # quit
        with open('phonebook_dict.pickle', 'wb') as fh:
                pickle.dump(phonebook_dict, fh)
        break
    
print('Bye.')
