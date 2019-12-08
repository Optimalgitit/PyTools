import os
import sys
import time
pypythonver = 0.1
pypython = str("PyPython interpreter- Python interpreter built with python")
print(pypython)
customcommands = {
    "exit":"exit()",
    "quit":"quit()",
    "pypver":"print(pypython)",
    "clear":"os.system('clear')",
    "print(inputtedcommand)":"print('This is an interpreter-required variable. Please do not tamper with it')",
    "print(customcommands)":"print('This is an interpreter-required variable. Please do not tamper with it')",
    "print(i_t_e_m)":"print('This is an interpreter-required variable. Please do not tamper with it')"
}
def commandie():
    global inputtedcommand
    inputtedcommand = str(input(">>> "))
    if inputtedcommand == "": return;
    for i_t_e_m in customcommands:
        if inputtedcommand == i_t_e_m:
            eval(customcommands[i_t_e_m])
            return;
    eval(inputtedcommand);
while True:
    commandie()