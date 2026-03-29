## Install Python from (Windows)
[Download](https://www.python.org/ftp/python/pymanager/python-manager-26.0.msix)

## Clone repo from (Link)
```bash
git clone https://github.com/Ashish-rajpoot/sir_eci_photo_verify.git
```
> Note: Open folder in vs code & Run below cmd's
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
### Run 1: Cmd's
```bash
git clone https://github.com/Ashish-rajpoot/sir_eci_photo_verify.git
cd sir_eci_photo_verify
code .
```
### Run 2: Cmd's
```bash
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
python -m venv venv
venv\Scripts\activate
pip install selenium
pip install python-dotenv
pip install openpyxl
pip freeze > requirements.txt
python main.py
```