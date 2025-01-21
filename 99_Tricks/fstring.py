# Master Python File: fstrings_and_frstrings_examples.py

# f-strings examples

# fstring_example_1: Basic f-string example with variables
def fstring_example_1():
    name = "Janeesh"
    age = 25
    greeting = f"Hello, my name is {name} and I am {age} years old."
    return greeting


# fstring_example_2: f-string with calculations
def fstring_example_2():
    a = 10
    b = 5
    result = f"The sum of {a} and {b} is {a + b}."
    return result


# fstring_example_3: f-string with function result
def fstring_example_3():
    def multiply(x, y):
        return x * y

    result = f"The result of multiplying 5 and 6 is {multiply(5, 6)}."
    return result


# fstring_example_4: f-string with formatted numbers
def fstring_example_4():
    pi = 3.14159
    formatted_pi = f"Pi rounded to 2 decimal places: {pi:.2f}"
    return formatted_pi


# fstring_example_5: f-string with dynamic expressions
def fstring_example_5():
    x = 2
    y = 3
    expression = f"Result of {x} raised to the power of {y}: {x ** y}"
    return expression


# Raw f-strings (fr-strings) examples

# frstring_example_1: Using fr-string for raw string with formatting
def frstring_example_1():
    path = r"C:\Users\Janeesh\Documents\Projects"
    message = fr"The project folder is located at {path}."
    return message


# frstring_example_2: fr-string with multiple backslashes
def frstring_example_2():
    regex = r"\d{2,4}-\d{2}-\d{2}"
    formatted_regex = fr"The regex for date format is {regex}."
    return formatted_regex


# frstring_example_3: fr-string with variables
def frstring_example_3():
    folder_name = "Data"
    file_name = "report.txt"
    message = fr"File path: C:\Users\Janeesh\Documents\{folder_name}\{file_name}"
    return message


# frstring_example_4: fr-string with dynamic formatting
def frstring_example_4():
    width = 10
    height = 20
    message = fr"The area of the rectangle is {width * height}."
    return message


# frstring_example_5: fr-string with special characters
def frstring_example_5():
    special_char = r"\t"
    formatted_message = fr"Special character: {special_char}"
    return formatted_message


# Main function to run all examples
def main():
    # Running f-string examples
    print("F-String Examples:")
    print(fstring_example_1())
    print(fstring_example_2())
    print(fstring_example_3())
    print(fstring_example_4())
    print(fstring_example_5())
    print()

    # Running fr-string examples
    print("Raw f-String (fr-String) Examples:")
    print(frstring_example_1())
    print(frstring_example_2())
    print(frstring_example_3())
    print(frstring_example_4())
    print(frstring_example_5())


if __name__ == "__main__":
    main()
