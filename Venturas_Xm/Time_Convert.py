def TimeConvert(num):
  h = int(num/60)
  m = int(num%60)
  time = f"{h}:{m}"
  return time

# keep this function call here 
print(TimeConvert(input()))