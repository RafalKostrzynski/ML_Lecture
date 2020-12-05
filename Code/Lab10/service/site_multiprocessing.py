import requests

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site_multiprocessing(url):
    session.get(url)