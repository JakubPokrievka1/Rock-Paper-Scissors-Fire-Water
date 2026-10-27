#!/usr/bin/python3

# NOTE: This code is coded for it to be run from the Linux terminal in mind.

def main():
    # Main function, where all the code/functions are stringed together. 

    import tkinter as tk
    import random
    from tkinter.constants import W
    
    def close_program():
        # This function allows for the program to be graphically stopped by 'root.destroy()', if the user clicks the option to end the program.

        if user_choice.get() == 'Stop Program':
            print('Ok. The Program Has Been Stopped!')
            root.destroy()
    

    def choice_checker():
        # Function that is used to store the user choice for each round and who to decide wins, until the user clicks the option to stop the program.

        choice = user_choice.get()

        words = ["Rock", "Paper", "Scissor", "Fire", "Water"]
        computer_choice = random.choice(words) 

        if choice == "Rock" and computer_choice == "Scissor":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'User Wins!\n')

        elif choice == "Scissor" and computer_choice == "Paper":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'User Wins!\n')

        elif choice == "Paper" and computer_choice == "Rock":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'User Wins!\n')
        
        elif choice == "Water" and computer_choice == "Fire":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'User Wins!\n')
        
        elif choice == "Water" and computer_choice != "Fire":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'Computer Wins!\n')
        
        elif choice == "Fire" and computer_choice == "Water":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'Computer Wins!\n')
        
        elif choice == "Fire" and computer_choice != "Water":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'User Wins!\n')

        elif computer_choice == "Water" and choice == "Fire":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'Computer Wins!\n')
        
        elif computer_choice == "Water" and choice != "Fire":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'User Wins!\n')
        
        elif computer_choice == "Fire" and choice == "Water":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'User Wins!\n')

        elif computer_choice == "Fire" and choice != "Water":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'Computer Wins!\n')

        elif computer_choice == "Rock" and choice == "Scissor":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'Computer Wins!\n')

        elif computer_choice == "Scissor" and choice == "Paper":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'Computer Wins!\n')

        elif computer_choice == "Paper" and choice == "Rock":
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'Computer Wins!\n')
        
        elif computer_choice == choice:
            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'It Is A Draw!\n')

        else:
            # This part of the code is for logic error debugging - Ignore this for most part, unless it gets triggered.

            T = tk.Text(root, height=2, width=30)
            T.pack()
            T.insert(tk.END, 'Whoops! Logic Error!\n')
            print(computer_choice)

    root = tk.Tk() 
    user_choice = tk.StringVar(master=root, value="")


    # These buttons define what each of the options mean that are clicked by the user, and are stored in the 'user_choice' variable. 
    # Each of these buttons fill the variable 'user_choice', with the string that will be used to compare the result of the choice of the computer.
    tk.Radiobutton(root, text='Rock', variable=user_choice, value='Rock').pack(anchor=W)
    tk.Radiobutton(root, text='Paper', variable=user_choice, value='Paper').pack(anchor=W)
    tk.Radiobutton(root, text='Scissor', variable=user_choice, value='Scissor').pack(anchor=W) 
    tk.Radiobutton(root, text='Fire', variable=user_choice, value='Fire').pack(anchor=W)
    tk.Radiobutton(root, text='Water', variable=user_choice, value='Water').pack(anchor=W)
    tk.Radiobutton(root, text='Select This Option To Stop The Program', variable=user_choice, value='Stop Program', command=close_program).pack(anchor=W)
    tk.Button(root, text="Confirm Choice", command=choice_checker).pack()



    root.mainloop() # Allows for the code for the GUI to be consistently looped, making sure it only ends when the user wants for it to end. 

# Calls the main function
# As all of the functions/code is inside the main function, the program starts when the main 

main() 
