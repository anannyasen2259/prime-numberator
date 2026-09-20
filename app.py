import streamlit as st


# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Function to get primes in a range
def get_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# App title and description
st.title("🔢 Fun with Prime Numbers!")
st.write(
    "Hey there! Welcome to my prime number tool. Use the tabs below to check a single number or find primes in a range."
)

# Create tabs for better organization
tab1, tab2 = st.tabs(["Check a Number", "Find Primes in a Range"])

with tab1:
    st.header("Is it Prime?")
    num_to_check = st.number_input(
        "Enter a number to check:", min_value=0, step=1, value=7
    )

    if st.button("Check Number"):
        if is_prime(num_to_check):
            st.success(f"🎉 Awesome! {num_to_check} is a prime number!")
        else:
            st.error(f"😢 Bummer, {num_to_check} is not a prime number.")

with tab2:
    st.header("Find Primes in a Range")
    col1, col2 = st.columns(2)
    with col1:
        start_num = st.number_input("Start number:", min_value=0, step=1, value=1)
    with col2:
        end_num = st.number_input("End number:", min_value=0, step=1, value=50)

    if st.button("Find Primes"):
        if start_num > end_num:
            st.warning("Oops! The start number can't be bigger than the end number.")
        else:
            prime_list = get_primes_in_range(start_num, end_num)
            if prime_list:
                st.write(
                    f"Found {len(prime_list)} prime numbers between {start_num} and {end_num}:"
                )
                st.info(", ".join(map(str, prime_list)))
            else:
                st.write(f"No prime numbers found between {start_num} and {end_num}.")
