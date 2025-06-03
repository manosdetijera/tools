import os
import sys
import re

quick_file = sys.argv[1]

with open(quick_file) as f:
    contents = f.read()

pattern = re.compile(r"^([0-9]+)/(tcp|udp)", flags=re.MULTILINE)

matches = pattern.finditer(contents)

ports = []
for match in matches:
    ports.append(match.group(1))

print(",".join(ports))
