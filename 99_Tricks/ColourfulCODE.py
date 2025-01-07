def print_colored_text():
    colors = {
        "Black": "\033[30m",
        "Red": "\033[31m",
        "Green": "\033[32m",
        "Yellow": "\033[33m",
        "Blue": "\033[34m",
        "Magenta": "\033[35m",
        "Cyan": "\033[36m",
        "White": "\033[37m",
        "Bright Black": "\033[90m",
        "Bright Red": "\033[91m",
        "Bright Green": "\033[92m",
        "Bright Yellow": "\033[93m",
        "Bright Blue": "\033[94m",
        "Bright Magenta": "\033[95m",
        "Bright Cyan": "\033[96m",
        "Bright White": "\033[97m"
    }

    for color, code in colors.items():
        print(f"{code}{color}\033[0m")
        print("\033[33mhello\033[0m")


print_colored_text()
