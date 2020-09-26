from google.cloud import bigquery

client = bigquery.Client()

def test_query():
    # Perform a query.
    QUERY = (
        'SELECT * FROM `msds-434-final-project.ncaa_basketball.mascots` '
        'LIMIT 100')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    for row in rows:
        print(row.name)