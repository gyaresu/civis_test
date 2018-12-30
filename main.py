# civis test
import os
import re

for each in os.environ:
  pattern = re.search('VS', each)
  if pattern:
    print(each)
