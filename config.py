from pickle import FALSE, TRUE
import sqlalchemy


class ConfigDebug():
   SECRET_KEY = 'hammarbyisbest#team32'
  #  SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Lsafms01a!@localhost/pabanken'
   SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root12345:Hejsan123#@pontus1918.mysql.database.azure.com/pontus2022'    # File-based SQL database
   
   SQLALCHEMY_TRACK_MODIFICATION=FALSE


# flask 