import os

def clear():
  command = 'clear'
  if os.name in ('nt', 'dos'):
      command = 'cls'
  os.system(command)

if __name__ == "__main__":
  clear()
