# azure_blob_storage.py

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

class AzureBlobStorage:
    def __init__(self, connection_string, container_name, container_name_temp):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_client = self.blob_service_client.get_container_client(container_name)
        self.container_client_temp = self.blob_service_client.get_container_client(container_name_temp)

    def upload_blob(self, blob_name, data):
        blob_client = self.container_client.get_blob_client(blob_name)
        blob_client.upload_blob(data)
        blob_client_temp = self.container_client_temp.get_blob_client(blob_name)
        blob_client_temp.upload_blob(data)

    def list_blobs(self):
        return [blob.name for blob in self.container_client.list_blobs()]

    def download_blob(self, blob_name):
        blob_client = self.container_client.get_blob_client(blob_name)
        return blob_client.download_blob().readall()

    def list_blobs_temp(self):
        return [blob.name for blob in self.container_client_temp.list_blobs()]

    def download_blob_temp(self, blob_name):
        blob_client = self.container_client_temp.get_blob_client(blob_name)
        return blob_client.download_blob().readall()
    
    def delete_blob_temp(self, blob_name):
        # Get a reference to the blob to be deleted
        blob_client = self.container_client_temp.get_blob_client(blob_name)

        # Delete the blob
        blob_client.delete_blob()
