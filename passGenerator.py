"""
A simple password genrator.
"""
import names
import random
import string
import time
from tqdm import tqdm

def main():
    while True:
        wantedPass = input("\n[w]Weak password\n[s]Strong password!\n[b]To Stop the Program!\n\nPlease select one of the option above for the password you need to be genearted:")
        print(f'you have selected: {wantedPass}')

        if wantedPass.lower() == 'b':
            print('Exiting the program!')
            break
            [time.sleep(0.2) for _ in tqdm(range(200))]
            print("Program Terminated!")

        if wantedPass.lower() == 'w':
            pwd = (names.get_first_name('male')) + (names.get_first_name('female'))
            print('Your password is: ' + pwd)
        if wantedPass.lower() == 's':
            pwd = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(16)])
            print('Your password is: ' + pwd)

__name__ =='__main__:'
main()

