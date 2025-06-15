import gspread
import awswrangler as wr
import boto3
from transform import format_columns
from airflow.models import Variable


def load_to_s3():
    # create a Google Sheet Client
    client = gspread.service_account(filename="credentials.json")

    # Read a Google Workbook by file_name
    workbook = client.open('class_list')
    workbook_names =  workbook.get_worksheet(0)

    # Pulling all records from sheet
    data = workbook_names.get_all_records()
    df = format_columns(data)

    # loading to s3 bucket
    session = boto3.Session(aws_access_key_id=Variable.get('access'),
                        aws_secret_access_key=Variable.get('secret'),
                        region_name=Variable.get('region')
                        )

    file_name = 'students_record.parquet'
    folder_name = 'students_folder'
    bucket = 'obinna-gsheet-bucket'
    path = f's3://{bucket}/{folder_name}/{file_name}'

    wr.s3.to_parquet(
        df=df,
        path=path,
        dataset=True,
        mode='append',
        boto3_session=session
    )

