"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 

        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    if (x.decimal_val <= 1 or y.decimal_val <= 1):
        return BinaryNumber(x.decimal_val * y.decimal_val)
    else:
        binx = x.binary_vec
        biny = y.binary_vec
        (binx, biny) = pad(binx, biny)
        (x_left, x_right) = split_number(binx) 
        (y_left,y_right) = split_number(biny)
        n = len(binx)
        return BinaryNumber((bit_shift(_quadratic_multiply(x_left,y_left),n)).decimal_val 
            + (bit_shift(BinaryNumber((_quadratic_multiply(x_left,y_right)).decimal_val 
            +(_quadratic_multiply(x_right,y_left).decimal_val)),n//2)).decimal_val 
            + _quadratic_multiply(x_right,y_right).decimal_val)

    
   
def time_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(BinaryNumber(x),BinaryNumber(y))
    return (time.time() - start)*1000


print(time_quadratic_multiply(1,2,_quadratic_multiply))
print(time_quadratic_multiply(10,2,_quadratic_multiply))
print(time_quadratic_multiply(100,2,_quadratic_multiply))
print(time_quadratic_multiply(1000,2,_quadratic_multiply))
print(time_quadratic_multiply(10000,2,_quadratic_multiply))
print(time_quadratic_multiply(100000,2,_quadratic_multiply))

