from shranjevanje_v_csv import shranjevanje_v_csv
from pobiranje_podatkov import v_datoteko
from izsluscenje_podatkov import pobiranje_podatkov

v_datoteko(50) #odločil sem se, da bom naložil prvih 50 strani(lahko jih tudi več samo potem shranjevanje in obdelava podatkov trajo malo dlje)
pobiranje_podatkov()
shranjevanje_v_csv()