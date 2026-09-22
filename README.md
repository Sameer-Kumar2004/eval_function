# Python `eval()`, Command-Line Arguments & Format Specifiers

A beginner-friendly reference for three important Python topics:

1. [`eval()`](#1-eval-function-in-python)
2. [Command-Line Arguments](#2-command-line-arguments-in-python)
3. [Format Specifiers](#3-format-specifiers-in-python)

---

## Table of Contents

- [1. `eval()` Function in Python](#1-eval-function-in-python)
  - [What is `eval()`?](#what-is-eval)
  - [Syntax](#syntax)
  - [Basic Example](#basic-example)
  - [Using Variables](#using-variables)
  - [Using `eval()` with User Input](#using-eval-with-user-input)
  - [Evaluating Mathematical Expressions](#evaluating-mathematical-expressions)
  - [Using `eval()` with Lists, Tuples and Dictionaries](#using-eval-with-lists-tuples-and-dictionaries)
  - [Using `eval()` with `globals` and `locals`](#using-eval-with-globals-and-locals)
  - [`eval()` vs `int()`](#eval-vs-int)
  - [`eval()` vs `exec()`](#eval-vs-exec)
  - [Why `eval()` Can Be Dangerous](#why-eval-can-be-dangerous)
  - [When to Avoid `eval()`](#when-to-avoid-eval)
  - [Safer Alternatives](#safer-alternatives)
- [2. Command-Line Arguments in Python](#2-command-line-arguments-in-python)
  - [What Are Command-Line Arguments?](#what-are-command-line-arguments)
  - [Running a Python File](#running-a-python-file)
  - [Using `sys.argv`](#using-sysargv)
  - [Important `sys.argv` Rules](#important-sysargv-rules)
  - [Example with One Argument](#example-with-one-argument)
  - [Example with Multiple Arguments](#example-with-multiple-arguments)
  - [Arguments Are Strings](#arguments-are-strings)
  - [Converting Arguments to Numbers](#converting-arguments-to-numbers)
  - [Checking Number of Arguments](#checking-number-of-arguments)
  - [Handling Missing Arguments](#handling-missing-arguments)
  - [Arguments Containing Spaces](#arguments-containing-spaces)
  - [Using `argparse`](#using-argparse)
  - [`sys.argv` vs `argparse`](#sysargv-vs-argparse)
- [3. Format Specifiers in Python](#3-format-specifiers-in-python)
  - [What Is a Format Specifier?](#what-is-a-format-specifier)
  - [F-Strings](#f-strings)
  - [Basic Formatting](#basic-formatting)
  - [Decimal Places](#decimal-places)
  - [Width and Alignment](#width-and-alignment)
  - [Fill Characters](#fill-characters)
  - [Sign](#sign)
  - [Zero Padding](#zero-padding)
  - [Thousands Separators](#thousands-separators)
  - [Percentages](#percentages)
  - [Scientific Notation](#scientific-notation)
  - [Binary, Octal and Hexadecimal](#binary-octal-and-hexadecimal)
  - [Dates and Times](#dates-and-times)
  - [Nested Formatting](#nested-formatting)
- [4. Quick Comparison](#4-quick-comparison)
- [5. Practice Questions](#5-practice-questions)
- [6. Mini Projects](#6-mini-projects)
- [7. Quick Cheat Sheet](#7-quick-cheat-sheet)

---

# 1. `eval()` Function in Python

## What is `eval()`?

Python's built-in `eval()` function evaluates a **Python expression** and returns its result.

In simple words:

> `eval()` takes a string and tries to treat that string as a Python expression.

### Example

```python
result = eval("10 + 20")

print(result)
```

Output:

```text
30
```

Here:

```text
"10 + 20"
```

is a string, but `eval()` evaluates it as Python code.

---

## Syntax

```python
eval(expression, globals=None, locals=None)
```

### Parameters

| Parameter | Meaning |
|---|---|
| `expression` | String containing a Python expression |
| `globals` | Optional global namespace |
| `locals` | Optional local namespace |

Example:

```python
x = 10

result = eval("x + 5")

print(result)
```

Output:

```text
15
```

---

## Basic Example

```python
x = eval("5 + 3")

print(x)
```

Output:

```text
8
```

Another example:

```python
x = eval("10 * 5")

print(x)
```

Output:

```text
50
```

---

## What Can `eval()` Evaluate?

`eval()` works with Python **expressions**.

Examples:

```python
print(eval("2 + 3"))
print(eval("10 * 5"))
print(eval("20 / 4"))
print(eval("2 ** 3"))
print(eval("'Hello' + ' World'"))
```

Output:

```text
5
50
5.0
8
Hello World
```

---

## Using Variables

```python
a = 10
b = 20

result = eval("a + b")

print(result)
```

Output:

```text
30
```

Another example:

```python
name = "Sameer"

print(eval("name"))
```

Output:

```text
Sameer
```

---

## Using `eval()` with User Input

Normally, `input()` returns a string.

```python
x = input("Enter a number: ")

print(type(x))
```

If the user enters:

```text
10
```

Output:

```text
<class 'str'>
```

Using `eval()`:

```python
x = eval(input("Enter a number: "))

print(x)
print(type(x))
```

Input:

```text
10
```

Output:

```text
10
<class 'int'>
```

If the user enters:

```text
10.5
```

Output:

```text
10.5
<class 'float'>
```

### Important

This:

```python
x = eval(input())
```

can interpret more than just numbers.

For example, entering:

```text
[10, 20, 30]
```

can produce a list.

```python
x = eval(input())

print(x)
print(type(x))
```

Output:

```text
[10, 20, 30]
<class 'list'>
```

Because of the security risks discussed later, `eval(input())` should generally **not** be used for untrusted input.

---

## Evaluating Mathematical Expressions

One common educational example is a calculator:

```python
expression = input("Enter expression: ")

result = eval(expression)

print("Result:", result)
```

Example:

```text
Enter expression: 10 + 20 * 2
Result: 50
```

The expression follows Python's normal operator precedence.

For example:

```python
eval("10 + 20 * 2")
```

is:

```text
50
```

not:

```text
60
```

because multiplication happens before addition.

---

## Using `eval()` with Lists, Tuples and Dictionaries

### List

```python
x = eval("[10, 20, 30]")

print(x)
print(type(x))
```

Output:

```text
[10, 20, 30]
<class 'list'>
```

### Tuple

```python
x = eval("(10, 20, 30)")

print(x)
print(type(x))
```

Output:

```text
(10, 20, 30)
<class 'tuple'>
```

### Dictionary

```python
x = eval("{'name': 'Sameer', 'age': 20}")

print(x)
print(type(x))
```

Output:

```text
{'name': 'Sameer', 'age': 20}
<class 'dict'>
```

Again, only evaluate trusted input.

---

## `eval()` with `globals` and `locals`

You can control the names available to the expression.

Example:

```python
x = 10

result = eval("x + 5", {"x": 100})

print(result)
```

Output:

```text
105
```

Here, the supplied globals dictionary contains:

```python
{"x": 100}
```

so the expression uses `100`.

### Using `locals`

```python
result = eval(
    "a + b",
    {},
    {"a": 10, "b": 20}
)

print(result)
```

Output:

```text
30
```

This can be useful when you need controlled evaluation of trusted expressions.

---

## `eval()` vs `int()`

Suppose:

```python
x = input("Enter number: ")
```

You can convert it using:

```python
x = int(x)
```

This is appropriate when you specifically expect an integer.

Using:

```python
x = eval(x)
```

is much broader because it evaluates a Python expression.

### Example

```python
x = "10"
print(int(x))
```

Output:

```text
10
```

For ordinary numeric input, prefer:

```python
int()
float()
```

rather than `eval()`.

---

## `eval()` vs `exec()`

This is an important distinction.

### `eval()`

Used for a Python **expression** and returns a value.

```python
result = eval("10 + 20")

print(result)
```

Output:

```text
30
```

### `exec()`

Used to execute Python **statements/code**.

```python
code = """
x = 10
y = 20
print(x + y)
"""

exec(code)
```

Output:

```text
30
```

### Simple difference

| `eval()` | `exec()` |
|---|---|
| Evaluates an expression | Executes Python code |
| Returns a result | Returns `None` |
| Example: `10 + 20` | Example: `x = 10` |
| More restricted | More powerful |

---

## Why `eval()` Can Be Dangerous

`eval()` can execute Python expressions.

If untrusted users control the string passed to `eval()`, they may be able to execute code you did not intend to run.

For example, this is unsafe:

```python
user_input = input("Enter expression: ")

result = eval(user_input)
```

Do **not** assume that because you expect a mathematical expression, the user will only enter mathematics.

### Rule

> Never use `eval()` on untrusted user input.

This is especially important in:

- Web applications
- APIs
- Authentication systems
- Online judges
- Server-side applications
- Programs accepting data from other users

---

## When to Avoid `eval()`

Avoid `eval()` when you can use a safer, more specific solution.

Instead of:

```python
age = eval(input("Enter age: "))
```

use:

```python
age = int(input("Enter age: "))
```

Instead of:

```python
price = eval(input("Enter price: "))
```

use:

```python
price = float(input("Enter price: "))
```

For structured data, consider:

```python
json.loads()
```

For safely parsing Python literals such as lists, dictionaries, numbers, strings, etc., consider:

```python
ast.literal_eval()
```

---

## Safer Alternative: `ast.literal_eval()`

Example:

```python
import ast

data = ast.literal_eval("[10, 20, 30]")

print(data)
```

Output:

```text
[10, 20, 30]
```

Another example:

```python
import ast

data = ast.literal_eval("{'name': 'Sameer', 'age': 20}")

print(data)
```

Output:

```text
{'name': 'Sameer', 'age': 20}
```

`ast.literal_eval()` is designed for safely evaluating strings containing Python literal structures. It does not provide the general code-execution behavior of `eval()`.

---

# 2. Command-Line Arguments in Python

## What Are Command-Line Arguments?

Command-line arguments are values passed to a program when starting it from a terminal.

For example:

```bash
python program.py Sameer 20
```

Here:

```text
program.py
Sameer
20
```

are command-line items.

Python provides the `sys.argv` list to access them.

---

## Running a Python File

Suppose you have:

```text
hello.py
```

with:

```python
print("Hello")
```

Run:

```bash
python hello.py
```

You can also pass arguments:

```bash
python hello.py Sameer
```

Or:

```bash
python hello.py Sameer 20
```

---

## Using `sys.argv`

First import the `sys` module:

```python
import sys
```

Then:

```python
print(sys.argv)
```

Suppose you run:

```bash
python hello.py Sameer 20
```

Output will look like:

```text
['hello.py', 'Sameer', '20']
```

---

## Important `sys.argv` Rules

`sys.argv` is a list.

The first item:

```python
sys.argv[0]
```

is normally the script name/path.

The first argument supplied by the user is:

```python
sys.argv[1]
```

The second argument is:

```python
sys.argv[2]
```

and so on.

### Example

Command:

```bash
python program.py Sameer 20 India
```

Conceptually:

```text
sys.argv[0] = "program.py"
sys.argv[1] = "Sameer"
sys.argv[2] = "20"
sys.argv[3] = "India"
```

---

## Example with One Argument

`hello.py`:

```python
import sys

print("Hello", sys.argv[1])
```

Run:

```bash
python hello.py Sameer
```

Output:

```text
Hello Sameer
```

---

## Example with Multiple Arguments

```python
import sys

print("Name:", sys.argv[1])
print("Age:", sys.argv[2])
print("City:", sys.argv[3])
```

Run:

```bash
python program.py Sameer 20 Patna
```

Output:

```text
Name: Sameer
Age: 20
City: Patna
```

---

## Arguments Are Strings

This is very important.

Suppose:

```bash
python add.py 10 20
```

and:

```python
import sys

a = sys.argv[1]
b = sys.argv[2]

print(type(a))
print(type(b))
```

Output:

```text
<class 'str'>
<class 'str'>
```

Even though you entered:

```text
10 20
```

command-line arguments arrive as strings.

---

## Converting Arguments to Numbers

Use `int()` when you need integers:

```python
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

print(a + b)
```

Run:

```bash
python add.py 10 20
```

Output:

```text
30
```

For decimal values:

```python
a = float(sys.argv[1])
b = float(sys.argv[2])
```

Run:

```bash
python add.py 10.5 20.5
```

Output:

```text
31.0
```

---

## `sys.argv` Length

You can use:

```python
len(sys.argv)
```

Example:

```python
import sys

print(len(sys.argv))
```

Run:

```bash
python program.py Sameer 20 India
```

Output:

```text
4
```

Why `4`?

```text
0 → program.py
1 → Sameer
2 → 20
3 → India
```

---

## Checking Number of Arguments

A common mistake is:

```python
import sys

print(sys.argv[1])
```

If you run:

```bash
python program.py
```

there is no `sys.argv[1]`.

You will get an error such as:

```text
IndexError: list index out of range
```

A safer version:

```python
import sys

if len(sys.argv) < 2:
    print("Please provide a name.")
else:
    print("Hello", sys.argv[1])
```

Run:

```bash
python program.py
```

Output:

```text
Please provide a name.
```

Run:

```bash
python program.py Sameer
```

Output:

```text
Hello Sameer
```

---

## Example: Command-Line Calculator

`calculator.py`:

```python
import sys

if len(sys.argv) != 4:
    print("Usage: python calculator.py number operator number")
    sys.exit()

a = float(sys.argv[1])
operator = sys.argv[2]
b = float(sys.argv[3])

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b == 0:
        print("Cannot divide by zero.")
        sys.exit()
    result = a / b
else:
    print("Invalid operator.")
    sys.exit()

print("Result:", result)
```

Run:

```bash
python calculator.py 10 + 20
```

Output:

```text
Result: 30.0
```

Run:

```bash
python calculator.py 10 "*" 20
```

Output:

```text
Result: 200.0
```

Quoting `*` is useful in shells where `*` can have a special meaning.

---

## Arguments Containing Spaces

Suppose you want to pass:

```text
Sameer Kumar
```

If you run:

```bash
python program.py Sameer Kumar
```

Python receives two arguments:

```text
Sameer
Kumar
```

Use quotes:

```bash
python program.py "Sameer Kumar"
```

Now it is one argument:

```text
Sameer Kumar
```

Example:

```python
import sys

print(sys.argv[1])
```

Command:

```bash
python program.py "Sameer Kumar"
```

Output:

```text
Sameer Kumar
```

---

# `argparse`

For simple programs, `sys.argv` is easy.

For larger command-line programs, Python's `argparse` module is usually a better choice.

Example:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")
parser.add_argument("age", type=int)

args = parser.parse_args()

print("Name:", args.name)
print("Age:", args.age)
```

Run:

```bash
python program.py Sameer 20
```

Output:

```text
Name: Sameer
Age: 20
```

---

## Optional Arguments with `argparse`

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name", required=True)
parser.add_argument("--age", type=int)

args = parser.parse_args()

print(args.name)
print(args.age)
```

Run:

```bash
python program.py --name Sameer --age 20
```

Output:

```text
Sameer
20
```

---

## Help with `argparse`

One useful feature is automatic help:

```bash
python program.py --help
```

It can show how the program should be used.

This makes `argparse` useful for real command-line tools.

---

## `sys.argv` vs `argparse`

| Feature | `sys.argv` | `argparse` |
|---|---|---|
| Easy to learn | Yes | Yes, after basics |
| Direct access to arguments | Yes | Yes |
| Automatic help | No | Yes |
| Type conversion | Manual | Can be automatic |
| Required/optional options | Manual | Built-in |
| Error messages | Manual | Built-in |
| Good for small scripts | Yes | Yes |
| Good for larger CLI tools | Less convenient | Yes |

### Beginner recommendation

Start with:

```python
sys.argv
```

Then learn:

```python
argparse
```

when you start creating proper command-line applications.

---

# 3. Format Specifiers in Python

## What Is a Format Specifier?

A format specifier controls **how a value is displayed**.

For example:

```python
price = 99.45678

print(f"{price:.2f}")
```

Output:

```text
99.46
```

Here:

```text
:.2f
```

is a format specifier.

It means:

- `:` → start formatting instructions
- `.2` → two digits after decimal
- `f` → floating-point format

---

# F-Strings

F-strings are one of the easiest ways to format strings.

Example:

```python
name = "Sameer"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Sameer and I am 20 years old.
```

Format specifiers are placed after a colon:

```python
f"{value:format_spec}"
```

Example:

```python
price = 123.456

print(f"{price:.2f}")
```

Output:

```text
123.46
```

---

# Basic Formatting

```python
name = "Sameer"
age = 20
marks = 95.678

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks:.2f}")
```

Output:

```text
Name: Sameer
Age: 20
Marks: 95.68
```

---

# Decimal Places

Use:

```text
.2f
```

for two decimal places.

```python
x = 12.34567

print(f"{x:.2f}")
```

Output:

```text
12.35
```

### Examples

```python
x = 12.34567

print(f"{x:.0f}")
print(f"{x:.1f}")
print(f"{x:.2f}")
print(f"{x:.3f}")
```

Output:

```text
12
12.3
12.35
12.346
```

---

# Width and Alignment

You can specify the minimum display width.

```python
name = "Sameer"

print(f"{name:10}")
```

The string is given a field width of 10 characters.

---

## Left Alignment

Use:

```text
<
```

Example:

```python
name = "Sameer"

print(f"{name:<10}")
```

---

## Right Alignment

Use:

```text
>
```

Example:

```python
name = "Sameer"

print(f"{name:>10}")
```

---

## Center Alignment

Use:

```text
^
```

Example:

```python
name = "Sameer"

print(f"{name:^10}")
```

---

# Fill Characters

You can specify a fill character before the alignment symbol.

Example:

```python
name = "Sameer"

print(f"{name:*^10}")
```

Output:

```text
**Sameer**
```

Another example:

```python
print(f"{name:-<10}")
```

Output:

```text
Sameer----
```

Another:

```python
print(f"{name:->10}")
```

Output:

```text
----Sameer
```

---

# Sign

For numbers, you can control how positive and negative signs are displayed.

```python
x = 25

print(f"{x:+}")
```

Output:

```text
+25
```

For a negative number:

```python
x = -25

print(f"{x:+}")
```

Output:

```text
-25
```

---

# Zero Padding

Use:

```text
0
```

to pad numbers with zeros.

```python
number = 42

print(f"{number:05}")
```

Output:

```text
00042
```

Another example:

```python
year = 2026

print(f"{year:08}")
```

Output:

```text
00002026
```

---

# Thousands Separators

Use:

```text
,
```

Example:

```python
number = 1000000

print(f"{number:,}")
```

Output:

```text
1,000,000
```

This is useful for readable large numbers.

---

# Percentages

Use:

```text
%
```

Example:

```python
percentage = 0.8567

print(f"{percentage:.2%}")
```

Output:

```text
85.67%
```

Remember:

```text
0.8567 × 100 = 85.67
```

So `%` converts the value to percentage display.

---

# Scientific Notation

Use:

```text
e
```

or:

```text
E
```

Example:

```python
number = 123456789

print(f"{number:.2e}")
```

Output:

```text
1.23e+08
```

---

# Binary, Octal and Hexadecimal

For integers:

### Binary

```python
number = 10

print(f"{number:b}")
```

Output:

```text
1010
```

### Octal

```python
print(f"{number:o}")
```

Output:

```text
12
```

### Hexadecimal

```python
print(f"{number:x}")
```

Output:

```text
a
```

Uppercase hexadecimal:

```python
print(f"{number:X}")
```

Output:

```text
A
```

---

# Combining Format Specifiers

You can combine multiple formatting features.

Example:

```python
price = 1234567.8912

print(f"{price:,.2f}")
```

Output:

```text
1,234,567.89
```

Here:

```text
,    → thousands separator
.2   → two decimal places
f    → floating-point format
```

Another example:

```python
price = 1234.5

print(f"{price:010,.2f}")
```

The exact layout depends on the requested width and formatting components, but the key idea is that format specifications can be combined.

---

# Dates and Times

Python's `datetime` objects can also be formatted.

```python
from datetime import datetime

now = datetime.now()

print(f"{now:%Y-%m-%d}")
```

Example output:

```text
2026-09-22
```

Common date/time codes:

| Code | Meaning |
|---|---|
| `%Y` | Four-digit year |
| `%m` | Month |
| `%d` | Day |
| `%H` | Hour |
| `%M` | Minute |
| `%S` | Second |

Example:

```python
from datetime import datetime

now = datetime.now()

print(f"{now:%d-%m-%Y %H:%M:%S}")
```

Example output:

```text
22-09-2026 10:30:45
```

---

# Nested Formatting

The width or precision can come from another variable.

Example:

```python
number = 12.34567
digits = 2

print(f"{number:.{digits}f}")
```

Output:

```text
12.35
```

Here:

```python
digits = 2
```

controls the number of decimal places.

---

# 4. Quick Comparison

## `eval()`

```python
result = eval("10 + 20")
```

Used to evaluate a Python expression.

**Important:** Do not use it with untrusted input.

---

## `sys.argv`

```python
import sys

print(sys.argv)
```

Used to receive command-line arguments.

Run:

```bash
python program.py Sameer 20
```

---

## `argparse`

```python
import argparse
```

Used for more structured command-line interfaces.

---

## Format Specifiers

```python
price = 1234.5678

print(f"{price:,.2f}")
```

Output:

```text
1,234.57
```

Used to control how values are displayed.

---

# 5. Practice Questions

## `eval()` Practice

### Q1

What is the output?

```python
x = eval("10 + 5")
print(x)
```

### Q2

What is the output?

```python
x = 10
print(eval("x * 2"))
```

### Q3

What type will this produce?

```python
x = eval("[1, 2, 3]")
print(type(x))
```

### Q4

Why is this dangerous?

```python
x = eval(input())
```

---

## Command-Line Argument Practice

### Q5

Suppose you run:

```bash
python program.py Sameer 20 India
```

What are:

```python
sys.argv[0]
sys.argv[1]
sys.argv[2]
sys.argv[3]
```

### Q6

Why does this print strings?

```python
import sys

a = sys.argv[1]
b = sys.argv[2]

print(type(a))
print(type(b))
```

### Q7

Write a program that accepts two integers from the command line and prints their sum.

Example:

```bash
python add.py 10 20
```

Expected:

```text
30
```

### Q8

Write a program that accepts:

```text
name age city
```

from the command line and prints:

```text
Name: ...
Age: ...
City: ...
```

---

## Format Specifier Practice

### Q9

Format this number to two decimal places:

```python
x = 45.67891
```

Expected:

```text
45.68
```

### Q10

Print:

```text
00042
```

from:

```python
x = 42
```

### Q11

Format:

```python
x = 1000000
```

as:

```text
1,000,000
```

### Q12

Convert:

```python
x = 0.875
```

to:

```text
87.50%
```

### Q13

Format:

```python
name = "Sameer"
```

inside a field of width 15 and center it.

---

# 6. Mini Projects

## Project 1: Command-Line Calculator

Create:

```text
calculator.py
```

Run:

```bash
python calculator.py 10 + 20
```

Expected:

```text
Result: 30
```

Try:

```bash
python calculator.py 50 - 10
python calculator.py 10 "*" 5
python calculator.py 20 / 4
```

Topics practiced:

- `sys.argv`
- `int()`
- `float()`
- `if/elif`
- operators
- error handling

---

## Project 2: Student Marks Calculator

Run:

```bash
python marks.py 80 90 75 88 92
```

Calculate:

- Total
- Average
- Percentage

Display the average using:

```python
f"{average:.2f}"
```

Example:

```text
Total: 425
Average: 85.00
Percentage: 85.00%
```

Topics practiced:

- `sys.argv`
- loops
- lists
- `sum()`
- `len()`
- format specifiers

---

## Project 3: Expression Calculator

Create:

```text
calculator_eval.py
```

Example:

```bash
python calculator_eval.py "10 + 20 * 3"
```

Expected:

```text
70
```

### Learning goal

Understand how:

```python
eval()
```

works.

### Security note

Use this only with expressions you control or trust. Do not build a real application that evaluates arbitrary user input with `eval()`.

For a safer calculator, parse only the operations you explicitly support.

---

## Project 4: Student Report

Command:

```bash
python report.py Sameer 85 90 78 92 88
```

Display:

```text
================================
Student Report
================================
Name    : Sameer
Marks   : 85, 90, 78, 92, 88
Total   : 433
Average : 86.60
================================
```

Use format specifiers to make the output clean.

---

## Project 5: CLI File Information Tool

Create:

```text
file_info.py
```

Run:

```bash
python file_info.py sample.txt
```

The program can display:

```text
File Name : sample.txt
Size      : 1024 bytes
```

This is a good beginner project for learning command-line tools.

---

# 7. Quick Cheat Sheet

## `eval()`

```python
eval("10 + 20")
```

Result:

```text
30
```

Basic syntax:

```python
eval(expression)
```

Remember:

```text
eval() → evaluates an expression
```

Avoid:

```python
eval(untrusted_input)
```

---

## `sys.argv`

Import:

```python
import sys
```

Command:

```bash
python program.py one two three
```

Values:

```python
sys.argv[0]  # program.py
sys.argv[1]  # one
sys.argv[2]  # two
sys.argv[3]  # three
```

Number of items:

```python
len(sys.argv)
```

Convert:

```python
int(sys.argv[1])
float(sys.argv[1])
```

---

## `argparse`

Basic:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")

args = parser.parse_args()

print(args.name)
```

---

## F-Strings

```python
name = "Sameer"

print(f"Hello {name}")
```

---

## Decimal Places

```python
x = 12.3456

print(f"{x:.2f}")
```

Output:

```text
12.35
```

---

## Width

```python
print(f"{x:10}")
```

---

## Alignment

```python
f"{x:<10}"   # left
f"{x:>10}"   # right
f"{x:^10}"   # center
```

---

## Zero Padding

```python
f"{42:05}"
```

Output:

```text
00042
```

---

## Thousands Separator

```python
f"{1000000:,}"
```

Output:

```text
1,000,000
```

---

## Percentage

```python
f"{0.8567:.2%}"
```

Output:

```text
85.67%
```

---

## Binary

```python
f"{10:b}"
```

Output:

```text
1010
```

---

## Octal

```python
f"{10:o}"
```

Output:

```text
12
```

---

## Hexadecimal

```python
f"{10:x}"
```

Output:

```text
a
```

---

# Final Summary

The three topics are different:

| Topic | Main Purpose | Example |
|---|---|---|
| `eval()` | Evaluate a Python expression | `eval("10 + 20")` |
| `sys.argv` | Read command-line arguments | `sys.argv[1]` |
| `argparse` | Build structured CLI programs | `parser.add_argument()` |
| Format specifiers | Control displayed output | `f"{price:.2f}"` |

### Learning order

A good beginner order is:

```text
1. input()
   ↓
2. Type conversion: int(), float()
   ↓
3. sys.argv
   ↓
4. argparse
   ↓
5. f-strings
   ↓
6. Format specifiers
   ↓
7. eval() concept
   ↓
8. Security risks of eval()
   ↓
9. Safer parsing alternatives
```

> **Important:** `eval()` is useful for understanding Python's evaluation mechanism, but it should not be treated as a general-purpose way to parse untrusted input.
