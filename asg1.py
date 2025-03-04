import itertools
import tkinter as tk
from tkinter import messagebox
import itertools
import os

def load_dictionary(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def dictionary_attack(username, correct_password, dictionary_file):
    print(f"Attempting dictionary attack for user: {username}...")
    dictionary = load_dictionary("wordlist.txt")
    
    for word in dictionary:
        if word == correct_password:
            print(f"Password found using dictionary attack: {word}")
            return True
    
    print("Dictionary attack failed.")
    return False

def brute_force_attack(correct_password):
    print("Starting brute force attack...")
    
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for attempt in itertools.product(chars, repeat=5):
        attempt_password = ''.join(attempt)
        if attempt_password == correct_password:
            print(f"Password found using brute force: {attempt_password}")
            return True

    print("Brute force attack failed.")
    return False


def main():
    username = input("Enter username: ")
    correct_password = input(f"Set a password for {username}: ")

    dictionary_file = "wordlist.txt"  
    
    if not dictionary_attack(username, correct_password, dictionary_file):
        brute_force_attack(correct_password)

if __name__ == "__main__":
    main()


def load_dictionary(filename):
    if not os.path.exists(filename):
        messagebox.showerror("Error", f"Dictionary file '{filename}' not found.")
        return []
    
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def dictionary_attack(username, correct_password, dictionary_file):
    dictionary = load_dictionary(dictionary_file)

    for word in dictionary:
        if word == correct_password:
            messagebox.showinfo("Success", f"Password found using dictionary attack: {word}")
            return True

    return False

def brute_force_attack(correct_password):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for attempt in itertools.product(chars, repeat=5): 
        attempt_password = "".join(attempt)
        if attempt_password == correct_password:
            messagebox.showinfo("Success", f"Password found using brute force: {attempt_password}")
            return True

    messagebox.showerror("Failure", "Brute force attack failed.")
    return False

def start_attack():
    username = username_entry.get()
    correct_password = password_entry.get()

    if not username or not correct_password:
        messagebox.showwarning("Warning", "Please enter both username and password.")
        return

    dictionary_file = "wordlist.txt"

    if not dictionary_attack(username, correct_password, dictionary_file):
        brute_force_attack(correct_password)
    
    root.destroy()  

#GUI Bonus point
root = tk.Tk()
root.title("Password Cracker")
root.geometry("300x200")

tk.Label(root, text="Enter Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Enter Password:").pack()
password_entry = tk.Entry(root, show="*") 
password_entry.pack()

tk.Button(root, text="Start Attack", command=start_attack).pack()

root.mainloop()
