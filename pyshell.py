import os
import sys
import time
pyshellver = 0.1
pyshellinfo = str("PyShell Command line shell - Python Shell built with python")
print(pyshellinfo)

pyshcommands = {
    "exit":"exit()",
    "quit":"quit()",
    "pyshfo":"print(pyshellinfo)",
    "pyshver":"print(pyshellver)",
    "clear":"os.system('clear')",
    "print(inputtedcommand)":"print('This is an interpreter-required variable. Please do not tamper with it')",
    "print(pyshcommands)":"print('This is an interpreter-required variable. Please do not tamper with it')",
    "print(i_t_e_m)":"print('This is an interpreter-required variable. Please do not tamper with it')"
}
def commandie():
    global inputtedcommand
    inputtedcommand = str(input(">>> "))
    if inputtedcommand == "": return;
    for i_t_e_m in pyshcommands:
        if inputtedcommand == i_t_e_m:
            eval(pyshcommands[i_t_e_m])
            return;
    print("pysh: ", inputtedcommand, " is not defined")
while True:
    commandie()