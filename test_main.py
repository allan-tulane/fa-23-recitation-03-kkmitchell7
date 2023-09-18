from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(5)) == 4*5
    assert quadratic_multiply(BinaryNumber(11), BinaryNumber(4)) == 11*4
    assert quadratic_multiply(BinaryNumber(32), BinaryNumber(3)) == 32*3

