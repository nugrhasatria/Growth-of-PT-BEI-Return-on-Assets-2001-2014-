#   Visualisasi Data:
    # Pertumbuhan Laba Bersih PT BEI Periode 2001-2014
    # Pertumbuhan Total AKtiva PT BEI Periode 2001-2014
    # Pertumbuhan Return on Assets PT BEI Periode 2001-2014

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

#############################################################################################################################################

# Comparative Line Chart
    # Laba Bersih '2001-2007' vs Laba Bersih '2008-2014'

# Data for Net Income YoY 2001-2007
ni0107 = [1.684, 13.606, 15.134, 37.809, 57.449, 103.781, 307.702]
# Data for Net Income YoY 2008-2014
ni814 = [231.892, 341.886, 358.041, 299.816, 218.091, 182.412, 392.035]
# Years Index for X-Axis Top BEI Setelah Merger
niyearsx_top = ['2008', '2009', '2010', '2011', '2012', '2013', '2014']
# Years Index for X-Axis Bottom BEI Sebelum Merger
niyearsx_bottom = ['2001', '2002', '2003', '2004', '2005', '2006', '2007']
# Merge Datasets to Dataframe
kappa = {'Ytop': niyearsx_top, 'Ybottom': niyearsx_bottom, 'ni1': ni0107, 'ni2': ni814}
k = pd.DataFrame(kappa)

# First Axis by Bottom for Net Income YoY 2001-2007
fig,ax = plt.subplots()
ax.plot(k['Ybottom'], k['ni1'], color='orange', marker='o')
ax.set_xlabel('Periode Sebelum Merger', fontsize=12)
ax.set_ylabel('Nilai Laba Bersih', fontsize=12)

# Second Axis by Top for Net Income YoY 2008-2014
ax2 = ax.twiny()
ax2.plot(k['Ytop'], k['ni2'], color='blue', marker='o')
ax2.set_xlabel('Periode Setelah Merger', fontsize=12)

plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

# Defining legend style and data index
orange_line = mlines.Line2D([], [], color='orange', label='Sebelum Merger')
blue_line = mlines.Line2D([], [], color='blue', label='Setelah Merger')
plt.legend(handles=[blue_line, orange_line], loc= 'lower right')
plt.show()

############################################################################################################################################

# Comparative Line Chart
    # Total AKtiva '2001-2007' vs Total Aktiva '2008-2014'

# Data for Net Income YoY 2001-2007
ta0107 = [728.093, 689.866, 837.383, 876.097, 748.562, 1565.783, 3390.192]
# Data for Net Income YoY 2008-2014
ta0814 = [1615.787, 2823.306, 3556.881, 3673.291, 4531.882, 4476.596, 5367.495]
# Years Index for X-Axis Top BEI Sebelum Merger
tayearsx_top = ['2008', '2009', '2010', '2011', '2012', '2013', '2014']
# Years Index for X-Axis Bottom BEI Setelah Merger
tayearsx_bottom = ['2001', '2002', '2003', '2004', '2005', '2006', '2007']
# Merge Datasets to Dataframe
mu = {'Xtop': tayearsx_top, 'Xbottom': tayearsx_bottom, 'ta1': ta0107, 'ta2': ta0814}
m = pd.DataFrame(mu)

# First Axis by Bottom for Net Income YoY 2001-2007
fig,ax = plt.subplots()
ax.plot(m['Xbottom'], m['ta1'], color='orange', marker='o')
ax.set_xlabel('Periode Sebelum Merger', fontsize=12)
ax.set_ylabel('Nilai Total Aktiva', fontsize=12)

# Second Axis by Top for Net Income YoY 2008-2014
ax2 = ax.twiny()
ax2.plot(m['Xtop'], m['ta2'], color='blue', marker='o')
ax2.set_xlabel('Periode Setelah Merger', fontsize=12)

plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

# Defining legend style and data index
orange_line = mlines.Line2D([], [], color='orange', label='Sebelum Merger')
blue_line = mlines.Line2D([], [], color='blue', label='Setelah Merger')
plt.legend(handles=[blue_line, orange_line], loc= 'upper left')
plt.show()

############################################################################################################################################

# Comparative Line Chart
    # Laba Bersih dan Total Aktiva '01-'07 

# Data for Net Income 2001-2007
y = [1.684, 13.606, 15.134, 37.809, 57.449, 103.781, 307.702]
# Data for Total Assets 2001-2007
v = [728.093, 689.866, 837.383, 876.097, 748.562, 1565.783, 3390.192]
# Years Index for Y-Axis
x = ['2001', '2002', '2003', '2004', '2005', '2006', '2007']
# Merge Datasets to Dataframe
z = {'Year': x, 'Laba Bersih': y, 'Total Aktiva': v}
zeta = pd.DataFrame(z)

# First Axis for Net Income 2001-2007
fig,ax = plt.subplots()
ax.set_title('Laba Bersih dan Total Aktiva BEI: \n Periode Sebelum Merger (2001-2007)', loc='center', pad=20, fontsize=15, color='black')
ax.plot(zeta['Year'], zeta['Laba Bersih'], color='orange', marker='o')
ax.set_xlabel('Tahun', fontsize=15)
ax.set_ylabel('Nilai Laba Bersih (Jutaan Rupiah)', color='orange', fontsize=15)

# Second axis for Total Assets 2001-2007
ax2=ax.twinx()
ax2.plot(zeta['Year'], zeta['Total Aktiva'], color='blue', marker='o')
ax2.set_ylabel('Nilai Total Aktiva (Jutaan Rupiah)', color='blue', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

# Defining legend style and data index
orange_line = mlines.Line2D([], [], color='orange', label='Laba Bersih')
blue_line = mlines.Line2D([], [], color='blue', label='Total Aktiva')
plt.legend(handles=[blue_line, orange_line])
plt.show()

############################################################################################################################################

# Comparative Line Chart
    # Laba Bersih dan Total Aktiva '08-'14

# Data for Net Income 2008-2014
net_income814 = [231.892, 341.886, 358.041, 299.816, 218.091, 182.412, 392.035]
# Data for Total Assets 2008-2014
total_assets_814 = [1615.787, 2823.306, 3556.881, 3673.291, 4531.882, 4476.596, 5367.495]
# Years Index for Y-Axis
year_814 = ['2008', '2009', '2010', '2011', '2012', '2013', '2014']
# Merge Datasets to Dataframe
nty = {'a': net_income814, 'b': total_assets_814, 'c': year_814}
delta = pd.DataFrame(nty)

# First Axis for Net Income 2008-2014
fig,ax = plt.subplots()
fig,ax = plt.subplots()
ax.set_title('Laba Bersih dan Total Aktiva BEI: \n Periode Setelah Merger (2008-2014)', loc='center', pad=15, fontsize=15, color='black')
ax.plot(delta['c'], delta['a'], color='orange', marker='o')
ax.set_xlabel('Tahun', fontsize=15)
ax.set_ylabel('Nilai Laba Bersih (Jutaan Rupiah)', color='orange', fontsize=15)

# Second Axis for Total Assets 2008-2014
ax2=ax.twinx()
ax2.plot(delta['c'], delta['b'], color='blue', marker='o')
ax2.set_ylabel('Nilai Total Aktiva (Jutaan Rupiah)', color='blue', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

# Defining legend style and data index
orange_line = mlines.Line2D([], [], color='orange', label='Laba Bersih')
blue_line = mlines.Line2D([], [], color='blue', label='Total Aktiva')
plt.legend(handles=[blue_line, orange_line])
plt.show()

############################################################################################################################################

                                # RoA (Return on Assets)

# Comparative Line Chart
    # RoA '2001-2007' vs RoA '2008-2014'

# Data for RoA YoY 2001-2007
roa0107 = [0.23, 1.97, 1.81, 4.32, 7.67, 6.63, 9.08]
# Data for RoA YoY 2008-2014
roa0814 = [14.35, 12.11, 10.07, 8.16, 4.81, 4.07, 7.30]
# Years Index for X-Axis Top BEI Setelah Merger
roayearsx_top = ['2008', '2009', '2010', '2011', '2012', '2013', '2014']
# Years Index for X-Axis Bottom BEI Sebelum Merger
roayearsx_bottom = ['2001', '2002', '2003', '2004', '2005', '2006', '2007']
# Merge Datasets to Dataframe
tau = {'topY': roayearsx_top, 'bottomY': roayearsx_bottom, 'roa1': roa0107, 'roa2': roa0814}
t = pd.DataFrame(tau)

# First Axis by Bottom for Net Income YoY 2001-2007
fig,ax = plt.subplots()
ax.plot(t['bottomY'], t['roa1'], color='orange', marker='o')
ax.set_xlabel('Periode Sebelum Merger', fontsize=12)
ax.set_ylabel('Nilai Return on Assets ( % )', fontsize=12)

# Second Axis by Top for Net Income YoY 2008-2014
ax2 = ax.twiny()
ax2.plot(t['topY'], t['roa2'], color='blue', marker='o')
ax2.set_xlabel('Periode Setelah Merger', fontsize=12)

plt.grid(color='darkgray', linestyle=':', linewidth=0.5)

# Defining legend style and data index
orange_line = mlines.Line2D([], [], color='orange', label='Sebelum Merger')
blue_line = mlines.Line2D([], [], color='blue', label='Setelah Merger')
plt.legend(handles=[blue_line, orange_line], loc= 'lower right')
plt.show()

############################################################################################################################################