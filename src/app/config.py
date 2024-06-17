import urllib

class Config:
    DRIVER = 'ODBC Driver 17 for SQL Server'
    SERVER = 'localhost'
    DATABASE = 'ArandaCO46-2023-12-18-8-1'    
    params = urllib.parse.quote_plus(f"DRIVER={{{DRIVER}}};"
                                     f"SERVER={SERVER};"
                                     f"DATABASE={DATABASE};"
                                     f"Trusted_Connection=yes")
    
    SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc:///?odbc_connect={params}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
