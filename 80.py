"""Please write a program to generate all sentences where subject is in ["I", "You"] and
verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.
"""

data = ["I", "You", "Play", "Love", "Hockey", "Football"]
for subject in data[0:2]:
    for verb in data[2:4]:
        for object in data[4:]:
            print("{} {} {}".format(subject, verb, object))
