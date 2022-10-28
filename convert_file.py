import pandas as pd 
import xlrd 
import openpyxl 
from io import StringIO  
import boto3 



BUCKET_IMPUT_FILE='s3://bucket/xslx/input/file.xlsx'
BUCKET_OUTPUT='s3://bucket_1/csv/output/'

def lambda_handler(event,context): 
    #leemos el xlsx con pandas y lo guardamos en un dataframe
    df=pd.read_excel(BUCKET_IMPUT_FILE, engine='openpyxl')    
    #file vacio
    csv_buffer = StringIO() 
    #pasamos el contenido del df en csv
    df.to_csv(csv_buffer) 

     #accedemos a s3 para crear el recurso con el metodo PUT
    s3_resource = boto3.resource('s3') 
    s3_resource.Object(BUCKET_OUTPUT,'output/file.csv').put(Body=csv_buffer.getvalue())