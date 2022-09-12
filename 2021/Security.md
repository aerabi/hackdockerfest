# Docker Security Best Practices


## Go Rootless
- Run containers as a non-root user
- Let the application be owned by root, but executed by non-root
- Run Docker in rootless mode

## Go Distroless
- Create the smallest image possible
- Start from the scratch, using a multi-stage build

## Maintain Dependencies
- Use specific version numbers for dependencies and base images
- Update the dependencies and base image periodically
- Use a private registry
- Sign images

## Maintain Docker Context
- Limit your context
- Use `.dockerignore`

## Scan Your Images
- Docker scan
- Docker Hub scan
- Hadolint
- Snyk


