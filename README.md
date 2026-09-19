# 🔢 Fraction Calculator – Custom Python Data Type

An interactive Fraction Calculator built using **Python, Object-Oriented Programming (OOP), Operator Overloading, and Streamlit**.

The application allows users to enter fractions directly, perform mathematical operations, compare fractions, convert values into decimals, and maintain downloadable calculation history through a simple web interface.

## 🚀 Live Demo

🔗 **Streamlit App:** https://fraction-calculator-python-njodbeq5iehafawdybcomb.streamlit.app/

## 📌 Project Overview

This project implements a custom `Fraction` class that represents fractions using a numerator and denominator.

The class automatically simplifies fractions using the Greatest Common Divisor (GCD) and supports several arithmetic and comparison operations through Python special methods.

The Streamlit interface makes the custom data type accessible through an interactive calculator.

## ✨ Features

- Direct fraction input using text fields
- Supports inputs such as `2/3`, `5/8`, `10`, `-3/4`, and decimal values
- Automatic fraction simplification using `gcd()`
- Addition
- Subtraction
- Multiplication
- Division
- Floor division
- Modulus
- Power operation
- Fraction comparison
- Absolute value
- Decimal conversion
- Negative fraction handling
- Input validation
- Zero-denominator and division-by-zero error handling
- Calculation history using Streamlit session state
- Downloadable calculation history in CSV format
- Custom CSS styling and sidebar settings

## 🛠️ Technologies Used

- **Python**
- **Object-Oriented Programming (OOP)**
- **Operator Overloading**
- **Streamlit**
- **Pandas**
- **Math Module**
- **Decimal Module**
- **Git and GitHub**

## 📂 Project Structure

```text
fraction-calculator-python/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/NehaKumari990/fraction-calculator-python.git
```

### 2. Open the Project Folder

```bash
cd fraction-calculator-python
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you are using macOS and `pip` is not recognized:

```bash
python3 -m pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

For macOS:

```bash
python3 -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 🧮 Supported Operations

| Operation | Example | Result |
|---|---|---|
| Addition | `2/3 + 3/4` | `17/12` |
| Subtraction | `2/3 - 3/4` | `-1/12` |
| Multiplication | `2/3 × 3/4` | `1/2` |
| Division | `2/3 ÷ 3/4` | `8/9` |
| Power | `(2/3)²` | `4/9` |
| Absolute Value | `abs(-5/3)` | `5/3` |

## 🧠 Core Python Concepts

### 1. Custom Fraction Class

The `Fraction` class stores the numerator and denominator and ensures that the denominator is not zero.

### 2. Automatic Simplification

Fractions are simplified during object creation using the GCD function.

Example:

```text
Input:  8/12
Output: 2/3
```

### 3. Operator Overloading

Python special methods define the behavior of fraction objects with mathematical operators, including:

```python
__add__()
__sub__()
__mul__()
__truediv__()
__floordiv__()
__mod__()
__pow__()
__eq__()
__lt__()
__gt__()
```

### 4. Input Parsing

The `parse_fraction()` function supports fraction, integer, and decimal input formats.

Examples:

```text
2/3
10
-3/4
0.75
```

### 5. Exception Handling

The application handles invalid inputs and mathematical errors such as:

- Empty input
- Invalid fraction format
- Zero denominator
- Division by zero
- Unsupported input types

## 📊 Application Workflow

```text
User Input
    ↓
Input Parsing
    ↓
Validation
    ↓
Fraction Object Creation
    ↓
Operation Selection
    ↓
Calculation
    ↓
Simplified Result
    ↓
History Storage
    ↓
CSV Download
```

## 🖥️ Application Interface

The Streamlit application includes:

- Fraction input fields
- Operation selection dropdown
- Calculate button
- Result display
- Decimal value display
- Comparison results
- Sidebar settings
- Calculation history table
- CSV download option

## 🎯 Learning Outcomes

This project helped me practice:

- Designing custom Python data types
- Classes and objects
- Static methods
- Operator overloading
- Input parsing
- Exception handling
- Mathematical logic
- Streamlit application development
- Session state management
- Data handling with Pandas
- GitHub documentation and deployment

## 🔮 Future Enhancements

- Mixed fraction support
- Percentage conversion
- Advanced mathematical expression parsing
- Unit testing using `pytest`
- PDF export
- Improved responsive design
- More advanced fraction operations
- User authentication and saved user history

## 👩‍💻 Author

**Neha Kumari**

Aspiring Data Scientist | Python and Machine Learning Enthusiast

- GitHub: [NehaKumari990](https://github.com/NehaKumari990)
- LinkedIn: [Neha Kumari](https://www.linkedin.com/in/nehakumari1110/)

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software, subject to the terms and conditions of the MIT License.

See the [LICENSE](LICENSE) file for more details.
