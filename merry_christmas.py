import random
import time
import sys
from colorama import Fore, init

init(autoreset=True)
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.WHITE, Fore.BLUE]
tree_layers = [
    "       * ",
    "      *** ",
    "     ***** ",
    "    ******* ",
    "   ********* ",
    "  *********** ",
    " ************* ",
]
trunk = "      | |      "

try:
    while True:
        sys.stdout.write("\033[H\033[J")
        tree_drawing = "\n"
        for layer in tree_layers:
            colored_layer = ""
            for char in layer:
                if char == '*':
                    colored_layer += random.choice(colors) + char
                else:
                    colored_layer += char
            tree_drawing += colored_layer + "\n"

        tree_drawing += (Fore.YELLOW + trunk + "\n")
        tree_drawing += (Fore.YELLOW + trunk + "\n")
        tree_drawing += "\nPress CTRL + C to stop."

        # Print the finished tree all at once for a smooth animation
        sys.stdout.write(tree_drawing)
        sys.stdout.flush()

        # Pause before the next frame
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n\nAnimation stopped.")