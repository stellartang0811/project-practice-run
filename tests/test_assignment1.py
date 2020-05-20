
from assignment1 import *

class Tests:

  def test_foo(self):
    """
    Test the foo method with variety of args
    """
    assert foo(10, 20) == 200
    assert foo(-5, -3) == 15
    assert foo(-5, 3) == -15

  def test_bar(self):
    """
    Test the bar method returns the proper text
    """
    assert type(bar()) == str
    assert bar() == "Hello world!"
  
  def test_baz(self, capsys):
    """
    Test the baz method prints the proper text
    """
    baz()
    captured = capsys.readouterr() # capture print output
    assert captured.out == "Hello world!\n"
