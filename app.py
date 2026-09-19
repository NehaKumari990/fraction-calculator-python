
import streamlit as st
from math import gcd
from decimal import Decimal
import pandas as pd


# ==========================================
# CUSTOM FRACTION DATA TYPE
# ==========================================

class Fraction:

    def __init__(self, n=0, d=1):

        if not isinstance(n, int) or not isinstance(d, int):
            raise TypeError("Numerator and denominator must be integers")

        if d == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        if d < 0:
            n = -n
            d = -d

        common = gcd(abs(n), d)

        self.num = n // common
        self.den = d // common

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    def __float__(self):
        return self.num / self.den

    def __int__(self):
        return int(self.num / self.den)

    def __bool__(self):
        return self.num != 0

    @staticmethod
    def convert(value):

        if isinstance(value, Fraction):
            return value

        if isinstance(value, int):
            return Fraction(value, 1)

        raise TypeError("Only Fraction or int is supported")

    def __add__(self, other):

        other = Fraction.convert(other)

        return Fraction(
            self.num * other.den + other.num * self.den,
            self.den * other.den
        )

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        other = Fraction.convert(other)

        return Fraction(
            self.num * other.den - other.num * self.den,
            self.den * other.den
        )

    def __rsub__(self, other):
        return Fraction.convert(other) - self

    def __mul__(self, other):

        other = Fraction.convert(other)

        return Fraction(
            self.num * other.num,
            self.den * other.den
        )

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):

        other = Fraction.convert(other)

        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        return Fraction(
            self.num * other.den,
            self.den * other.num
        )

    def __rtruediv__(self, other):
        return Fraction.convert(other) / self

    def __floordiv__(self, other):

        other = Fraction.convert(other)

        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        return self.num * other.den // (self.den * other.num)

    def __mod__(self, other):

        other = Fraction.convert(other)

        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        quotient = self // other

        return self - (other * quotient)

    def __pow__(self, power):

        if not isinstance(power, int):
            raise TypeError("Power must be an integer")

        if power >= 0:
            return Fraction(
                self.num ** power,
                self.den ** power
            )

        if self.num == 0:
            raise ZeroDivisionError("Zero cannot have negative power")

        return Fraction(
            self.den ** (-power),
            self.num ** (-power)
        )

    def __neg__(self):
        return Fraction(-self.num, self.den)

    def __pos__(self):
        return Fraction(self.num, self.den)

    def __abs__(self):
        return Fraction(abs(self.num), self.den)

    def __eq__(self, other):

        try:
            other = Fraction.convert(other)
        except TypeError:
            return NotImplemented

        return (
            self.num == other.num
            and self.den == other.den
        )

    def __lt__(self, other):

        other = Fraction.convert(other)

        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):

        other = Fraction.convert(other)

        return self.num * other.den > other.num * self.den

    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((self.num, self.den))


# ==========================================
# INPUT PARSER
# ==========================================

def parse_fraction(value):

    value = value.strip()

    if not value:
        raise ValueError("Please enter a fraction")

    if "/" in value:

        parts = value.split("/")

        if len(parts) != 2:
            raise ValueError("Use format like 2/3")

        numerator = int(parts[0].strip())
        denominator = int(parts[1].strip())

        return Fraction(numerator, denominator)

    # Decimal support
    if "." in value:

        decimal_value = Decimal(value)

        numerator, denominator = decimal_value.as_integer_ratio()

        return Fraction(numerator, denominator)

    return Fraction(int(value), 1)


# ==========================================
# STREAMLIT CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Fraction Calculator",
    page_icon="🔢",
    layout="centered"
)


# ==========================================
# SESSION STATE
# ==========================================

if "history" not in st.session_state:
    st.session_state.history = []


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #e8f5e9;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.header("⚙️ Settings")

    st.write("Custom Fraction Calculator")

    st.write("Features:")
    st.write("✔ Automatic Simplification")
    st.write("✔ Arithmetic Operations")
    st.write("✔ Comparison")
    st.write("✔ History")
    st.write("✔ Decimal Support")

    if st.button("🗑️ Clear History"):

        st.session_state.history = []

        st.success("History cleared!")


# ==========================================
# TITLE
# ==========================================

st.markdown(
    '<div class="main-title">🔢 Fraction Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Custom Python Data Type + Streamlit</div>',
    unsafe_allow_html=True
)

st.divider()


# ==========================================
# INPUT SECTION
# ==========================================

st.subheader("Enter Fractions")

col1, col2 = st.columns(2)

with col1:

    fraction1_input = st.text_input(
        "Fraction 1",
        value="2/3",
        placeholder="Example: 2/3"
    )

with col2:

    fraction2_input = st.text_input(
        "Fraction 2",
        value="3/4",
        placeholder="Example: 5/8"
    )


st.caption("You can enter 2/3, 5/8, 10, or 0.75")


# ==========================================
# OPERATION
# ==========================================

st.subheader("Choose Operation")

operation = st.selectbox(
    "Select an operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (*)",
        "Division (/)",
        "Floor Division (//)",
        "Modulus (%)",
        "Power (**)",
        "Comparison",
        "Absolute Value",
        "Decimal Conversion"
    ]
)


power = 2

if operation == "Power (**)" :

    power = st.number_input(
        "Enter Power",
        value=2,
        step=1
    )


# ==========================================
# CALCULATION
# ==========================================

if st.button("Calculate", type="primary", use_container_width=True):

    try:

        f1 = parse_fraction(fraction1_input)
        f2 = parse_fraction(fraction2_input)

        result = None
        expression = ""

        if operation == "Addition (+)":

            result = f1 + f2
            expression = f"{f1} + {f2}"

        elif operation == "Subtraction (-)":

            result = f1 - f2
            expression = f"{f1} - {f2}"

        elif operation == "Multiplication (*)":

            result = f1 * f2
            expression = f"{f1} * {f2}"

        elif operation == "Division (/)":

            result = f1 / f2
            expression = f"{f1} / {f2}"

        elif operation == "Floor Division (//)":

            result = f1 // f2
            expression = f"{f1} // {f2}"

        elif operation == "Modulus (%)":

            result = f1 % f2
            expression = f"{f1} % {f2}"

        elif operation == "Power (**)" :

            result = f1 ** int(power)
            expression = f"{f1} ** {int(power)}"

        elif operation == "Comparison":

            st.subheader("Comparison Results")

            st.write(f"Fraction 1: **{f1}**")
            st.write(f"Fraction 2: **{f2}**")

            st.write(f"Equal (==): {f1 == f2}")
            st.write(f"Not Equal (!=): {f1 != f2}")
            st.write(f"Less Than (<): {f1 < f2}")
            st.write(f"Greater Than (>): {f1 > f2}")
            st.write(f"Less or Equal (<=): {f1 <= f2}")
            st.write(f"Greater or Equal (>=): {f1 >= f2}")

        elif operation == "Absolute Value":

            result = abs(f1)
            expression = f"abs({f1})"

        elif operation == "Decimal Conversion":

            st.subheader("Decimal Values")

            st.write(f"Fraction 1: **{float(f1):.6f}**")
            st.write(f"Fraction 2: **{float(f2):.6f}**")

        if result is not None:

            st.subheader("Result")

            st.markdown(
                f'<div class="result-box">{result}</div>',
                unsafe_allow_html=True
            )

            st.write(f"Expression: `{expression}`")

            st.write(f"Decimal Value: `{float(result):.6f}`")

            st.session_state.history.append({
                "Expression": expression,
                "Result": str(result)
            })

            st.success("Calculation completed successfully!")

    except (ValueError, TypeError, ZeroDivisionError) as e:

        st.error(f"Error: {e}")


# ==========================================
# HISTORY
# ==========================================

st.divider()

st.subheader("📜 Calculation History")

if st.session_state.history:

    history_df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )

    csv_data = history_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download History",
        data=csv_data,
        file_name="fraction_history.csv",
        mime="text/csv"
    )

else:

    st.info("No calculation history yet.")


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Built with Python | OOP | Operator Overloading | Streamlit"
)