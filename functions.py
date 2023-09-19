# write a fizzbuzz function in python

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
# To test the given function, we can redirect the print statements to a string
# Then make assertions based on the expected output
# Note that the implementation should return the outputs rather than print them
# Here is an adjusted implementation for the purpose of testing

def fizzbuzz():
    result = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(i)
    return result
  
import unittest

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz(self):
        result = fizzbuzz()
        self.assertEqual(len(result), 100)
        
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                self.assertEqual(result[i-1], 'fizzbuzz')
            elif i % 3 == 0:
                self.assertEqual(result[i-1], 'fizz')
            elif i % 5 == 0:
                self.assertEqual(result[i-1], 'buzz')
            else:
                self.assertEqual(result[i-1], i)

if __name__ == '__main__':
    unittest.main()