from google.cloud import storage

def upload_file_to_gcs(file):
    client = storage.Client()
    bucket = client.get_bucket('my-bucket-5864')
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

def list_files_in_gcs():
    client = storage.Client()
    bucket = client.get_bucket('my-bucket-5864')
    return [blob.name for blob in bucket.list_blobs()]
