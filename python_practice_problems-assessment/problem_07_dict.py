# DICTIONARY
#
# Write a function named "my_map" that takes a dictionary as a parameter.
# Return another dictionary that consists of the key/value pairs from the
# argument where the values are tripled. Use any construct that you want to
# implement "my_map".
#
#
#
#  --- YOUR CODE HERE ---

def my_filter(dic):
    return {key: value * 3 for key, value in dic.items()}

#
#  ------ EXAMPLES ------
#
print('filter', my_filter({1: ".", 2: "..", 5: "..."}))     # => {1: "...", 2: "......", 3: "........."}
print('filter', my_filter({}))                              # => {}
print('filter', my_filter({1: 2, 2: 33, 5: 14}))            # => {1: 6, 2: 99, 5: 42}
