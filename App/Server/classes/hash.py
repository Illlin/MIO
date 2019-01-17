# This will hash the passwords and store the salt with the returned string.
import bcrypt

# Generate the password hash
def make_password_hash(password):
    # Secure salt that will stop same passwords haveing same hash
    salt = bcrypt.gensalt()

    password_bytes = password.encode("utf-8")

    # Hash password. This takes some time to stop brute force attack.
    password_hash = bcrypt.hashpw(password_bytes,salt)
    return password_hash.decode("utf-8")

# Checks if enterd password matches hash
def check_password(password,password_hash):
    password_bytes = password.encode("utf-8")
    correct = bcrypt.checkpw(password_bytes, password_hash)

    return correct


