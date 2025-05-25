sudo apt install python3.10-venv

python3 -m venv env_d

source env_d/bin/activate

pip install -r requirements.txt

python -m ipykernel install --user --name=env_d --display-name "Python (env_d)"

