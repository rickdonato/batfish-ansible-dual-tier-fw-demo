## Introduction
TBC

## Installation
TBC

## Manual Testing
### From Client to Web
client - `nc 10.0.1.1 80`
webserver - `nc -vv -l -p 80`

### From Web to DB
client - `nc 10.0.1.1 3306`
webserver - `nc -vv -l -p 3306`

## Caveats
* **VIRL topology** - Cisco ASA requires a new key pair to be created on each boot. Therefore `crypto key generate rsa general-keys modulus 2048 noconfirm` is added to the configuration. This command however is removed if you perform an "extract configs" from within VIRL.

## Links 
https://github.com/batfish/ansible/tree/master/docs
