# medications
Medications API coding challenge

## Execution Instructions
This should work if you already have python 3. If not, go to Python Installation Instructions.

### Clone the repo

Clone the repo: 
`$ git clone https://github.com/emilybaer/medications.git`

### Run the code
Install the *requests* package: `$ pip install requests`

Run the code: `$ python3 medications/main.py`

A json file called *updates.json* will be created in the *medications* directory

## Python Installation Instructions
If you need to install python 3, follow these instructions.

### Install homebrew
You'll need homebrew to install python3 and pipenv.
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

If you don't want to keep homebrew, uninstall it with this command once you're done:
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
```

### Install python 3
Install python 3: 
```$ brew install python```

See which version of python you're using: 
```$ python --version```

If you still see 2.7 ensure in PATH /usr/local/bin/ takes precedence over /usr/bin/.
Alternatively, find where python 3 lives and fully qualify it when running applications:
```
$ which python3
/usr/local/bin/python3

$ /usr/local/bin/python3 my_project.py
```