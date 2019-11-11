## Purpose
The purpose of this template is to be used as a **repository template** when creating new repos.

## Makefile
The Makefile provides the following:
```
# make
  add-venv-py2.7            Install virtualenv, create virtualenv, install requirements
  add-venv-py3.6            Install virtualenv, create virtualenv, install requirements
  black-check               Perform Black formatting against py files. Check ONLY.
  black-diff                Perform formatting against py files. Diff ONLY.
  black                     Perform formatting against py files.
  install-py3.6             Install Python3.6
  lint-ansible              Perform linting against ansible yaml files
  lint-py                   Perform linting against py files
  lint                      Remove YAML EOL spaces, perform yaml and py linting.
  remove-yml-eol-spaces     Remove end of line spaces from yaml files
```

## Ansible
The included Ansible dir includes a predefined `ansible.cfg` file. 
If you are not using Ansible for your project feel free to delete the directory and remove the required entries from `requirements.txt`.
