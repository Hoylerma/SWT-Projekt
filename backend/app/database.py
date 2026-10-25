from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

from .config import database_url

url = database_url()
if url.startswith("sqlite"):
    engine = create_engine(url, connect_args={"check_same_thread": False}, poolclass=StaticPool)
else:
    engine = create_engine(url)
