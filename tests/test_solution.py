
from solution import *

class Tests:

  def test_get_adj(self, monkeypatch):
    """
    Test the get_adj method
    """
    monkeypatch.setattr('builtins.input', lambda x: "arugula")
    adjective_1 = get_adj()
    assert adjective_1 == 'arugula'

  def test_get_verb(self, monkeypatch):
    """
    Test the get_verb method
    """
    monkeypatch.setattr('builtins.input', lambda x: "arugula")
    verb_1 = get_verb()
    assert verb_1 == 'arugula'

  def test_get_plural_noun(self, monkeypatch):
    """
    Test the get_plural_noun method
    """
    monkeypatch.setattr('builtins.input', lambda x: "arugula")
    plural_noun_1 = get_plural_noun()
    assert plural_noun_1 == 'arugula'

  def test_get_proper_noun(self, monkeypatch):
    """
    Test the get_proper_noun method
    """
    monkeypatch.setattr('builtins.input', lambda x: "arugula")
    proper_noun_1 = get_proper_noun()
    assert proper_noun_1 == 'arugula'

  def test_generate(self, capsys, monkeypatch):
    """
    Test the generate method outputs the correct poem
    """
    monkeypatch.setattr('builtins.input', lambda x: "arugula")
    generate()
    captured = capsys.readouterr()  # capture print output
    actual = captured.out.lower().strip()
    expected = '''
    ’Twas arugula, and the slithy toves
    Did arugula and gimble in the wabe;
    All arugula were the arugula,
    And the mome arugula outgrabe.

    “Beware the arugula, my son!
    The jaws that arugula, the arugula that catch!
    Beware the Jubjub bird, and shun
    The frumious arugula!”
  ''' .lower().strip()
  
    assert actual == expected
