from abc import ABC

from google.cloud import storage
from typing import Optional, Dict, Any, List
import json
import requests
from bs4 import BeautifulSoup
from .secretmanager import SecretManager
from .base_fetcher import BaseFetcher
from itertools import chain


class GCPFetcher(BaseFetcher, ABC):
    def __init__(self, storage_client: Optional[storage.Client] = None, secret_client: SecretManager = None):
        super().__init__()
        self._storage_client = storage_client or storage.Client()
        self._secret_client = secret_client or SecretManager()

    @property
    def storage_client(self):
        return self._storage_client

    @property
    def secret_manager_client(self):
        return self._secret_manager_client

    def fetch_config(self, secret_name):
        return self._secret_client.access_secret_version(secret_name)

    def _read_from_gcp(self, bucket_name: str, blob_name: str = None) -> Dict[str, Any]:

        bucket = self._storage_client.get_bucket(bucket_name)

        if not blob_name:
            blobs = list(bucket.list_blobs())
            if not blobs:
                return []
            blob_name = blobs[0].name

        blob = bucket.get_blob(blob_name)

        if blob is None:
            return []

        content = blob.download_as_text()
        data = json.loads(content)
        return data

    def write_to_gcs(self, urls: List[str], bucket_name: str, folder_name: str):
        """
        Write images to Google Cloud Storage.
        """
        bucket = self._storage_client.bucket(bucket_name)

        for url in urls:
            response = requests.get(url, stream=True)

            if response.status_code == 200:
                # Extract file name from URL and create GCS blob name
                file_name = url.split('/')[-1]
                blob_name = f"{folder_name}/{file_name}"

                blob = bucket.blob(blob_name)
                blob.upload_from_string(response.content, content_type=response.headers['Content-Type'])

                print(f"Image {file_name} written to {blob_name} in bucket {bucket_name}")
            else:
                print(f"Failed to download {url}")