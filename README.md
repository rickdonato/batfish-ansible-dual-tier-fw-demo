## Introduction
This repo contains the code, templates and playbooks that accompanies the:<br>
Hands-on Guide to Multi-Tiered Firewall Changes with Ansible and Batfish

## Installation
### Repo
```
git clone https://github.com/rickdonato/batfish-ansible-dual-tier-fw-demo
cd batfish-ansible-dual-tier-fw-demo
```
### Create VirtualEnv
```
make add-venv-py3.6
source venv/bin/activate
```
### VIRL topology
To spin up the VIRL topology run the command:
```
make start-virl-topology
```
Any issues stop/remove topology from VIRL UWM UI, and remove id file via `rm .virl/*/id`.

## Repo Layout
```

├── ansible
│   ├── ansible.cfg
│   ├── data
│   │   ├── bf_facts
│   │   │   ├── expected
│   │   │   │   ├── db.yml
│   │   │   │   ├── fw1.yml
│   │   │   │   ├── fw2.yml
│   │   │   │   └── websrv.yml
│   │   │   └── extract
│   │   │       ├── db.yml
│   │   │       ├── fw1.yml
│   │   │       ├── fw2.yml
│   │   │       └── websrv.yml
│   │   ├── snapshots
│   │   │   └── snapshot
│   │   │       ├── configs
│   │   │       │   ├── fw1.cfg
│   │   │       │   └── fw2.cfg
│   │   │       ├── hosts
│   │   │       │   ├── db.json
│   │   │       │   └── websrv.json
│   │   │       └── iptables
│   │   │           ├── db.iptables
│   │   │           └── websrv.iptables
│   │   └── templates
│   │       └── hosts.j2
│   ├── inventory
│   │   └── hosts
│   └── playbooks
│       ├── bf_gather_validate_facts.yml
│       ├── bf_init_snapshot.yml
│       ├── bf_validate_acls_flows.yml
│       ├── bf_validate_snapshot.yml
│       ├── create_bf_snapshot.yml
│       └── push_config.yml
├── Makefile
├── README.md
├── requirements.txt
└── topology.virl
```
Note: The playbooks that use the Batfish modules are named `bf_xxxxxx.yml`.


## Caveats
* **VIRL topology** - Cisco ASA requires a new key pair to be created on each boot. Therefore `crypto key generate rsa general-keys modulus 2048 noconfirm` is added to the configuration. This command however is removed if you perform an "extract configs" from within VIRL.
