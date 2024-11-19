import time

#Algorithm MT19937
w, n, m, r = 32, 624, 397, 31
a = 0x9908B0DF
u, d = 11, 0xFFFFFFFF
s, b = 7, 0x9D2C5680
t, c = 15, 0xEFC60000
l = 18
f = 1812433253
upper_mask = 0x80000000  # Most significant (w-r) bits
lower_mask = 0x7FFFFFFF  # Least significant r bits

class MT19937:
    def __init__(self, seed):
        # Initialize generator from a seed
        self.MT = [0] * n
        self.index = n
        self.MT[0] = seed
        for i in range(1, n):
            self.MT[i] = (f * (self.MT[i - 1] ^ (self.MT[i - 1] >> (w - 2))) + i) & 0xFFFFFFFF

    def twist(self):
        # Update state array with twisting
        for i in range(n):
            x = (self.MT[i] & upper_mask) + (self.MT[(i + 1) % n] & lower_mask)
            xA = x >> 1
            if x % 2 != 0:  # If x is odd
                xA ^= a
            self.MT[i] = (self.MT[(i + m) % n] ^ xA) & 0xFFFFFFFF

    def temper(self, y):
        # Apply tempering transformations
        y ^= (y >> u) & d
        y ^= (y << s) & b
        y ^= (y << t) & c
        y ^= y >> l
        return y

    def extract_number(self):
        # Extract a tempered value based on MT using twist
        if self.index >= n:
            self.twist()
            self.index = 0

        y = self.MT[self.index]
        self.index += 1

        return self.temper(y)

def generate_randomness():
    global randomness
    initial_seed = int(time.time()*1000000)
    mt_initial = MT19937(seed=initial_seed)

    new_seed = mt_initial.extract_number()

    mt = MT19937(seed=new_seed)

    randomness = [(mt.extract_number()) % 100 for _ in range(1)]
    return randomness

def generate_number():
    global random_numbers
    initial_seed = int(time.time())
    mt_initial = MT19937(seed=initial_seed)

    new_seed = mt_initial.extract_number()

    mt = MT19937(seed=new_seed)

    random_numbers = [(mt.extract_number() % 3) + 1 for _ in range(100)]
    return random_numbers
