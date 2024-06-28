# Data analysis
- Document here the project: smr
- Description: Le Wagon Python Data Science final project: uses a neural network 
               to classify roofs based on the post code you supply. 
- Data Source: Training data source: 
- Type of analysis:

Please document the project the better you can.

# Install & run

Go to `git@github.com:hughharford/smr.git` to see the project

Install virtualenv if you don't have it already
Create a python3 virtual environment called 'smr_env' and set it locally:

```bash
sudo apt-get install virtualenv python-pip python-dev
pyenv virtualenv 3.10.6 smr_env
pyenv local smr_env 
```

Clone the project via ssh (presume you've got this sorted) and install it:

```bash
git clone git@github.com:hughharford/smr.git
cd smr
pip install -r requirements.txt
make clean install test                # install and test
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
smr-run
```
