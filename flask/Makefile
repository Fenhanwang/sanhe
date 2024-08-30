init:
	pip3 install --user pipenv;
	pipenv install;
	pipenv requirements > requirements.txt;

testing:
	pipenv sync --dev;

s: #trigger local server
	flask run --host=0.0.0.0 --port=9090;
	

deploying:
	pipenv requirements > requirements.txt;