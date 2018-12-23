def is_isogram(string):
  if(string==""):
      return True
  else:
      isogram = string.lower()
      converted_to_set = set(isogram)
      converted_to_tuple=tuple(isogram)
      count_of_letters = 0
      length_of_string = len(isogram)
      yes_flag = 0
      for letter in isogram:
          if letter in converted_to_set:
             if(converted_to_tuple.count(letter)>1):
                 yes_flag = 1
                
      
      
      if(yes_flag == 1):
          return False
      else:
          return True
