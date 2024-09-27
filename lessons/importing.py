"""Practice importing"""

from lessons.scope_practice import remove_chars

print(remove_chars("happy", "p"))
# since the the calls were put under the if name = main statement, now when this function is called, it won't print what is said on the previous file
# now it will use the function from the other file, but we don't have to worry about what was on the other file and we can create our own specifications
