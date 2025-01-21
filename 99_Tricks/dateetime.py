from datetime import datetime

# Current datetime
now = datetime.now()

# Format specifiers and their descriptions
format_specifiers = {
    "%a": "Abbreviated weekday name",
    "%A": "Full weekday name",
    "%b": "Abbreviated month name",
    "%B": "Full month name",
    "%c": "Locale's date and time representation",
    "%d": "Day of the month (01–31)",
    "%H": "Hour (24-hour clock, 00–23)",
    "%I": "Hour (12-hour clock, 01–12)",
    "%j": "Day of the year (001–366)",
    "%m": "Month as a zero-padded decimal (01–12)",
    "%M": "Minute (00–59)",
    "%p": "Locale’s AM or PM",
    "%S": "Second (00–59)",
    "%U": "Week number (Sunday as the first day of the week, 00–53)",
    "%w": "Weekday as a number (Sunday=0, 0–6)",
    "%W": "Week number (Monday as the first day of the week, 00–53)",
    "%x": "Locale’s date representation",
    "%X": "Locale’s time representation",
    "%Y": "Year with century",
    "%y": "Year without century (00–99)",
    "%Z": "Time zone name (empty string if no time zone is set)",
    "%%": "Literal '%' character",
    "%D": "Equivalent to %m/%d/%y",
}

# Print formatted output for each specifier
print("Datetime:", now)
for specifier, description in format_specifiers.items():
    try:
        print(f"{specifier:5} | {description:50} | {now.strftime(specifier)}")
    except Exception as e:
        print(f"{specifier:5} | {description:50} | Error: {e}")
