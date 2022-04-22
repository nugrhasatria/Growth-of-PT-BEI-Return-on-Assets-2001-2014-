import numpy as np


# Dataframe untuk menghitung Return on Assets (RoA) Year by Year (YoY) IDX tahun 2000-2014
    # ROA adalah suatu alat yang digunakan untuk menilai sejauh mana kemampuan berbagai aset yang dimiliki perusahaan untuk bisa menghasilkan laba.
        # Data diambil dari IDX Consolidated Income Statement / Laporan Tahunan PT Bursa Efek Indonesia
    # Laba Bersih (Net Income) yang digunakan adalah "Laba Bersih Tahun Berjalan"
    # Total Aset (Total Assets) yang digunakan adalah keseluruhan asset yang dimiliki IDX

                                #       #       #       #

                # Pertumbuhan Laba Bersih dan Total Aktiva PT BEI 2001-2014

# Datafrane variabel Net Income & Total Assets
            # Variable Laba Bersih
Laba_Bersih = [4.996, 1.684, 13.606, 15.134, 37.809, 57.449, 103.781, 307.702, 
                231.892, 341.886, 358.041, 299.816, 218.091, 182.412, 392.035]
            # Variable Total AKtiva
Total_Aktiva = [521.837, 728.093, 689.866, 837.383, 876.097, 748.562, 1565.783, 
                3390.192, 1615.787, 2823.306, 3556.881, 3673.291, 4531.882, 4476.596, 5367.495]

# Fungsi Hitung Perubahan Relatif pada Variebel Laba Bersih dan Total AKtiva:
def percent_change(value):
    output = []
    try:
        for index,i in enumerate(range(len(value))):
            if i == 0:
                output.append(i)
            else:
                old_num = value[index-1]
                new_num = value[index]                    
                output.append(round((((old_num-new_num)/old_num)*100), 2))
    except ZeroDivisionError:
            output.append(0)
    return output
 
# Hasil Fungsi Hitung Perubahan Relatif
#print('Perubahan Relatif pada Net Income YoY: ', percent_change(Laba_Bersih))
#print('Perubahan Relatif pada Total Aktiva YoY: ', percent_change(Total_Aktiva))

#######################################################################################################################

    # Statistika Deskriptif pada Pertumbuhan Laba Bersih dan Total Aktiva PT BEI
        # Periodesasi 2001-2007 adalah periode PT BEI Sebelum Merjer
        # Periodesasi 2008-2014 adalah periode PT BEI Setelah Merjer

# Periode Sebelum Merjer:
    # Variable Laba Bersih (2001-2007)
vbl_1b_17 = [1.684, 13.606, 15.134, 37.809, 57.449, 103.781, 307.702]
    # Variable Diff Laba Bersih (2001-2007)
vbl_dflb_17 = [-66.29, 707.96, 11.23, 149.83, 51.95, 80.65, 196.49]

    # Variable Total Aktiva (2001-2007)
vbl_ta_17 = [728.093, 689.866, 837.383, 876.097, 748.562, 1565.783, 3390.192]
    # Variable Diff Total Aktiva (2001-2007)
vbl_dfta_17 = [39.52, -5.25, 21.38, 4.62, -14.56, 109.17, 116.52]

# Periodesasi Setelah Merjer:
    # Variable Laba Bersih (2008-2014)
vbl_lb_814 = [231.892, 341.886, 358.041, 299.816, 218.091, 182.412, 392.035]
    # Variable Diff Laba Bersih (2008-2014)
vbl_dflb_814 = [-24.64, 47.43, 4.73, -16.26, -27.26, -16.36, 114.92]

    # Variable Total Aktiva (2008-2014)
vbl_ta_814 = [1615.787, 2823.306, 3556.881, 3673.291, 4531.882, 4476.596, 5367.495]
    # Variable Diff Total Aktiva (2008-2014)
vbl_dfta_814 = [-52.34, 74.73, 25.98, 3.27, 23.37, -1.22, 19.9]

#                       #                         #                               #
# (Total Value) Fungsi Hitung Jumlah Nilai Variabel
def sums_val(vbl):
    sums = 0
    for item in vbl:
        sums += item
    return sums

# (Average Value) Fungsi Hitung Nilai Rata-rata
def avg_val(vbl):
    jumlah = 0
    for item in vbl:
        jumlah += item
    avg = jumlah/len(vbl)
    return avg

# (Standar Deviation) Fungsi Hitung Nilai Standar Deviasi
def calculate_sdev_vbl(vbl):
    average_vbl = avg_val(vbl)
    varians = 0
    for item in vbl:
        varians += (item - average_vbl) ** 2
    varians /= len(vbl)
    sdev_vbl = varians ** (1/2)
    return sdev_vbl

# (Value - Count) Hasil Fungsi Hitung Statistika Deskriptif pada Variabel Laba Bersih dan Total Assets

    # Laba Bersih IDX 2001-2007:
#print('Sums Laba Bersih IDX 2001-2007: ', sums_val(vbl_1b_17))
#print('Rata-rata Laba Bersih IDX 2001-2007: ', avg_val(vbl_1b_17))
#print('Sums Perbedaan Relatif Laba Bersih IDX 2001-2007: ', sums_val(vbl_dflb_17))
#print('Rata-rata Perbedaan Relatif Laba Bersih IDX 2000-2007: ', avg_val(vbl_dflb_17))
#print('Standar Deviasi Laba Bersih IDX 2001-2007: ', calculate_sdev_vbl(vbl_1b_17))

    # Total Aktiva IDX IDX 2001-2007:
#print('Sums Total Aktiiva IDX 2001-2007: ', sums_val(vbl_ta_17))
#print('Rata-rata Total Aktiva IDX 2001-2007: ', avg_val(vbl_ta_17))
#print('Sums Perbedaan Relatif Total Aktiva IDX 2001-2007: ', sums_val(vbl_dfta_17))
#print('Rata-rata Perbedaan Relatif Total Aktiva IDX 2001-2007: ', avg_val(vbl_dfta_17))
#print('Standar Deviasi Total Aktiva IDX 2001-2007: ', calculate_sdev_vbl(vbl_ta_17))

    # Laba Bersih IDX 2008-2014:
#print('Sums Laba Bersih IDX 2008-2014: ', sums_val(vbl_lb_814))
#print('Rata-rata Laba bersih IDX 2008-2014: ', avg_val(vbl_lb_814))
#print('Sums Perbedaan Relatif Laba Bersih IDX 2008-2014: ', sums_val(vbl_dflb_814))
#print('Rata-rata Perbedaan Relatif Laba Bersih IDX 2008-2014 : ', avg_val(vbl_dflb_814))
#print('Standar Deviasi Laba Bersih IDX 2008-2014: ', calculate_sdev_vbl(vbl_lb_814))

    # Total Aktiva IDX 2008-2014:
#print('Sums Total Aktiva IDX 2008-2014: ', sums_val(vbl_ta_814))
#print('Rata-rata Total Aktiva IDX 2008-2014: ', avg_val(vbl_ta_814))
#print('Sums Perbedaan Relatif Total Aktiva IDX 2008-2014: ', sums_val(vbl_dfta_814))
#print('Rata-rata Perbedaan Relatif Total Aktiva IDX 2008-2014 : ', avg_val(vbl_dfta_814))
#print('Standar Deviasi Total Aktiva IDX 2008-2014: ', calculate_sdev_vbl(vbl_ta_814))

##########################################################################################################################

#       RETURN  ON  ASSETS      #       RETURN  ON  ASSETS      #       RETURN  ON  ASSETS      #       RETURN  ON  ASSETS

# Deskripsi Variabel yang diperlukan untuk menghitung RoA dalam bentuk class
class variable(object):
    def __init__(self, year, net_income, total_assets):
        self.year = year
        self.net_income = net_income
        self.total_assets = total_assets

variable_yoy = {
    # Net Income & Total Assets value by Year on Year
    "2000": variable("2000", 4996, 521837),
    "2001": variable("2001", 1684, 728093),
    "2002": variable("2002", 13606, 689866),
    "2003": variable("2003", 15134, 837383),
    "2004": variable("2004", 37809, 876097),
    "2005": variable("2005", 57449, 748562),
    "2006": variable("2006", 103781, 1565783),
    "2007": variable("2007", 307702, 3390192),
    "2008": variable("2008", 231892, 1615787),
    "2009": variable("2009", 341886, 2823306),
    "2010": variable("2010", 358041, 3556881),
    "2011": variable("2011", 299816, 3673291),
    "2012": variable("2012", 218091, 4531882),
    "2013": variable("2013", 182412, 4476596),
    "2014": variable("2014", 392035, 5367495)
    }

# Fungsi Hitung Return on Assets (RoA)
    # RoA = Net Income dibagi Total Assets dikali 100%
for variable in variable_yoy.values():
    roa =  round(((variable.net_income / variable.total_assets) * 100), 2)

# Hasil Perhitungan Roa YoY
#print('RoA ' + 'tahun ' + str(variable.year) + ' = ' + str(roa))

##########################################################################################################################

                            # Pertumbuhan Return on Assets PT BEI

# Dataframe Roa YoY (2000-2014)
roa_yoy =   [0.96, 0.23, 1.97, 1.81, 4.32, 7.67, 6.63, 9.08,
             14.35, 12.11, 10.07, 8.16, 4.81, 4.07, 7.30]

# Fungsi Hitung Perubahan Relatif pada Variebel Return on Assets:
def percent_change(value):
    output = []
    try:
        for index,i in enumerate(range(len(value))):
            if i == 0:
                output.append(i)
            else:
                old_num = value[index-1]
                new_num = value[index]                    
                output.append(round((((old_num-new_num)/old_num)*100), 2))
    except ZeroDivisionError:
            output.append(0)
    return output

# Hasil Fungsi Hitung Perubahan Relatif
#print('Perubahan Relatif pada RoA YoY: ', percent_change(roa_yoy))

#######################################################################################################################

        #   Statistika Deskriptif pada Pertumbuhan RoA 
                # Periodesasi 2001-2007 adalah periode PT BEI Sebelum Merjer
                # Periodesasi 2008-2014 adalah periode PT BEI Setelah Merjer

# RoA Berdasarkan Periode:
    # Periode 2001-2007
RoA_17 =   [0.23, 1.97, 1.81, 4.32, 7.67, 6.63, 9.08]
    # Perubahan Relatif pada Periode 2001-2007
RoA_diff_17 = [-76.04, 756.52, -8.12, 138.67, 77.55, -13.56, 36.95]
    # Periode 2008-2014
RoA_814 =  [14.35, 12.11, 10.07, 8.16, 4.81, 4.07, 7.30]
    # Perubahan Relatif pada Periode 2008-2014
RoA_diff_814 = [58.04, -15.61, -16.85, -18.97, -41.05, -15.38, 79.36]

# (Total Value) Fungsi Hitung Jumlah Nilai RoA tiap Periode
def sums_val(RoA):
    sums = 0
    for item in RoA:
        sums += item
    return sums

# (Average Value) Fungsi Hitung Nilai Rata-rata
def avg_val(RoA):
    jumlah = 0
    for item in RoA:
        jumlah += item
    avg = jumlah/len(RoA)
    return avg

# (Standard Deviation) Fungsi Hitung Nilai Standar Deviasi RoA
def calculate_sdev_RoA(RoA):
    average_vbl = avg_val(RoA)
    varians = 0
    for item in RoA:
        varians += (item - average_vbl) ** 2
    varians /= len(RoA)
    sdev_vbl = varians ** (1/2)
    return sdev_vbl

# (Value - Count) Hasil Fungsi Hitung Statistika Deskriptif pada Variabel RoA 

# RoA IDX 2001-2007:
#print('Sums Nilai RoA IDX 2001-2007: ', sums_val(RoA_17))
#print('Rata-rata Nilai RoA IDX 2001-2007: ', avg_val(RoA_17))
#print('Standar Deviasi Nilai RoA IDX 2001-2007 adalah: ', calculate_sdev_RoA(RoA_17))

# Diff RoA IDX 2001-2007:
#print('Sums Perbedaan Nilai RoA IDX 2001-2007: ', sums_val(RoA_diff_17))
#print('Rata-rata Perbedaan Nilai RoA IDX 2001-2007: ', avg_val(RoA_diff_17))

# RoA IDX 2008-2014:
#print('Sums Nilai RoA IDX 2008-2014: ', sums_val(RoA_814))
#print('Rata-rata Nilai RoA IDX 2008-2014: ', avg_val(RoA_814))
#print('Standar Deviasi Nilai RoA IDX 2008-2014 adalah: ', calculate_sdev_RoA(RoA_814))

# Diff IDX 2008-2014:
#print('Sums Perbedaan Nilai RoA IDX 2008-2014: ', sums_val(RoA_diff_814))
#print('Rata-rata Perbedaan Nilai RoA IDX 2008-2014: ', avg_val(RoA_diff_814))

#####################################################################################################################