import re

with open("words.txt", "r") as f:
    lines = f.readlines()
    def test(l):
        return re.match('[a-z]+$', l)
    lines2 = [l.strip() for l in lines if test(l)]
print(lines2[10:50])
