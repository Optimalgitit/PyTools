import os
import sys
import time
pypythonver = 0.1
pypython = str("PyPython interpreter- Python interpreter built with python")
print(pypython)
def e_x_i_t():
    print("Next time, use sys.exit()!")
    exit()
customcommands = {
    "exit":"e_x_i_t()",
    "quit":"e_x_i_t()",
    "pypfo":"print(pypython)",
    "pypver":"print(pypythonver)",
    "clear":"os.system('clear')",
    "print(inputtedcommand)":"print('This is an interpreter-required variable. Please do not tamper with it')",
    "print(customcommands)":"print('This is an interpreter-required variable. Please do not tamper with it')",
    "print(i_t_e_m)":"print('This is an interpreter-required variable. Please do not tamper with it')",
    "ls":"print('You are in the python shell.')"
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
    try:
        commandie()
    except NameError as e:
        print(f"{inputtedcommand}is not a command, mathematical equation, function, or a valid syntax for the command you just tried to use. ({e})")
    except EOFError:
        print("\nUse sys.exit() next time!")
        sys.exit()
    except KeyboardInterrupt:
        print("\nUse sys.exit() next time!")
        sys.exit()
