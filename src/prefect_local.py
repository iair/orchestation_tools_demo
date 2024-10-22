from prefect import flow, task
import requests
import csv

@task
def extract_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

@task
def transform_data(data):
    return [{"title": post["title"], "userId": post["userId"]} for post in data]

@task
def load_data(data):
    with open("../data/output_prefect_local.csv", mode="w", newline="") as csv_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

@flow
def etl_pipeline():
    data = extract_data()
    transformed_data = transform_data(data)
    load_data(transformed_data)
    
if __name__ == "__main__":
    etl_pipeline()