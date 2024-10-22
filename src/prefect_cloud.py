from prefect import flow, task, get_run_logger
from prefect_email import EmailServerCredentials, email_send_message
import requests
import csv
import asyncio

@task
def extract_data():
    logger = get_run_logger()
    logger.info("Extracting data...")
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

@task
def transform_data(data):
    logger = get_run_logger()
    logger.info("Transforming data...")
    return [{"title": post["title"], "userId": post["userId"]} for post in data]

@task
def load_data(data):
    logger = get_run_logger()
    logger.info("Loading data to CSV file...")
    with open("output_data.csv", mode="w", newline="") as csv_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

@flow
def etl_pipeline():
    # Load the email credentials block
    email_credentials = EmailServerCredentials.load("my-email-credentials")

    try:
        # Logging and Observability
        data = extract_data()
        transformed_data = transform_data(data)
        load_data(transformed_data)

        # Send success notification email
        asyncio.run(email_send_message(
            subject="ETL Pipeline Completed Successfully!",
            msg="The ETL pipeline has completed successfully.",
            email_server_credentials=email_credentials,
            email_to=["i.linker8@gmail.com"]
        ))

    except Exception as e:
        # Send failure notification email
        asyncio.run(email_send_message(
            subject="ETL Pipeline Failed!",
            msg=f"The ETL pipeline failed with error: {e}",
            email_server_credentials=email_credentials,
            email_to=["i.linker8@gmail.com"]
        ))
        raise e

if __name__ == "__main__":
    etl_pipeline()