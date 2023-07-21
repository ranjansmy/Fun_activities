def length_substring_char(s):

  start = 0
  max_length = 0
  char_index_map ={}

  for i, char in enumerate(s):
    if char_index_map and char_index_map[char] >= start :
      start = char_index_map[char] + i
    char_index_map[char] = i
    max_length = max(max_length, i - start + 1)

return (max_length)
