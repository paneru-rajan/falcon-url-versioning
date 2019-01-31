## An Example of URL Versioning with Falcon
An Example showing a simple way to add URL versioning in Falcon based Applications.

#### Installation
> I am using Python 3.6

Create a virtual env and Install the requirements
```
pip install -r requirements.txt
```
Run server
```
gunicorn app --reload
```

For v1 Open [http://localhost:8000/v1/things](http://localhost:8000/v1/things)

For v2 Open [http://localhost:8000/v2/things](http://localhost:8000/v2/things)

For v3 Open [http://localhost:8000/v3/things/Version-Three](http://localhost:8000/v3/things/Version-Three)

#### Configuration
###### Add version name in [app.py](app.py)
```
VERSIONS = [
    'v1',
    'v2',
    'v3'
]
```
> Version Name should be similar to the folder name

> Each folder should contain one `urls.py` file

###### Inside `urls.py` add urls
```
urls = [
    ('route', InstanceOfResources),
]
```
`urls` is a list of tuples, 1st parameter is route and 2nd is Instance of Resources


###### Reference
1. [Falcon Docs](https://falcon.readthedocs.io/en/stable/)
1. [Falcon Github](https://github.com/falconry/falcon)


###### &copy; Copyright
Do what you want.