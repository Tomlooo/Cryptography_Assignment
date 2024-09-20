import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

def vigenere_encrypt(plaintext, key):
    key = key.upper()
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i].upper()
        if char.isalpha():
            ciphertext += chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    key = key * (len(ciphertext) // len(key)) + key[:len(ciphertext) % len(key)]
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i].upper()
        if char.isalpha():
            plaintext += chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        else:
            plaintext += char
    return plaintext

def create_playfair_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = "".join(sorted(set(key), key=lambda x: key.index(x)))
    table = [x for x in key.upper() if x in alphabet]
    table += [x for x in alphabet if x not in table]
    return np.array(table).reshape(5, 5)

def find_position(table, letter):
    index = np.where(table == letter)
    return index[0][0], index[1][0]

def playfair_encrypt(plaintext, key):
    table = create_playfair_table(key)
    plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  
    ciphertext = ""
    
    i = 0
    while i < len(plaintext):
        char1, char2 = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(table, char1)
        row2, col2 = find_position(table, char2)

        if row1 == row2:
            ciphertext += table[row1][(col1 + 1) % 5]
            ciphertext += table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[(row1 + 1) % 5][col1]
            ciphertext += table[(row2 + 1) % 5][col2]
        else:
            ciphertext += table[row1][col2]
            ciphertext += table[row2][col1]
        i += 2
    return ciphertext

def playfair_decrypt(ciphertext, key):
    table = create_playfair_table(key)
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(table, char1)
        row2, col2 = find_position(table, char2)

        if row1 == row2:
            plaintext += table[row1][(col1 - 1) % 5]
            plaintext += table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[(row1 - 1) % 5][col1]
            plaintext += table[(row2 - 1) % 5][col2]
        else:
            plaintext += table[row1][col2]
            plaintext += table[row2][col1]
        i += 2
    return plaintext

def hill_encrypt(plaintext, key_matrix):
    plaintext_vector = np.array([ord(char) - ord('A') for char in plaintext.upper()])
    ciphertext_vector = np.dot(key_matrix, plaintext_vector) % 26
    ciphertext = ''.join(chr(x + ord('A')) for x in ciphertext_vector)
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    inverse_key = np.linalg.inv(key_matrix).astype(int) % 26
    ciphertext_vector = np.array([ord(char) - ord('A') for char in ciphertext.upper()])
    plaintext_vector = np.dot(inverse_key, ciphertext_vector) % 26
    plaintext = ''.join(chr(x + ord('A')) for x in plaintext_vector)
    return plaintext

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ciphers: Vigenère, Playfair, Hill")
        self.root.geometry("600x500")

        self.input_label = tk.Label(root, text="Input Text")
        self.input_label.pack()
        self.input_text = tk.Text(root, height=5, width=50)
        self.input_text.pack()

        self.key_label = tk.Label(root, text="Key (min 12 characters)")
        self.key_label.pack()
        self.key_entry = tk.Entry(root, width=50)
        self.key_entry.pack()

        self.cipher_choice = tk.StringVar(value="vigenere")
        self.vigenere_radio = tk.Radiobutton(root, text="Vigenère Cipher", variable=self.cipher_choice, value="vigenere")
        self.playfair_radio = tk.Radiobutton(root, text="Playfair Cipher", variable=self.cipher_choice, value="playfair")
        self.hill_radio = tk.Radiobutton(root, text="Hill Cipher", variable=self.cipher_choice, value="hill")

        self.vigenere_radio.pack(anchor=tk.W)
        self.playfair_radio.pack(anchor=tk.W)
        self.hill_radio.pack(anchor=tk.W)

        self.upload_button = tk.Button(root, text="Upload File", command=self.upload_file)
        self.upload_button.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack()

        self.output_label = tk.Label(root, text="Output Text")
        self.output_label.pack()
        self.output_text = tk.Text(root, height=5, width=50)
        self.output_text.pack()

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                data = file.read()
                self.input_text.delete(1.0, tk.END)
                self.input_text.insert(tk.END, data)

    def encrypt_text(self):
        plaintext = self.input_text.get(1.0, tk.END).strip()
        key = self.key_entry.get().strip()
        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long.")
            return
        cipher_choice = self.cipher_choice.get()
        
        if cipher_choice == "vigenere":
            ciphertext = vigenere_encrypt(plaintext, key)
        elif cipher_choice == "playfair":
            ciphertext = playfair_encrypt(plaintext, key)
        elif cipher_choice == "hill":
            # Example key matrix for Hill Cipher
            key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
            ciphertext = hill_encrypt(plaintext, key_matrix)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, ciphertext)

    def decrypt_text(self):
        ciphertext = self.input_text.get(1.0, tk.END).strip()
        key = self.key_entry.get().strip()
        if len(key) < 12:
            messagebox.showerror("Error", "Key must be at least 12 characters long.")
            return
        cipher_choice = self.cipher_choice.get()
        
        if cipher_choice == "vigenere":
            plaintext = vigenere_decrypt(ciphertext, key)
        elif cipher_choice == "playfair":
            plaintext = playfair_decrypt(ciphertext, key)
        elif cipher_choice == "hill":
            key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
            plaintext = hill_decrypt(ciphertext, key_matrix)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, plaintext)

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
