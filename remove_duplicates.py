def remove_duplicates(list):
  output = []
  seen = set()
  for value in list:
        # If value has not been encountered yet,
        # ... add it to both list and set.
    if value not in seen:
      output.append(value)
      seen.add(value)
  return output

print remove_duplicates([1,1,3,4,5,6,6,6,6,7,8])
