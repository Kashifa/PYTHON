import sys


def word_count_dict(filename):
  """Returns a word/count dict for this filename."""
  # Utility used by count() and Topcount().
  word_count = {}  # Map each word to its count
  input_file = open(filename, 'r')
  for line in input_file:
    words = line.split()
    for word in words:
      word = word.lower()
      
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1
  input_file.close() 
  return word_count


def print_words(filename):
  """Prints one per line '<word> <count>' sorted by word for the given file."""
  word_count = word_count_dict(filename)
  words = sorted(word_count.keys())
  for word in words:
    print (word, word_count[word])


def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""
  return word_count_tuple[1]


def print_top(filename):
  """Prints the top count listing for the given file."""
  word_count = word_count_dict(filename)

  # Each item is a (word, count) tuple.
  # Sort them so the big counts are first using key=get_count() to extract count.
  items = sorted(word_count.items(), key=get_count, reverse=True)

  # Print the first 20
  for item in items[:20]:
    print (item[0], item[1])

