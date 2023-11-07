set table "Ch8_3.pgf-plot.table"; set format "%.5f"
set format "%.7e";;plot 'Data/Test1Results.csv' u 1:(1./14.) smooth kdensity
