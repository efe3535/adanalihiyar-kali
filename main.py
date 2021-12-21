from colorama import *

print(f"""
{Fore.RED} _              _
{Fore.LIGHTRED_EX}| | _____  _ __| |__
{Fore.YELLOW}| |/ / _ \| '__| '_ \\
{Fore.BLUE}|   < (_) | |  | |_) |
{Fore.MAGENTA}|_|\_\___/|_|  |_.__/{Fore.RESET}
""")

print(f"{Fore.MAGENTA} RTE Ahiret sinavina hos geldiniz bayim, cay kahve?!{Fore.RESET}\n")

x = input("?\t")

if x.lower()=="cay":
    print(f"{Fore.GREEN}Evet{Fore.RESET}, cumhurbaskanimiz size {Fore.RED}cayinizi{Fore.RESET} firlatmak icin nerede sorun varsa orada olacaktir. Su an kendisi dolara yumruk atmakla mesgul oldugundan sizinle danismanlarindan biri ilgilenecektir.")

else:
    print(f"{Fore.RED}Cumhurbaskanimiz {Fore.MAGENTA}cay icmeyenleri{Fore.RED} sevmez, size bir Karadeniz turkusu tutturma cezasi veriyor.{Fore.RESET}")
