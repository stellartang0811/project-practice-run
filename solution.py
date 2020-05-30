
def get_adj():
  """
  Ask the user to enter an adjective.
    :returns: the text entered by the user
  """
  # write your code for this function below this line

  # don't modify the return statement below... 
  return word

def get_verb():
  """
  Ask the user to enter a verb.
    :returns: the text entered by the user
  """
  # write your code for this function below this line

  # don't modify the return statement below... leave it as the last line in this function
  return word

def get_plural_noun():
  """
  Ask the user to enter a plural noun.
    :returns: the text entered by the user
  """
  # write your code for this function below this line

  # don't modify the return statement below... leave it as the last line in this function
  return word

def get_proper_noun():
  """
  Ask the user to enter a proper noun (the name of a location, person, or event).
    :returns: the text entered by the user
  """
  # write your code for this function below this line

  # don't modify the return statement below... leave it as the last line in this function
  return word

def generate():
  """
  Generates a variation of the Jabberwocky poem in a "Mad Lib" style.
  You can view the text of the original Jaabberwocky poem here: https://en.wikipedia.org/wiki/Jabberwocky

  Uses the functions defined in this file to ask the user for...
  - 2 adjectives
  - 2 verbs
  - 2 plural nouns
  - 2 proper nouns (names of a place, person, or event)

  Then plug these into the Jaberwocky poem according to the given template.

    :returns: the Jaberwocky poem with the user's words inserted
  """

  # write your code for this function below this line...
  # feel free to modify the given poem code and add any additional code as necessary

  poem = '''
    ’Twas {adjective_1}, and the slithy toves
    Did {verb_1} and gimble in the wabe;
    All {adjective_2} were the {plural_noun_1},
    And the mome {plural_noun_1} outgrabe.

    “Beware the {proper_noun_1}, my son!
    The jaws that {verb_2}, the {plural_noun_2} that catch!
    Beware the Jubjub bird, and shun
    The frumious {proper_noun_2}!”
  '''

  # don't modify the print statement below... leave it as the last line in this function
  print(poem)
