import os
import time
import pyfiglet  #pip install pyfiglet
from colorama import Fore
from subprocess import call

Message = 'Happy New Year 2021'
Front = 'slant'

def clear():
    _ = call('clear' if os.name=='posix' else 'cls', shell=True)

def print_nye_to_console():
    f = pyfiglet.Figlet(font=Front)
    clear()
    for col in [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.YELLOW] * 10 + [Fore.WHITE]:
        print(col + f.renderText(Message))
        print(fireworks_display)
        time.sleep(0.05)
        clear()

fireworks_display = \
"""
                                 .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

if __name__ == '__main__':
    print_nye_to_console()