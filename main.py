if __name__ == "__main__":
  # Using Python set intersection() method to intersect two or more sets

  """
  new_set = set1.intersection(set2, set3, ...)
  """

  s1 = {"Python", "Java","C++"}
  s2 = {"C#", "Java", "C++"}
  s = s1.intersection(s2)

  print(s1)
  print(s2)
  print(s)

  # Using Python set intersection (&) operator to intersect two or more sets

  """
  new_set = s1 & s2 & s3 & ...
  """

  s1 = {"Python", "Java","C++"}
  s2 = {"C#", "Java", "C++"}
  s = s1 & s2

  print(s1)
  print(s2)
  print(s)

  # Set intersection() method vs set intersection operator (&)

  numbers = {1, 2, 3}
  scores = [2, 3, 4]
  print(numbers)
  print(scores)

  numbers = numbers.intersection(scores)
  print(numbers)

  numbers = {1, 2, 3}
  scores = [2, 3, 4]
  print(numbers)
  print(scores)

  # numbers = numbers.intersection(scores)
  # TypeError
