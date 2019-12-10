# This week's exercise might seem a bit uninteresting at first because it involves working with an HTML-like syntax at a low level. The purpose this week isn't to familiarize yourself with HTML, but to get some practice with string manipulation in Python.

# This week I'd like you to write a function that accepts two strings containing
# opening HTML tags and returns True if they have the same attributes with the same values.

# Some examples of basic tag comparisons I'd like you to handle:

# >>> tags_equal("<img src=cats.jpg width=20>", "<IMG SRC=Cats.JPG height=40")
# True
# >>> tags_equal("<img src=dogs.jpg width=99>", "<img src=dogs.jpg width=20>")
# False
# >>> tags_equal("<p>", "<P>")
# True
# >>> tags_equal("<b>", "<p>")
# False
# This might sound complex and it sort of is.

# To make things a little easier:

# Assume attributes don't have double/single quotes around them and don't contain spaces (until you get bonus 3)
# Don't worry about repeated attribute names or value-less attributes.
# Assume there won't be repeats (until you get to bonus 1)
# Assume all attributes are key-value pairs (until you get to bonus 2)
# Assume attributes have no whitespace around them (key=value and never key = value)
# But your function must:

# Ignore order of attributes: the same attribute names/values in different order
# should be equivalent
# Ignore case for both attribute names and values (yes even ignore case for attribute values)
# I encourage you to try solving this exercise without using the standard library at first.
# Everything but the last bonus should be relatively do-able without importing any libraries.

# If you get your tests to pass, consider doing some of these bonuses. Make sure you don't
# spend too much time trying to get the second or third bonus done though.

# Bonus 1

# For the first bonus, I'd like you to handle duplicate attribute names by allowing the
# first one to "win" (ignoring any before the last) ✔️:

# >>> tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_email>")
# True
# >>> tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_username>")
# False
# Bonus 2

# For the second bonus, I'd like you to allow attributes without a value ✔️:

# >>> tags_equal("<OPTION NAME=Hawaii SELECTED>", "<option selected name=hawaii>")
# True
# >>> tags_equal("<option name=hawaii>", "<option name=hawaii selected>")
# False
# Bonus 3

# For the third bonus I'd like you to handle single/double quotes around attribute values and attribute values to have spaces in them ✔️:

# >>> tags_equal("<input value='hello there'>", '<input value="hello there">')
# True
# >>> tags_equal("<input value=hello>", "<input value='hello'>")
# True
# >>> tags_equal("<input value='hi friend'>", "<input value='hi there'>")
# False
# That last bonus may be pretty tricky and I recommend you reach for the standard library if you attempt it.

import shlex


class HtmlTag:
    def __init__(self, input_string):
        self._html = input_string.casefold()
        self.tag_name = ""
        self.attributes = {}
        self.parse_input()

    def parse_input(self):
        base_str = self._html.replace("<", "").replace(">", "")
        tokens = shlex.split(base_str)
        self.tag_name = tokens[0]
        if len(tokens) <= 1:
            return
        for t in tokens[1:]:
            if "=" not in t:
                self.attributes[t] = True
                continue
            key, value = t.split("=")
            if key in self.attributes:
                continue
            self.attributes[key] = value

    def __eq__(self, other):
        for k, v in self.attributes.items():
            if k not in other.attributes:
                return False
            if self.attributes[k] != other.attributes[k]:
                return False
        return self.tag_name == other.tag_name


def tags_equal(input1, input2):
    tag1 = HtmlTag(input1)
    tag2 = HtmlTag(input2)
    return tag1 == tag2
