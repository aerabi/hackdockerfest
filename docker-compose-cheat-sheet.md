# Docker Compose Cheat Sheet

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.

This cheat sheet is a quick reference for the most common Docker Compose commands and options.

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Basic Commands](#basic-commands)
- [Configuration](#configuration)
- [Services](#services)
- [Volumes](#volumes)
- [Networks](#networks)
- [Environment Variables](#environment-variables)
- [Logging](#logging)
- [Healthchecks](#healthchecks)
- [Dependencies](#dependencies)
- [Extensions](#extensions)
- [References](#references)

## Installation

Docker Compose is included with Docker Desktop for Windows and macOS. On Linux, you can download Compose as a Docker CLI plugin:

```bash
sudo apt install docker-compose-plugin
```

Please refer to the [official installation guide](https://docs.docker.com/compose/install/linux/) for more Linux installation options.

## Getting Started

To get started with Docker Compose, create a `docker-compose.yml` file in your project directory. Here is an example file:

```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
```

Then, run the following command to start the services:

```bash
docker compose up
```


