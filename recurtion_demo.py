
def call_this(current_value):

  if current_value < 10:
    print("Hey")
    current_value += 1
    call_this(current_value)

call_this(0)