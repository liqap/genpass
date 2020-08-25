import pyfiglet
from colorama import init, Fore
import random
from string import digits
from string import punctuation
from string import ascii_letters

banner = pyfiglet.figlet_format("genpass")
print(Fore.GREEN + banner)
print("Автор: @neoivan")

symbols = digits + punctuation + ascii_letters
sec_random = random.SystemRandom()
password = ''.join(sec_random.choice(symbols) for i in range(15))
print(f'Ваш новый пароль высокой сложности: {password}')
