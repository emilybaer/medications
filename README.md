# medications
Medications API coding challenge

## Install python 3 and pipenv

### Install python 3
Install python 3: 
```brew install python```

See which version of python you're using: 
```python --version```

If you still see 2.7 ensure in PATH /usr/local/bin/ takes precedence over /usr/bin/.
Alternatively, find where python 3 lives and fully qualify it when running applications:
```
which python3
/usr/local/bin/python3 my_project.py
```

### Install pipenv
Install pipenv: `brew install pipenv`

## Clone the repo

Clone the repo
`git clone https://github.com/emilybaer/medications.git`

## Run the code
To run the code
```
cd medications
pipenv run python main.py
```

A json file called *updates.json* will be created in the *medications* directory