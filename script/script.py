from datetime import datetime
import time
from os import system

class Node:
    def __init__(self, value, link=None):
        self.value = value 
        self.link = link 

    def get_value(self):
        return self.value 

    def get_link(self):
        return self.link 

    def set_link(self, new_link):
        self.link = new_link 


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node 

    def insert_node(self, new_value):
        new_node = Node(new_value)
        new_node.set_link(self.head_node)
        self.head_node = new_node 

    def stringify_lst(self):
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                print(current_node.get_value())                       
            current_node = current_node.get_link()
        
    def remove_node(self, value):
        current_node = self.get_head_node()
        if current_node.get_value() == value:
            self.head_node = current_node.get_link()
        else:
            while current_node:
                next_node = current_node.get_link()
                if next_node.get_value() == value:
                    current_node.set_link(next_node.get_link())
                    current_node = None 
                else:
                    current_node = next_node 

               


playing = True 

print("Welcome to your Word Editor made by Jaival Patel!")
time.sleep(0.5)
prompt1 = input("Please select a user you want to write with! If you currently have no users, please type \"None\": ")
users = []
files = ["Files:" ]
if len(users) == 0:
        print("In order for you to write in this word editor, you must create an account")


while playing:
    user = input()
    if user == "/add_user":
        name = input("Please enter a name for the user: ")
        users.append(name)
        time.sleep(0.5)
        updated_date = datetime.strftime(datetime.now(), " %c ")
        print("User added")
        
        for i in users:
            print(i)

    if user == "/remove_user":
        name = input("Please enter a user you want to remove: ")
        
        if name in users:
            users.remove(name)
            time.sleep(0.5)
            print("The user has been removed")
            
            for i in users:
                print(i)
        else:
            print("That user is not valid!")
            for i in users:
                print(i)
    
    if user == "/select_user":
        for j in users:
                print(j)
        og_prompt = input("Please select a user to work with: ")
        if user != user:
            files = ["Files:" ]
        else:
            pass
        if og_prompt in users:

    
            def home_page():
                print("\n")
                print(updated_date)
                print(files)
            print(home_page())
        
            print("\n")
            file_name = input("Please type /select_file. If you want to add a new file, then please type /add or to go back to the homepage, please type /Home: " )
            print()

            if file_name == "/select_file":
                current_node = og_prompt_docs.get_head_node()
                while current_node:                               
                    for j in files:
                        if name == j:
                            if current_node.get_value() == name:
                                clear = lambda: system('clear')
                                clear()
                                print(current_node.get_value() + "," + updated_date)
                                continue
                            current_node = current_node.get_link() 
                    break
                break
            
            
            if file_name == "/remove_file":
                remove_file = input("Please enter the name of the file you want to remove")
                
                if remove_file in files:
                    og_prompt_docs.remove_node(remove_file)
                    current_node = og_prompt_docs.get_head_node()
                    while current_node:                               
                        for j in files:
                            if name == j:
                                if current_node.get_value() == name:
                                    clear = lambda: system('clear')
                                    clear()
                                    print(current_node.get_value() + "," + updated_date)
                                    continue
                                current_node = current_node.get_link() 
                        break
                    break
                else:
                    print("That file is not there!")
            
            if file_name == "/Home":
                print(home_page())

            if file_name == "/add":
                def add_new_file():
                    og_prompt_docs = LinkedList()
                    name = input("Please enter a name for the file: ")
                    clear = lambda: system('clear')
                    clear()
                    
                    print("{file},{datetime}:".format(file=name, datetime=updated_date))
                    og_prompt_docs.insert_node(str(name))
                    #print(og_prompt_docs.peek())
                    files.append(name)
            
                    
                    while True:
                        #file_name = file_name
                        file_prompt = input()
                        
                        if file_prompt == "/Choose_File":               
                            for i in files:
                                print(i)

                
                            name = input("Please enter a name for the file: ")

                            current_node = og_prompt_docs.get_head_node()
                            while current_node:                               
                                for j in files:
                                    if name == j:
                                        if current_node.get_value() == name:
                                            clear = lambda: system('clear')
                                            clear()
                                            print(current_node.get_value() + "," + updated_date)
                                            continue
                                        current_node = current_node.get_link() 
                                break
                            break          
                add_new_file()

            else:
                pass
            
            
                

            

            
          

        else:
            print('That name is not valid')
        

        
        
            


    
    
    
    
    

    