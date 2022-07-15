from sympy import *


class Poly_derivative:
    def __init__(self,polynomial,variable):
        self._poly = str(polynomial)
        self._var = str(variable)
    def first_dx(self):
        x = Symbol(self._var)
        y = sympify(self._poly)
        return y.diff(x)

if __name__=='__main__':
      test_poly = input('Please input algebraic polynomial with format ex. 18*x**4 + 12*x**3 - 9*x**2 + 4 \n')
      variable = input('Please input what variable we are solving for ex. x \n')
      j = sympify(test_poly)
      dx = Poly_derivative(j,variable)
      print(dx.first_dx())