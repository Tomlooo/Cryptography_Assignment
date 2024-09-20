#Cryptography Assignment

#Cipher GUI: Vigenère, Playfair, and Hill Ciphers

**Description**
This is a Python-based graphical user interface (GUI) program that allows users to encrypt and decrypt text using the Vigenère Cipher, Playfair Cipher, and Hill Cipher. 
The program supports both direct keyboard input and file upload (in .txt format) and requires the user to input a key of at least 12 characters for both encryption and decryption.

**Features**
-Three Cipher Options: Vigenère, Playfair, and Hill Ciphers.
-Text Input: Enter text directly in the GUI or upload from a .txt file.
-Encryption and Decryption: Both functionalities are supported.
-User-friendly GUI: Built with tkinter for ease of use.

**Requirements**
To run this program, ensure that you have the following installed:
-Python 3.x
-Required Python libraries:
-tkinter (for GUI)
-numpy (for matrix operations in Hill cipher)

**Installation**
1. Clone this repository:
   git clone https://github.com/yourusername/cipher-gui.git
   cd cipher-gui
2. Install the required dependencies: If tkinter and numpy are not installed, you can install them using pip:
   pip install numpy
   -tkinter is part of the standard Python distribution, so it should already be installed. If it's not installed, follow the instructions for your platform to install it:
   -Windows: tkinter is included by default with Python installations.
   -Mac: Install the Python framework version from python.org.
   
**Running The Program**
1. Navigate to the project directory where the script is located:
   cd cipher-gui
2. Run the Python program:
   python cipher_gui.py
3. The GUI will launch, allowing you to:
-Enter text manually or upload a .txt file.
-Input a key of at least 12 characters.
-Select between the Vigenère, Playfair, or Hill cipher.
-Encrypt or decrypt the text, and view the result in the output section.

**Usage**
1. Input Section
You can either type in your text in the provided input area or upload a text file by clicking the Upload File button.
2. Key Section
Input a key (minimum of 12 characters) for encryption or decryption.
3. Cipher Selection
Choose the cipher type (Vigenère, Playfair, or Hill) by selecting the appropriate radio button.
4. Encrypt/Decrypt
Click Encrypt or Decrypt to perform the operation. The resulting text will be displayed in the output section.
