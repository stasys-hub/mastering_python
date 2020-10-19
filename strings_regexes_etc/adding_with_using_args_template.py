import getopt
import sys

# Get the arguments from the command-line except the filename
argv = sys.argv[1:]
sum = 0

try:
    # Define the getopt parameters
    opts, args = getopt.getopt(argv, 'a:b:', ['foperand', 'soperand'])
    # Check if the options' length is 2 (can be enhanced)
    if len(opts) == 0 and len(opts) > 2:
      print ('usage: add.py -a <first_operand> -b <second_operand>')
    else:
      # Iterate the options and get the corresponding values
      for opt, arg in opts:
         sum += int(arg)
      print('Sum is {}'.format(sum))

except getopt.GetoptError:
    # Print something useful
    print ('usage: add.py -a <first_operand> -b <second_operand>')
    sys.exit(2)
