One time setup
==============

1. install homebrew http://brew.sh/
2. install pyenv virtualenv:
	a.  brew install pyenv-virtualenv
	b.  echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
	c.  echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.ash_profile
3. restart shell
4. pyenv install --list   # see what versions are available
5. pyenv install <tab>
6. pyenv install 2.7.<tab>
7. pyenv install 2.7.9 # wait for download


Downloading code and initial setup
==============
1. git clone .....
2. cd pythonstarter
3. install a virtualenv
	a. which python   # /usr/local/bin/python
	b. pyenv virtualenv <tab>
	c. pyenv virtualenv 2.7.9 pythonstarter
	d. pyenv local pythonstarter
	e. which python   # $HOME/.pyenv/versions/pythonstarter/bin/python
4. pip install -r requirements.txt # install all the needed python libraries
