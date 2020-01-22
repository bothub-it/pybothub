install:
	pipenv run python setup.py install

test:
	pipenv run python tests/tests.py

black:
	pipenv run black --target-version=py36 .   