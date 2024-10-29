import random

def generate_random_key():
    # Menghasilkan kunci acak 64-bit
    return ''.join(random.choice('01') for _ in range(64))
