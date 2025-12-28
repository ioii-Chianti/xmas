import time
import os
import random
import sys

COLORS = {
    'R': '\033[91m',
    'G': '\033[92m',
    'Y': '\033[93m',
    'B': '\033[94m',
    'M': '\033[95m',
    'C': '\033[96m',
    'W': '\033[97m',
    'END': '\033[0m'
}

tree_shape = [
    "                    ⭐ ",
    "                   *** ",
    "                  ***** ",
    "                 ******* ",
    "                ********* ",
    "               *********** ",
    "              ************* ",
    "             *************** ",
    "            ***************** ",
    "           ******************* ",
    "          ********************* ",
    "         *********************** ",
    "        ************************* ",
    "       *************************** ",
    "      ***************************** ",
    "     ******************************* ",
    "    ********************************* ",
    "   *********************************** ",
    "  ************************************* ",
    " *************************************** ",
    "*****************************************",
    "                 |||||                   ",
    "                 |||||                   ",
    "                 |||||                   ",
    "                 |||||                   "
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_tree():
    output_buffer = ""
    
    for line in tree_shape:
        new_line = ""
        for char in line:
            if char == '⭐':
                new_line += COLORS['Y'] + "⭐" + COLORS['END']
            elif char == '*':
                if random.random() > 0.15:
                    new_line += COLORS['G'] + "*" + COLORS['END']
                else:
                    color = random.choice([COLORS['R'], COLORS['Y'], COLORS['B'], COLORS['M'], COLORS['C'], COLORS['W']])
                    new_line += color + "●" + COLORS['END']
            elif char == '|':
                new_line += COLORS['W'] + "|" + COLORS['END']
            else:
                new_line += char
        output_buffer += new_line + "\n"
    
    output_buffer += "\n" + COLORS['Y'] + "   🎄 Merry Christmas OuO 🎄" + COLORS['END']
    print(output_buffer)

def main():
    try:
        time.sleep(1)
        while True:
            clear_console()
            draw_tree()
            time.sleep(0.3)
    except KeyboardInterrupt:
        clear_console()
        print(COLORS['R'] + "聖誕快樂！" + COLORS['END'])
        sys.exit()

if __name__ == "__main__":
    main()