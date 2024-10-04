library(arcgisbinding)
# install.packages("spdplyr")
library(spdplyr)

arc.check_product()

texas <- arc.open("D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/30/texas.shp")

print(texas@fields)

texas_df <- arc.select(texas, c("Shape", "NAME", "CNTY_FIPS", "FIPS"))
print(texas_df)
texas_sp <- arc.data2sp(texas_df)
# spplot(texas_sp)