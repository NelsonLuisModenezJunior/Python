import string as st
import numpy as np

letters = st.ascii_letters
numbers = st.digits
special = st.punctuation
code = (letters+numbers+special)
password = np.random.choice(list(code),12)
print(" ")
print("----------------------------------")
print("Sua senha de 12 caracteres é: ",''.join(password))
print("----------------------------------")