import re, sys

#original that gave Precision 0.871, Recall 0.916
#for line in sys.stdin:
 #   for token in re.findall("([,;:.!?\"]|\w+)", line.strip()):
  #      print(token)

#should give 0.97
for line in sys.stdin:
    for token in re.findall("(''|``|--|[A-Z][a-z]{1,2}\.|\w+\.\w+\.\w+\.|\w+\.\w\.|\w+[\'\-]\w+|\d+.\d+|[#\$&%!?\"\.;,:`'+-]|[A-Z]\.|\w+)", line.strip()):
        print(token)
#(''|``|--|[A-Z][a-z]{1,2}\.|\w+\.\w+\.\w+\.|\w+\.\w\.|\w+[\'\-]\w+|\d+.\d+|[#\$&%!?\"\.;,:`'+-]|[A-Z]\.|\w+)