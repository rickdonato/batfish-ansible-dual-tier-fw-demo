## Introduction
This repo contains the code, templates and playbooks that accompanies the:
Hands-on Guide to Multi-Tiered Firewall Changes with Ansible and Batfish

## Installation
TBC

## Caveats
* **VIRL topology** - Cisco ASA requires a new key pair to be created on each boot. Therefore `crypto key generate rsa general-keys modulus 2048 noconfirm` is added to the configuration. This command however is removed if you perform an "extract configs" from within VIRL.
