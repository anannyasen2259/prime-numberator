# [prime-numberator](https://prime-numberator.streamlit.app/)

**Summer Project 2026**

This is a streamlit app for finding prime numbers. The app can find all the prime numbers between 2 given numbers or verify if a single number is a prime number or not.

## Primality Testing

The app uses the **Primality Testing**, which uses the squareroot method to verify whether a given number is prime number or not.
To verify a number is prime number or not using Primality Testing, the logic is to find numbers between 2 and squareroot of the given number and find if any of the number is a factors for the number. If there are not factors for the given number in the range, then the number will be a prime number.

e.g. Taking an example of 50, the following steps are performed

- Find the squareroot of 50 ( 50**(1/2) ) or ( 50**0.5)
- Iteratre from 2 to 7.07106 or 8
- Find if any of the number between 2 and 8 is a factor of 50 ( 50 % number = 0 )
  - For a number (x) to be a factor of another number (n), dividing x by n should give a remainder of 0
- If there are any factors between the squareroot range numbers, then the number will not be a prime number

### Other Methods

The other methods to find the prime numbers are **Sieve of Eratosthenes**, which iterates through the numbers and eliminates the multiples of each prime number found.

### My Choice

I choose the **Primality Testing** because I can use the same method to find all the prime number between 2 numbers and verify if a given mumber is a prime number or not. For my curiosity I found this method easier to implement than the other methods.

I choose Streamlit app as it is an open-source python based app. It also provides a free platform to host any python app. Streamlit also provides a very basic GUI to display the functionality and was a good fit to showcase my project.

### Uses of Prime numbers

- **Nature and Biology:** Periodical cicadas emerge from the ground every 13 or 17 years—both prime numbers. This evolutionary strategy helps them avoid syncing up with short-cycle predators. In the Summer of 2024, we had a lot of cicadas, which made me curious and as a result found out about the relation with the Prime numbers and their lifecycle.
- **Cybersecurity and Encryption:** Systems like RSA encryption multiply two massive prime numbers together. It is very easy for a computer to multiply them, but extremely hard to reverse the process and figure out what the original prime numbers were. This protects your private information online
- **Pseudo-Random Number Generation:** Computer programs use primes to generate unpredictable sequences of numbers used in simulations, gaming, and secure data handling.
- **Error-Correcting Codes:** Telecommunications and data storage use math built on prime numbers to automatically detect and fix corrupted data during transmission.
- **Engineering and Design:** Engineers use prime-numbered dimensions or gear teeth counts in machinery (like jet engine fans) to prevent matching vibrations and minimize wear and tear.
