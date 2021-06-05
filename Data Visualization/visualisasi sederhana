import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


table = pd.read_csv("https://academy.dqlab.id/dataset/penduduk_gender_head.csv")
table.head()

x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)), height=table['LAKI-LAKI WNI'], color='green')
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=89)
plt.title('Persebaran jumlah penduduk laki-laki di Jakarta Pusat', fontsize='15.5', color='green')
plt.xlabel('Kelurahan di Jakarta Pusat', color='yellow')
plt.ylabel('Jumlah penduduk laki-laki', color='red')
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.show()
