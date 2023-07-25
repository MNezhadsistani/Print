import colorama
from colorama import init,Fore,Back,Style
init(autoreset=True)
#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL
print(Fore.BLUE+Back.WHITE+"init(autoreset = True) Setting this to True will reset color and style settings after each line.")
print(Style.BRIGHT+Fore.CYAN+"*************************************************")
print(Style.BRIGHT+Fore.RED+Style.BRIGHT+"Hello World")
print(Style.BRIGHT+Fore.CYAN+"*************************************************")




