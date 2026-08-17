from calculator import add, subtract, multiply

def test_add():
  assert add(2,5)==7
  assert add(10,10)==19
  assert add(12,3)==15
  
def test_subtract():
  assert subtract(5,2)==3
  assert subtract(10,6)==4
  assert subtract(12,20)==-8
  
def test_multiply():
  assert multiply(2,5)==10
  assert multiply(10,5)==50
