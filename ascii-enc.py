#!/usr/bin/env python3
import sys

# Color codes
GREEN="\033[32m"
RED="\033[31m"
BLUE="\033[34m"
CYAN="\033[36m"
WHITE="\033[37m"
YELLOW="\033[33m"
PURPLE="\033[35m"
BOLD="\033[1m"
RESET="\033[0m"

def encode_string(s: str) -> str:
    """Encode a string to ASCII numbers joined together"""
    return ''.join(str(ord(c)) for c in s)

def encode_list(s: str):
    """Encode a string to list format"""
    for c in s:
        print(f"{c} -> {ord(c)}")

def decode_ascii(ascii_str: str) -> str:
    """Decode continuous ASCII digits back to text"""
    decoded = ""
    num = ""
    for ch in ascii_str:
        num += ch
        if int(num) in range(32, 127):
            decoded += chr(int(num))
            num = ""
    return decoded

def show_help():
    print(f"""
{BOLD}{CYAN}ascii encoder CLI help{RESET}
{YELLOW}Usage:{RESET}
  {GREEN}encoder.py{RESET} [options] [string/ascii]

{YELLOW}Options:{RESET}
  {GREEN}-l [string]{RESET}    Encode as list format
  {GREEN}-r [ascii]{RESET}     Decode ASCII numbers to text
  {GREEN}-h{RESET}             Show this help menu

{YELLOW}Examples:{RESET}
  {GREEN}./encoder.py hello{RESET}        → Encode "hello" as one line
  {GREEN}./encoder.py -l hello{RESET}     → Encode "hello" as a list
  {GREEN}./encoder.py -r 104101108108111{RESET} → Decode back to text
  {RED}https://github.com/Szerwigi1410/Text-to-ascii-encoder{RESET}             →github
""")

def interactive_mode():
    print("Welcome to" + BOLD + GREEN + " a" + RED + "s" + BLUE + "c" + CYAN + "i" + PURPLE + "i " + WHITE + "encoder!" + RESET)

    question = input("Do you want to encode a sentence like a list? " + BOLD + "(y/n): " + RESET)

    if question == "y":
        sentence = input(BOLD + "Enter your sentence: " + RESET)
        encode_list(sentence)
    else:
        question1 = input("Do you want to encode a sentence like a string? " + BOLD + "(y/n): " + RESET)
        if question1 == "n":
            print("Bye!")
            exit()
        else:
            ascii = input(BOLD + "Enter your sentence: " + RESET)
            print(encode_string(ascii))

def main():
    args = sys.argv[1:]

    if not args:
        interactive_mode()
        return

    if args[0] == "-h":
        show_help()
        return

    if args[0] == "-l" and len(args) > 1:
        encode_list(args[1])
    elif args[0] == "-r" and len(args) > 1:
        print(decode_ascii(args[1]))
    else:
        print(encode_string(args[0]))

if __name__ == "__main__":
    main()
