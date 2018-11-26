#$1 est eccart à l'heure courante

# Importation des données
rm data.grib2
python ScriptRequeteMeteoFrance/RequeteAromeHD.py $1 SP1
mv *.grib2 data.grib2
chmod +x wgrib2
./wgrib2
./wgrib2 data.grib2 -netcdf data.nc

# Traitement des données
pvpython ContourLine.py data.nc 250.0

# Création des fichiers KML
#Actuellement rien à faire (double clic sur test.kml)
