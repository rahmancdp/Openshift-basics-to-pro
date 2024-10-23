# Docker: Zero-to-Hero Course

Welcome to the Docker course! This guide will introduce you to Docker, a popular containerization tool that makes application deployment efficient and portable.

## Table of Contents
1. [What is a Container?](#what-is-a-container)
2. [Containers vs Virtual Machines](#containers-vs-virtual-machines)
3. [Why Are Containers Lightweight?](#why-are-containers-lightweight)
4. [Docker Overview](#docker-overview)
5. [Installing Docker on Linux](#installing-docker-on-linux)
6. [Basic Docker Commands](#basic-docker-commands)
    - Pulling an Image
    - Running an Image
    - Pushing an Image
7. [Container Runtime Basics](#container-runtime-basics)

---

## What is a Container?

A container is a lightweight unit of software that packages an application and all its dependencies, ensuring it runs the same regardless of the computing environment.

### Simple Explanation
Think of a container as a bundle that contains:
- The application
- Libraries required to run the application
- Minimal system dependencies

This enables easy, portable deployment.

![Container vs VM](https://user-images.githubusercontent.com/43399466/217262726-7cabcb5b-074d-45cc-950e-84f7119e7162.png)

---

## Containers vs Virtual Machines

### Key Differences:

- **Resource Utilization**: Containers share the host OS kernel, while VMs include a full OS, making containers more lightweight.
- **Portability**: Containers are more portable as they run on any compatible OS, unlike VMs that need hypervisors.
- **Security**: VMs offer better isolation with their dedicated OS, while containers share the host kernel.
- **Management**: Containers are easier to manage due to their minimal footprint.

---

## Why Are Containers Lightweight?

Containers use the host system’s OS kernel and libraries, minimizing their size compared to virtual machines. For example, a Docker container for Ubuntu is just around 22 MB, compared to a 2.3 GB VM image.

---

## Docker Overview

### What is Docker?

Docker is a platform that enables containerization. It helps you:
- Build container images
- Run containers from images
- Push and share container images in repositories like DockerHub

### Docker Architecture

![Docker Architecture](https://user-images.githubusercontent.com/43399466/217507877-212d3a60-143a-4a1d-ab79-4bb615cb4622.png)

### Docker Lifecycle
1. **docker build**: Build container images from a Dockerfile.
2. **docker run**: Run containers from images.
3. **docker push**: Push container images to a repository like DockerHub.

---

## Installing Docker on Linux

### Steps for Ubuntu

1. **Update your system**:
   ```bash
   sudo apt update
   ```
2. **Install Docker**:
   ```bash
   sudo apt install docker.io -y
   ```
3. **Start Docker Daemon**:
   ```bash
   sudo systemctl start docker
   ```
4. **Add your user to Docker group** (to avoid using `sudo` every time):
   ```bash
   sudo usermod -aG docker $USER
   ```
   - **Note**: Log out and log back in for this to take effect.

5. **Verify Docker Installation**:
   ```bash
   docker run hello-world
   ```

   You should see a message saying: 
   ```
   Hello from Docker!
   ```

---

## Basic Docker Commands

### Pulling an Image
To download an image from DockerHub:
```bash
docker pull ubuntu:latest
```

### Running an Image
To create and start a container from an image:
```bash
docker run -it ubuntu
```

### Pushing an Image
1. **Login to Docker**:
   ```bash
   docker login
   ```
2. **Push an Image**:
   ```bash
   docker push your-username/your-image-name:tag
   ```

---

## Container Runtime Basics

### What is a Container Runtime?

A container runtime is the software responsible for running containers. It manages container lifecycles, ensuring the isolation of resources while sharing the underlying host's operating system. Some common runtimes include:
- **Docker** (for Docker containers)
- **containerd** (Docker’s runtime)
- **CRI-O** (for Kubernetes)

### Who Invented Docker?

Docker was originally developed by Solomon Hykes at dotCloud in 2013. It evolved into a significant open-source project and is now a key part of many modern software deployment environments.

---

## Before Learning Kubernetes

Before diving into Kubernetes, it's important to understand:
1. **Docker Basics**: Building, running, and managing containers.
2. **Container Runtime**: The engine that runs your containers.
3. **Networking**: How containers communicate with each other.
4. **Volumes**: Persistent storage for containers.
