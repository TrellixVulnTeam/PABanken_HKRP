from pickle import FALSE, TRUE
import sqlalchemy


class ConfigDebug():
   SECRET_KEY = 'nowichange#!1212'
  #  SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Lsafms01a!@localhost/pabanken'
   SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root12345:Hejsan123#@pontus1920.mysql.database.azure.com/pabanken'    # File-based SQL database
   
   SQLALCHEMY_TRACK_MODIFICATION=FALSE


 # Flask-Mail SMTP server settings
   MAIL_SERVER = 'smtp.gmail.com'
   MAIL_PORT =587
   MAIL_USE_SSL = False
   MAIL_USE_TLS = False
   MAIL_USERNAME = 'pontusalm2022@example.com'     
   MAIL_PASSWORD = 'Pontusalm2022_!'
   MAIL_DEFAULT_SENDER = '"MyApp" <pontusalm2022@gmail.com>'

   # Flask-User settingsa
   USER_APP_NAME = "Flask-User Basic App"      # Shown in and email templates and page footers
   USER_ENABLE_EMAIL = True        # Enable email aution
   USER_ENABLE_USERNAME = False    # Disable username authentication
   USER_EMAIL_SENDER_NAME = USER_APP_NAME
   USER_EMAIL_SENDER_EMAIL = "noreply@example.com"  