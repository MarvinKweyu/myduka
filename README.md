# Myduka
An online shopping experience. The e-commerce system Kenya needs.

## Setup 
---

### Bare metal
**Base requirements:** 

**Install postgresql and rabbitMQ on your host machine**

Setup a virtual environment, install requirements , run migrations and run the server

```bash
bash develop.sh
```

### It just works(Docker)  - WIP

**Development**

With *docker* and *docker-compose* installed , clone the repo and run the following command at the root of the project.
```bash
docker-compose -f docker-compose.yml up -d --build

```

**Production**

```bash
docker-compose -f docker-compose.prod.yml up -d --build

```

Access the project via: 1**27.0.0.1:8000/**%