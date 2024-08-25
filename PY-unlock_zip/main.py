from zipfile import ZipFile, BadZipFile
from string import ascii_letters, digits
import itertools

def zip_unlock_1d(file_name):
    """
    this can be only used for password of length one
    """
    total_str = digits + ascii_letters
    current_password_index = 0

    with ZipFile(file_name, 'r') as protected_file:
            while(True):
                try:
                    protected_file.extractall(pwd=bytes(total_str[current_password_index], encoding='utf-8'))
                    break
                except RuntimeError as e:
                    #print("Wrong password!")
                    current_password_index += 1
            print("The password is: "+total_str[current_password_index])
#zip_unlock_1d("protected.zip")



def unlock_zip(file_name, max_length=8):
    """
    itertools.product generates all possible combinations of characters up to the specified max_length.
    So his method allows trying passwords of varying lengths.
    """
    characters = ascii_letters + digits 
    
    with ZipFile(file_name, 'r') as zip_file:
        for length in range(1, max_length + 1):
            for password_tuple in itertools.product(characters, repeat=length):
                password = ''.join(password_tuple)
                try:
                    print(f"Trying the sequence: {password}")
                    zip_file.extractall(pwd=bytes(password, 'utf-8'))
                    print(f"The password is: {password}")
                    return
                except (RuntimeError, BadZipFile):
                    continue
        print("Password not found within the given length limit.")

# Usage
unlock_zip("protected.zip")
