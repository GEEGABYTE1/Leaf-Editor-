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

og_prompt_docs = LinkedList("Files: ")
while playing:
    text1 = ""
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
            og_prompt_docs = Linked_list("Files: ")
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
                f_name = input("Please enter the name of the file: ")

                while True:
                    if len(text1) == 0:
                        while current_node:                               
                            for j in files:
                                if f_name == j:
                                    if current_node.get_value() == f_name:
                                        clear = lambda: system('clear')
                                        clear()
                                        #print(current_node.get_value() + "," + updated_date)
                                        f = open(str(f_name),"r")
                                        if f.mode == "r":
                                            contents = f.read()
                                            print(contents)
                                            #f = open(str(f_name), "a")
                                            
                                            #f.write(new_input)
                                            #f.close()

                                        continue
                                    current_node = current_node.get_link() 
                            break
                    
                    new_input = input()

                    
                    if new_input != "/home":
                        text1 += str(new_input)
                    else:
                        pass
                    if new_input != "/save_file" or new_input != "/save_file ":
                        if user != "/add_user":
                            if user != "/select_user":
                                if user != "remove_user":
                                    text += str(user)
                    else:
                        pass
                    if new_input == "/save_file":
                        f = open(str(f_name), "a")
                        f.write(text1)
                        f.close()

                    if new_input == "/home":
                        print(home_page())
                        break

                
                
                
            
            
            if file_name == "/remove_file":
                remove_file = input("Please enter the name of the file you want to remove: ")
                
                if remove_file in files:
                    og_prompt_docs.remove_node(remove_file)
                    current_node = og_prompt_docs.get_head_node()
                    clear = lambda: system('clear')
                    clear()
                    print(home_page())
                                    
                else:
                    print("That file is not there!")
            
            if file_name == "/Home":
                print(home_page())

            if file_name == "/add":
                def add_new_file():
                    name = input("Please enter a name for the file: ")
                    og_prompt_docs.insert_node(str(name))
                    files.append(name)
                    #print(og_prompt_docs.stringify_lst())
                    text = ""
                    clear = lambda: system('clear')
                    clear()

                    
                    print("{file},{datetime}:".format(file=name, datetime=updated_date))
                    
                    
                    #print(og_prompt_docs.peek())
                    
                    
                    
                    
                    while True:
                        #file_name = file_name
                        #f = open(str(name), "w+")
                        file_prompt = input()
                        
                        if file_prompt != "/Choose_File":
                            if file_prompt != "/save_file" or file_name != "/save_file ":
                                text += file_prompt  
                        else:
                            pass
                        
                        
                        if file_prompt == "/Choose_File":               
                            for i in files:
                                print(i)

                
                            name = input("Please enter a name for the file: ")

                            if name in files:

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
                                print("That file is not valid!")

                        if file_prompt == "/save_file":
                            for i in files:
                                print(i)
                            print("\n")
                            name_file = input("Please enter a name for the file: ")
                            f = open(str(name_file), "a")
                            for i in range(1):
                                f.write(str(text))
                            f.close()

                add_new_file()

            else:
                print("The command is invalid")
                print(input("Please type /select_file. If you want to add a new file, then please type /add or to go back to the homepage, please type /Home: " ))
            
            
                

            

            
          

        else:
            print('That name is not valid')
        

        
        
            


    
    
    
    
    

    