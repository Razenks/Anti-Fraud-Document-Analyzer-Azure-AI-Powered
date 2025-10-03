import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")
    STORAGE_CONNECTION_STRING = os.getenv("STORAGE_CONNECTION_STRING")
    DOC_ENDPOINT = os.getenv("DOC_ENDPOINT")
    DOC_KEY = os.getenv("DOC_KEY")