from colorama import Fore
from autosage import Poe

if __name__ == '__main__':
    mychat = Poe(
        name_session='my_account',
        email='hi@outlook.es'
    )
    mychat.connect()

    code = input('Send the code receive in email: ')
    mychat.send_verification_code(code)

    while True:
        prompt = str(input(Fore.BLUE + 'Me: ' + Fore.RESET))
        answer = mychat.sage(prompt=prompt)

        print(Fore.GREEN + 'AutoSage: ' + answer + Fore.RESET)
