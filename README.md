# Data analysis
- Document here the project: smr
- Description: Le Wagon Python Data Science final project: uses a neural network 
               to classify roofs based on the post code you supply. 
               This sister repo is for database recording of post-code search 
               and their results.
- Data Source: Training data source is the [INRIA](https://project.inria.fr/aerialimagelabeling/) 405 sq km labelled data
- Type of analysis: U-Net neural-network, using VGG-16 transfer learning

# Install
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

# Once installed: run

