# Simple example of linear programming

# Let’s try to formalize an use-case and carry it forward throughout the article. Suppose you are a magical healer and you goal is to
# heal anyone who asks for help. The more you are able to heal someone, the better. Your secret behind the healing is 2 medicines, each of
# which uses special herbs. To create one unit of medicine 1, you need 3 units of herb A and 2 units of herb B. Similarly, to create one unit
# of medicine 2, you need 4 and 1 units of herb A and B respectively. Now medicine 1 can heal a person by 25 unit of health (whatever it
# is) and medicine 2 by 20 units. To complicate things further, you only have 25 and 10 units of herb A and B at your disposal. Now the
# question is, how many of each medicine will you create to maximize the health of the next person who walks in ?


# Let's identify the objective we want to optimize first:
# we create x units of medicine 1 and y units of medicine 2

# -> 25x + 20y = Health Restored       <-This is our objective function we want to maximize

# x = Units of med 1
# y = Units of med 2

# now let's deal with the constrains:
#   we need 3x + 4y units of Herb A to create med1/2, but we only have 25 units max:
#       3x +4y <= 25 
# Analogously for Herb 2:
#       2x + y <= 10
# Also amount created must be positive:
#       x >= 0
#       y >= 0



