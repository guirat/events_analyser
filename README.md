# events_analyser

This is an api that parse events data from giving input.

## Getting started
Dependencies required:
* Postgresql
* Makefile
* Python

Start by installing dependencies:

```
make install
```

Then run the app
```
make run
```
it will run on the default http://127.0.0.1:8000/

----------

to make migrations:
```
make migrations
```
to migrate:
```
make migrate
```

to lunch tests:
```
make test
```
to format the code for a better PEP8 friendly:
```
make format
```
to lint the code:
```
make lint
```
