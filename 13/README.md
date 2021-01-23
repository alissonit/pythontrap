# COMMANDS


Commands used to manage `virtualenv`.

### LIST PACKAGES
```
pip list
```
### CREATE VIRTUALENV
```
python -m venv pythontrap_venv
```
### ACTIVATE VIRTUALENV
```
source pythontrap_venv/bin/activate
```
### SEE PATH PYTHON
```
which python
```
### INSTALL PACKAGE TO TEST
```
pip install flask
```
### GENERATE REQUIREMENTS.TXT
```
pip freeze > requirements.txt
```

### INSTALL REQUIREMENTS
```
pip install -r requirements.txt
```
### DEACTIVATE VIRTUALENV
```
deactivate 
```

### USE SYSTEM PACKAGES
```
python -m venv pythontrap_venv --system-site-packages
```

### LIST PACKAGE VENV LOCAL
```
pip list --local
```

### Links

- [pypi](https://pypi.org/)
- [about virtualenv](https://docs.python.org/pt-br/3/library/venv.html)
- [PEP-405](https://www.python.org/dev/peps/pep-0405/)
