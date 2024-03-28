import re
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame
from pandas import Series

A = r't.acd?tor$'
B = r'^[a-z]{2,7}$'
C = r'^trac(tor|tion)'
D = r'^[^a-z]{2,7}'

S = r'a\\?y'

print(re.search(S, r"bba\y"))
print(re.search(S, r"a?y"))
print(re.search(S, r"ba\\y"))
print(re.search(S, r"a\\\\y"))