## Create Virtual Environment
```bash
python -m venv venv
```

## In Command Prompt:
```bash 
venv\Scripts\activate
```
## Install Selenium

```bash 
pip install selenium
```
## Install Dotenv

```bash 
pip install python-dotenv
```
## Verify Installed Packages
```bash 
pip list
```


# Virtual environment not activating in PowerShell

## Run PowerShell as admin once and allow script execution:
```bash
Set-ExecutionPolicy RemoteSigned
```

Then activate again.

## Chrome driver issue

### Upgrade Selenium:
```bash
pip install --upgrade selenium
```

# Full Command List
```bash
mkdir selenium_project
cd selenium_project
python -m venv venv
venv\Scripts\activate
pip install selenium
pip install python-dotenv
pip freeze > requirements.txt
```