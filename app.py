from settings import API

# Version Name should be similar to the folder name
# Each folder should contain one urls.py file inside it
VERSIONS = [
    'v1',
    'v2',
    'v3'
]
api = application = API(versions=VERSIONS, middleware=[])
