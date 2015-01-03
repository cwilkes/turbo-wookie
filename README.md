One time setup
==============

1. install homebrew http://brew.sh/
2. install pyenv virtualenv:
  1.  brew install pyenv-virtualenv
  2.  echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
  3.  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
3. restart shell
4. pyenv install --list   # see what versions are available
5. pyenv install <tab>
6. pyenv install 2.7.<tab>
7. pyenv install 2.7.9 # wait for download


Downloading code and initial setup
==============
1. git clone git@github.com:cwilkes/turbo-wookie.git pythonstarter
2. cd pythonstarter
3. install a virtualenv
  1. which python   # /usr/local/bin/python
  2. pyenv virtualenv <tab>
  3. pyenv virtualenv 2.7.9 pythonstarter
  4. pyenv local pythonstarter
  5. which python   # $HOME/.pyenv/versions/pythonstarter/bin/python
4. pip install -r requirements.txt # install all the needed python libraries
