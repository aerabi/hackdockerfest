# Docker Security Best Practices

Security is critical when working with Docker containers. This guide outlines best practices and recommendations for ensuring that your Docker environment and applications are secure.

## 1. Go Rootless

Running containers as root can be dangerous because any vulnerabilities in your containerized application may allow an attacker to escalate privileges. To reduce this risk, adopt the following practices:

### 1.1 Run Containers as a Non-Root User

Description: Configure containers to run with a non-root user to avoid giving processes within the container full root access to the host machine.

Example: In your Dockerfile, you can use the USER directive to specify a non-root user:

```dockerfile
FROM ubuntu:latest
RUN useradd -ms /bin/bash myuser
USER myuser
```

### 1.2 Let the Application Be Owned by Root, But Executed by Non-Root

Description: You can let root own application files while the process is run by a less privileged user.

Example: Ensure that files are owned by root and use the USER directive to execute the application with a lower privilege user:

```dockerfile
RUN chown -R root:myuser /myapp
USER myuser
CMD ["/myapp/start.sh"]
```

### 1.3 Run Docker in Rootless Mode

Description: Docker supports rootless mode, which allows you to run Docker as a regular user without requiring root privileges on the host system. This reduces the risk of privilege escalation.

Example: To run Docker in rootless mode, follow the official guide.

## 2. Go Distroless

Using smaller images reduces the attack surface and ensures that only necessary components are included.

### 2.1 Create the Smallest Image Possible

Description: Aim to build the smallest Docker image possible by removing unnecessary components and dependencies.

Example: Use a minimal base image like alpine or scratch:

```dockerfile
FROM scratch
COPY myapp /myapp
CMD ["/myapp"]
```

### 2.2 Start from Scratch Using Multi-Stage Builds

Description: Use multi-stage builds to separate the build environment from the runtime environment. Only copy the necessary artifacts into the final image.

Example:

```dockerfile
# Build stage
FROM golang:alpine AS builder
WORKDIR /src
COPY . .
RUN go build -o /app

# Final stage
FROM scratch
COPY --from=builder /app /app
CMD ["/app"]
```

## 3. Maintain Dependencies

### 3.1 Use Specific Version Numbers for Dependencies and Base Images

Description: Always pin versions of your base images and dependencies to ensure consistency across builds and to avoid pulling in unvetted updates.

Example:

```dockerfile
FROM node:14.17.0-alpine
```

### 3.2 Update Dependencies and Base Images Periodically

Description: Regularly update dependencies to incorporate the latest security patches.

Example: Schedule dependency checks in your CI/CD pipeline.

## 4. Use a Private Registry

### 4.1 Secure Your Image Distribution

Description: Use a private Docker registry to store and manage your images, ensuring that access to these images is controlled.

Example: Set up a private registry using Docker Hub or self-hosted options like Harbor.

### 4.2 Sign Images

Description: Use Docker Content Trust (DCT) to sign and verify the integrity of your images.

Example:

```bash
export DOCKER_CONTENT_TRUST=1
docker push your-repository/your-image
```

## 5. Maintain Docker Context

### 5.1 Limit Your Context

Description: Limit the size of the build context sent to the Docker daemon to reduce potential attack vectors.

Example: Use a .dockerignore file to exclude unnecessary files from the build context:

```
.git
node_modules
test/
```

### 5.2 Use .dockerignore

Description: Similar to .gitignore, the .dockerignore file ensures that sensitive or unnecessary files do not make it into the Docker build context.

Example:

```
.env
.git
node_modules
```

## 6. Scan Your Images

### 6.1 Docker Scan

Description: Docker provides a built-in security scanning tool to check for vulnerabilities in your images.

Example:

```bash
docker scan your-image
```

### 6.2 Docker Hub Scan

Description: If you use Docker Hub, it automatically scans images for vulnerabilities when they are pushed.

### 6.3 Hadolint

Description: Hadolint is a Dockerfile linter that helps you write Dockerfiles following best practices.

Example:

```bash
hadolint Dockerfile
```

### 6.4 Snyk

Description: Snyk can scan your images and Dockerfiles for vulnerabilities.

Example:

```bash
snyk container test your-image
```

## 7. Restrict Container Capabilities

### 7.1 Use Docker's --cap-drop and --cap-add

Description: Reduce the attack surface by dropping unnecessary Linux kernel capabilities and only granting what's strictly necessary.

Example:

```bash
docker run --cap-drop=ALL --cap-add=NET_BIND_SERVICE your-image
```

## 8. Use Read-Only Filesystem

### 8.1 Use the --read-only Flag

Description: Prevent modification of files within the container by mounting the filesystem as read-only. This ensures that an attacker cannot write to the filesystem.

Example:

```bash
docker run --read-only your-image
```

## 9. Limit Resource Consumption

### 9.1 Set CPU and Memory Limits

Description: To prevent containers from consuming excessive resources, configure limits on memory and CPU usage.

Example:

```bash
docker run --memory="256m" --cpus="1.0" your-image
```

## 10. Network Security

### 10.1 Use User-Defined Networks

Description: Isolate containers on user-defined networks rather than using the default bridge network.

Example:

```bash
docker network create mynetwork
docker run --network=mynetwork your-image
```

## 11. Keep Docker Updated

Description: Regularly update Docker to the latest version to ensure you are running the latest security patches and features.
##
By following these best practices, you can greatly improve the security of your Docker containers and minimize potential risks.
