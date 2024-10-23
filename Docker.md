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


# Docker Networking and Volumes: Simple Explanation

## Networking: How Containers Communicate

Containers run separately but often need to talk to each other or to your computer. Networking helps with this. Imagine it like a road between two houses—without a road, no one can visit the other house.

- **Bridge Network**: This is like a private road between the containers. They can communicate with each other without bothering anyone else.
  - You can create your own bridge network to control which containers can talk to each other.
  
- **Host Network**: This gives containers access to the same network as your computer. It’s like opening your home to the container, so it uses the same "road" as your PC. But be careful—this is less safe since the container can access your computer’s network directly.
  
- **Overlay Network**: This lets containers on different computers communicate, like a global road connecting houses in different cities.

Here are some simple examples for Docker **Networking** 
### Docker Networking Examples

#### 1. **Bridge Networking Example:**
The default network type in Docker. You can create a custom bridge network for your containers.

- **Create a custom bridge network:**
    ```bash
    docker network create my_bridge
    ```

- **Run a container attached to this custom network:**
    ```bash
    docker run -d --name web --network my_bridge nginx
    ```

- **List all networks, including your custom bridge:**
    ```bash
    docker network ls
    ```

- **Connect another container to the same network:**
    ```bash
    docker run -d --name app --network my_bridge alpine sleep 3600
    ```

- **Attach an existing container to a network:**
    ```bash
    docker network connect my_bridge web
    ```

Now, both containers (`web` and `app`) can communicate with each other through the `my_bridge` network.

#### 2. **Host Networking Example:**
This allows your container to share the host's network stack.

- **Run a container using host networking:**
    ```bash
    docker run -d --network host nginx
    ```

This makes the container share the same network interface as the host.

#### 3. **Overlay Networking Example (for Swarm mode):**
Overlay networks are used when you need containers to communicate across multiple hosts.

- **Create an overlay network (requires Docker Swarm):**
    ```bash
    docker network create -d overlay my_overlay
    ```

- **Run a service attached to the overlay network:**
    ```bash
    docker service create --name web --network my_overlay nginx
    ```


## Volumes: Persistent Storage

Normally, when a container is deleted, all its data is also deleted. Volumes allow containers to save data, like having a special storage box outside the house. Even if the container (house) is destroyed, the data in the volume (storage box) remains.

- **Volume**: A special space created by Docker to store data safely.
  - You can tell Docker to store container data in a volume using the `docker run` command.
  
- **Bind Mount**: This lets containers use a folder from your computer to store data. It’s like letting a container use a specific room in your house to store things.

 ### Why Use Volumes?
- Containers are **ephemeral** by design, meaning their file system disappears when the container stops.
- Volumes let you store data outside of the container, so even if the container is deleted, the data remains intact on the host.
  
### How Docker Volumes Work
When you create a volume, Docker handles the volume location and management automatically on the **host file system**. 

- You can **mount** a volume to a specific directory in the container. This directory in the container will store the data from the host, and any changes inside the container’s directory will be reflected in the host’s mounted volume, and vice versa.

#### Steps to Create and Use a Docker Volume

##### 1. **Create a Volume**
First, you create a volume using the `docker volume create` command. This volume will live on the host's file system.

```bash
docker volume create my_data_volume
```

- **Volume created**: Docker creates this volume in the background, but it doesn’t automatically attach to any container.

##### 2. **Mount a Volume to a Container**
When you run a container, you can **mount** the volume to a directory in the container using the `-v` option or `--mount`.

- **Mount the volume** to `/data` in the container:
  ```bash
  docker run -d -v my_data_volume:/data --name my_container ubuntu
  ```

In this example:
- **`my_data_volume`** is the volume you created.
- **`/data`** is the directory in the container where the volume is mounted.

##### 3. **How Mount Points Work**
- When you mount the volume to a container, Docker automatically connects the volume to the specified directory (e.g., `/data`) inside the container.
- **Mount Point**: This means that any files written inside `/data` in the container are actually stored on the host’s file system, in the volume you created.
- If you stop or delete the container, the data remains in the **volume** on the host and can be used by another container.

##### 4. **View Where the Volume is Stored**
To inspect the details of the volume (such as where it's stored on the host), you can use:

```bash
docker volume inspect my_data_volume
```

This command will output details like:
```json
[
    {
        "CreatedAt": "2024-10-23T12:00:00Z",
        "Driver": "local",
        "Mountpoint": "/var/lib/docker/volumes/my_data_volume/_data",
        "Name": "my_data_volume",
        "Scope": "local"
    }
]
```

- **Mountpoint**: This shows where the volume is located on the host. In this case, it’s in `/var/lib/docker/volumes/my_data_volume/_data`. This is the directory where all the data written to `/data` in the container will be saved on the host.

##### 5. **Using Volumes Across Multiple Containers**
You can use the same volume with multiple containers, so they share the same data. Here’s an example:

- Run a second container using the same volume:
  ```bash
  docker run -it -v my_data_volume:/data ubuntu bash
  ```

- Both containers (`my_container` and this new one) can now access and modify the same data in `/data`, since it's stored in the `my_data_volume`.

#### Example: Writing Data to a Volume

1. **Write a file in the container**:
   ```bash
   echo "Hello, Docker Volumes!" > /data/hello.txt
   ```

2. **Check the file on the host**: 
   Since the volume is mounted, this file will be saved in the volume’s directory on the host (`/var/lib/docker/volumes/my_data_volume/_data`).

3. **Stop the container**: 
   ```bash
   docker stop my_container
   ```

4. **Start a new container using the same volume**: 
   ```bash
   docker run -it -v my_data_volume:/data ubuntu bash
   ```

5. **Check if the file exists**:
   ```bash
   cat /data/hello.txt
   ```

   You'll see the content `"Hello, Docker Volumes!"` because it was saved in the volume.

---

### Key Points about Docker Volumes:
- **Persistent Data**: Data in volumes persists even when the container is removed.
- **Isolation**: Volumes are isolated from the container’s file system, ensuring independence between the container and stored data.
- **Multi-Container Sharing**: Multiple containers can share a volume, allowing them to read and write to the same data location.
- **Portable**: Volumes are portable between containers on the same host and can be backed up separately from the container’s lifecycle.

  

Now you can easily manage communication and data storage between your containers!




## Before Learning Kubernetes

Before diving into Kubernetes, it's important to understand:
1. **Docker Basics**: Building, running, and managing containers.
2. **Container Runtime**: The engine that runs your containers.
3. **Networking**: How containers communicate with each other.
4. **Volumes**: Persistent storage for containers.
