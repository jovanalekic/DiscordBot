import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

data = pd.read_excel('GooglePlaystore.xlsx')

data = data[data['Reviews'] != '3.0M']
data = data.dropna()

print(data.shape)
if data.shape == (9360, 13):
  print("this works")

def is_varies_with_device(value):
  return value == "Varies with device"

varies_with_device = data.applymap(is_varies_with_device)
contains_varies_with_device = varies_with_device.any(axis=1)
does_not_contain_varies_with_device = ~contains_varies_with_device
data = data[does_not_contain_varies_with_device]


regex = r'(\d+\.\d+(\.\d+)?)'

data['Android Ver'] = data['Android Ver'].str.extract(regex, expand=False)[0]


# Remove commas and plus signs from the "Installs" column
data['Installs'] = data['Installs'].str.replace(',', '').str.replace('+', '')
data['Installs'] = pd.to_numeric(data['Installs'], errors='coerce')
data = data.dropna(subset=['Installs'])
data['Installs'] = data['Installs'].astype(int)