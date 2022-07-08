# Calculator Class
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        sum_total = self.num1 + self.num2
        return sum_total
    def avg(self):
        avg_total = (self.num1 + self.num2) / 2
        return avg_total

class multiply_calculator(Calculator):
    def multiply(self):
        multiply_total = self.num1 * self.num2
        return multiply_total
        
c = multiply_calculator(3,10)

print(c.sum())
print(c.avg())
print(c.multiply())