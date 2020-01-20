import math

def is_prime(n):  
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(9) is False
    assert is_prime(12) is False
