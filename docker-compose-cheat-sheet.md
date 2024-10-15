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
- [Include](#include)
- [Watch](#Watch)
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



## Basic Commands

Here are some of the most commonly used Docker Compose commands:

- Start services:

```bash
docker-compose up
```

- Start services in the background:

```bash
docker-compose up -d
```
- Stop services:

```bash
docker-compose stop
```

- Shut down services and remove containers, networks, and volumes:

```bash
docker-compose down
```

- View running services:

```bash
docker-compose ps
```

- View logs for all services:

```bash
docker-compose logs
```

- Execute a command inside a running container:

```bash
docker-compose exec <service_name> <command>
```



## Configuration

The `docker-compose.yml` file is where you define your services, networks, and volumes. Commonly used configuration options include:

- services: Defines the services (containers) for the application.
- networks: Specifies the networks to be created and used by services.
- volumes: Configures persistent data storage.
- build: Builds the image from a Dockerfile.

Example `docker-compose.yml`:

```yaml
services:
  app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - DEBUG=1
```

## Services

Each service defines a container that runs as part of your application. Here are some key options for defining services:

- image: The Docker image to use (e.g., `nginx:alpine`).
- build: Path to a directory containing a Dockerfile.
- ports: Exposes ports from the container to the host (e.g., "8080:80").
- volumes: Mounts host paths or named volumes into the container (e.g., `./app:/app`).
- environment: Sets environment variables inside the container (e.g., `DEBUG=1`).
- depends_on: Specifies dependencies between services.

## Volumes

Volumes provide persistent storage for containers. You can define volumes in two ways:

### Named Volumes

Defined in the volumes section of the Compose file and can be reused across services.

```yaml
volumes:
  data_volume:

services:
  app:
    volumes:
      - data_volume:/app/data
```

### Bind Mounts

Maps a directory on the host to a directory inside the container.

```yaml

services:
  app:
    volumes:
      - ./host_dir:/container_dir
```

To list volumes used by Docker Compose:

```bash
docker-compose volumes ls
```

## Network

Docker Compose automatically creates a default network for your application. You can define custom networks in the `docker-compose.yml` file:

```yaml
networks:
  app_network:

services:
  app:
    networks:
      - app_network
```

Types of networks:

- bridge (default): For isolated networks.
- host: Shares the host's network stack.
- overlay: Used for Docker Swarm services.

## Environment Variables

You can pass environment variables to services using either the environment key or by referencing an external `.env` file:
Example using the environment key:

```yaml
services:
  app:
    environment:
      - DEBUG=true
      - DATABASE_URL=postgres://db:5432/mydb
```

Example using a `.env` file:

```yaml
services:
  app:
    env_file:
      - .env
```

## Logging

You can configure logging drivers for services in Docker Compose:

```yaml
services:
  app:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

To view logs:

```bash
docker-compose logs
```

## Healthchecks

You can define health checks to ensure that services are running properly:

```yaml
services:
  app:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 30s
      timeout: 10s
      retries: 5
```  

## Dependencies

To define service startup dependencies, use the `depends_on` option. Note that this only ensures that containers are started in the correct order, but doesn't guarantee that the dependent service is ready (for this, use health checks):

```yaml
services:
  web:
    depends_on:
      - db
  db:
    image: postgres
```

## Extensions

Docker Compose extensions allow you to extend existing service definitions by inheriting configuration:

```yaml
services:
  base:
    image: busybox
    volumes:
      - ./shared:/mnt

  app:
    extends:
      service: base
    command: sleep 3600
```

## Include

Docker compose's `include` feature allows you to import and reuse configuration from other compose files.
This is useful for modularizing your Compose configurations and avoiding duplication.

```yaml
include:
  - service-b-include.yaml  # serviceB declaration
services:
  serviceA:
    build: .
    depends_on:
      - serviceB
```

## Watch

Docker Compose Watch is a feature in Docker Compose (introduced in v2.16.0) that automatically watches your project files for changes and updates the services in real-time, making it perfect for development environments.

**Key Features:**
- _Real-time updates_: Automatically rebuilds and restarts services when files change.
- _Development efficiency_: Eliminates the need to manually run `docker compose up` after each change.
- _Automatic rebuilds_: Detects changes in application code, Dockerfiles, and configuration files.
- _Customizable_: Supports custom watch configurations for different use cases.

```bash
docker compose up --watch
```
This command:
- Starts your services.
- Continuously monitors for file changes (e.g., code, configuration files).
- Automatically applies updates by restarting or rebuilding services as needed.

This is a development tool, and using it in production could result in unintended service disruptions.
Files such as Dockerfiles, docker-compose.yml, and mounted application files will be watched. Exact behavior depends on your project setup.

## References

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Docker Compose File Reference](https://docs.docker.com/reference/compose-file/)

This cheat sheet gives you an overview of the key features and commands in Docker Compose. For more advanced configurations, consult the official Docker documentation!
