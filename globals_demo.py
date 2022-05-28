
defg = 1000

def sample_function():
  abc = 10
  print(abc)
  global defg
  defg = 10000
  print(defg)

sample_function()
print("DEFG Global:",defg)
