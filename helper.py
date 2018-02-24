file = open('helper.txt', 'rw') 
lines = file.readlines()
file.close() 

#for line in lines:
#  print line[0:-2]

def level(string):
  return (string.find('"') / 2)


result = []

stack = []
for line in lines:
  line = line[0:-2]
  lev = level(line)
  while len(stack) > lev:
    stack = stack[:-1]

  stack.append(line.strip()[1:])
  result.append(stack[:])


for res in result:
  print '"' + ".".join(res) + '",'
