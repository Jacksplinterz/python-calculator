# Python Calculator

A text-based calculator I built as my first Python project. It takes two numbers and an operation (+, -, *, /) and prints the result. This is the first hands-on personal project I've worked on in a while. The others were mostly school and formal projects and I wanted to create something on my own. It's really simple but as I progress in my knowledge of python, more projects are gonna come. 

## How to run

    python calculator.py

## What I practiced

- `input()` and converting strings to numbers with `float()`
- `if` / `elif` / `else` and nested conditions
- Handling edge cases (negative results, dividing by zero)

## Bugs I hit and fixed

- `input()` returns text, so `"5" + "3"` gave `"53"` until I converted to `float`
- My negative-number check was unreachable because the earlier conditions already covered every case
- Dividing by zero printed my message and then crashed anyway, because the next lines weren't in an `else`

## Known limitations / next steps

- Typing letters instead of a number crashes it (adding `try`/`except`)
- It only does one calculation per run (adding a `while` loop)
- It's too simple to actually become anything concrete or marketable so I need to work on adding a user interface (UI) and more features, especially the ability to handle more than just 2 operands.
- I will learn about more advanced Python concepts like classes and object-oriented programming, which will help me structure my code better as I add more features.
- I will explore using libraries and frameworks to enhance my projects and make them more robust.