from art import *
from colorama import Fore, Back, Style

tprint("Text ART")

print(Fore.CYAN)
tprint("BELIEVE", font='block', chr_ignore=True)
tprint("AND", font='block')
tprint("ACHEIVE", font='block', chr_ignore=True)
print(Style.RESET_ALL)

tprint("HELLO", font='sub-zero', chr_ignore=True)

tprint("HAPPY HOLIDAY", font="rnd-medium")
tprint("HAPPY", font="rnd-xlarge")
tprint("Ring","mix")

print(Fore.RED + Back.WHITE)
tprint("HI", font="large")
print(Style.RESET_ALL)

print(decor("barcode1"))

print("\n"+ Back.WHITE + Style.DIM + Fore.LIGHTGREEN_EX +"H"+ Style.DIM +"E"+ Fore.LIGHTMAGENTA_EX + Style.BRIGHT +"L"+ 
      Fore.WHITE + Style.BRIGHT +"L"+ Fore.RED +"O !!" + Style.RESET_ALL)