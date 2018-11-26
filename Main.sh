#$1 est eccart à l'heure courante

# Importation des données
python ScriptRequeteMeteoFrance/RequeteAromeHD.py $1 SP1 #> data.grib2
./wgrib2
./wgrib2 data.grib2 -netcdf data.nc

# Traitement des données

# Création des fichiers KML
#Actuellement rien à faire (double clic sur test.kml)
#A faire pour animation
