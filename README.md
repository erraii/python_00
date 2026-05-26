# python_00

`python_00` is a small educational Python repository designed for practicing Python fundamentals. The exercises follow a garden/growing-code theme and are organized step by step in separate folders.

## Contents

| Folder / File | Description |
|---|---|
| `ex0/ft_hello_garden.py` | Prints a simple welcome message. |
| `ex1/ft_garden_name.py` | Asks the user for a garden name and prints it. |
| `ex2/ft_plot_area.py` | Calculates an area using length and width values. |
| `ex3/ft_harvest_total.py` | Calculates the total harvest amount for three days. |
| `ex4/ft_plant_age.py` | Checks whether a plant is ready for harvest. |
| `ex5/ft_water_reminder.py` | Checks whether it is time to water the plant. |
| `ex6/ft_count_harvest_iterative.py` | Counts the remaining days until harvest using a loop. |
| `ex6/ft_count_harvest_recursive.py` | Counts the remaining days until harvest using recursion. |
| `ex7/ft_seed_inventory.py` | Displays seed inventory information using type hints. |
| `test00.py` | Helper file for running/testing the exercises. |

## Requirements

- Python 3
- `uv`
- `flake8`
- `mypy`

In this setup, `flake8` and `mypy` were installed with `uv tool install`:

```bash
uv tool install flake8
uv tool install mypy
```

After installation, you can check whether the tools are available with:

```bash
flake8 --version
mypy --version
```

## Clone the Repository

```bash
git clone https://github.com/erraii/python_00.git
cd python_00
```

## Running the Exercises

Each exercise contains its own Python function. You can run the helper test file to try the exercises:

```bash
python3 test00.py
```

When the program starts, it asks which exercise you want to run. You can select a single exercise or choose `a` to run all exercises.

## Code Quality Checks

This project can be checked with:

- `mypy` for static type checking
- `flake8` for style and error checking

## mypy Command

```bash
mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs .
```

## mypy Flag Explanations

| Flag | Explanation |
|---|---|
| `--warn-return-any` | Warns when a function returns a value typed as `Any`. This helps encourage more precise return types. |
| `--warn-unused-ignores` | Warns about unnecessary `# type: ignore` comments. This helps keep the code clean when an ignore comment is no longer needed. |
| `--ignore-missing-imports` | Suppresses errors for imports that do not have available type information or cannot be found by mypy. This is often useful for third-party packages. |
| `--disallow-untyped-defs` | Disallows function definitions without type annotations. Function parameters and return types must be explicitly typed. |
| `--check-untyped-defs` | Checks the bodies of functions even if they do not have type annotations. This can catch type-related issues inside untyped functions. |
| `.` | Tells mypy to check the current directory and its subdirectories. |

## flake8 Command

```bash
flake8 --extend-select=N .
```

## flake8 Flag Explanations

| Flag | Explanation |
|---|---|
| `--extend-select=N` | Enables additional checks with codes starting with `N`, usually naming-convention checks provided by the `pep8-naming` plugin. |
| `.` | Tells flake8 to check the current directory and its subdirectories. |

> Note: For `--extend-select=N` to report naming-convention issues, the `pep8-naming` plugin may need to be available in the same environment as `flake8`. If `N` codes are not reported, install the plugin according to your environment setup.

Example:

```bash
uv tool install pep8-naming
```

Depending on your setup, make sure `pep8-naming` is installed in a way that your `flake8` command can access it.

## Suggested Workflow

After writing or editing code, you can run the following commands:

```bash
mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs .
flake8 --extend-select=N .
python3 test00.py
```

This workflow:

1. Checks static typing issues.
2. Checks style and naming issues.
3. Runs the exercise test helper.

## Project Structure

```text
python_00/
├── README.md
├── test00.py
├── ex0/
│   └── ft_hello_garden.py
├── ex1/
│   └── ft_garden_name.py
├── ex2/
│   └── ft_plot_area.py
├── ex3/
│   └── ft_harvest_total.py
├── ex4/
│   └── ft_plant_age.py
├── ex5/
│   └── ft_water_reminder.py
├── ex6/
│   ├── ft_count_harvest_iterative.py
│   └── ft_count_harvest_recursive.py
└── ex7/
    └── ft_seed_inventory.py
```

## Purpose

This repository is intended to help beginners practice core Python topics such as:

- Defining functions
- Getting user input with `input()`
- Printing output with `print()`
- Basic arithmetic operations
- Conditional logic with `if / else`
- Loops
- Recursive functions
- Type hints
- A simple test flow
- Code quality checks with `mypy` and `flake8`

## License

No license information is currently specified for this repository. A `LICENSE` file can be added to clarify usage terms.
