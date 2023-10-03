# Time complexity: O(sqrt(n))
# Space complexity: O(1)
def prime_number(number):

  if number <= 1:
    return False
  for i in range(2, int(number ** 0.5) + 1):  
    if number % i == 0:
      return False
  return True

if __name__ == '__main__':
    print(prime_number(1000000007)) # True
    print(prime_number(1500450271)) # True
    print(prime_number(1000000000)) # False
    print(prime_number(10000000019)) # True
    print(prime_number(10000000033)) # True
