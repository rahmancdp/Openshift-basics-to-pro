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

Below is the screenshot of official ubuntu base image which you can use for your container. It's just ~ 22 MB, isn't it very small ? on a contrary if you look at official ubuntu VM image it will be close to ~ 2.3 GB. So the container base image is almost 100 times less than VM image.

![Screenshot 2023-02-08 at 3 12 38 PM](https://user-images.githubusercontent.com/43399466/217493284-85411ae0-b283-4475-9729-6b082e35fc7d.png)

To provide a better picture of files and folders that containers base images have and files and folders that containers use from host operating system (not 100 percent accurate -> varies from base image to base image). Refer below.


### Files and Folders in containers base images

```
    /bin: contains binary executable files, such as the ls, cp, and ps commands.

    /sbin: contains system binary executable files, such as the init and shutdown commands.

    /etc: contains configuration files for various system services.

    /lib: contains library files that are used by the binary executables.

    /usr: contains user-related files and utilities, such as applications, libraries, and documentation.

    /var: contains variable data, such as log files, spool files, and temporary files.

    /root: is the home directory of the root user.
```


### Files and Folders that containers use from host operating system

```
    The host's file system: Docker containers can access the host file system using bind mounts, which allow the container to read and write files in the host file system.

    Networking stack: The host's networking stack is used to provide network connectivity to the container. Docker containers can be connected to the host's network directly or through a virtual network.

    System calls: The host's kernel handles system calls from the container, which is how the container accesses the host's resources, such as CPU, memory, and I/O.

    Namespaces: Docker containers use Linux namespaces to create isolated environments for the container's processes. Namespaces provide isolation for resources such as the file system, process ID, and network.

    Control groups (cgroups): Docker containers use cgroups to limit and control the amount of resources, such as CPU, memory, and I/O, that a container can access.
    
```

---

## Docker Overview

### What is Docker?

Docker is a platform that enables containerization. It helps you:
- Build container images
- Run containers from images
- Push and share container images in repositories like DockerHub

### Docker Architecture

![Docker Architecture](https://user-images.githubusercontent.com/43399466/217507877-212d3a60-143a-4a1d-ab79-4bb615cb4622.png)

### Docker LifeCycle 

We can use the above Image as reference to understand the lifecycle of Docker.

There are three important things,

1. docker build -> builds docker images from Dockerfile
2. docker run   -> runs container from docker images
3. docker push  -> push the container image to public/private regestries to share the docker images.

![Screenshot 2023-02-08 at 4 32 13 PM](https://user-images.githubusercontent.com/43399466/217511949-81f897b2-70ee-41d1-b229-38d0572c54c7.png)


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

# Docker Networking

Networking allows containers to communicate with each other and with the host system. Containers run isolated from the host system
and need a way to communicate with each other and with the host system.

By default, Docker provides two network drivers for you, the bridge and the overlay drivers. 

```
docker network ls
```

```
NETWORK ID          NAME                DRIVER
xxxxxxxxxxxx        none                null
xxxxxxxxxxxx        host                host
xxxxxxxxxxxx        bridge              bridge
```


### Bridge Networking

The default network mode in Docker. It creates a private network between the host and containers, allowing
containers to communicate with each other and with the host system.

![image](https://user-images.githubusercontent.com/43399466/217745543-f40e5614-ac34-4b78-85a9-91b24512388d.png)

If you want to secure your containers and isolate them from the default bridge network you can also create your own bridge network.

```
docker network create -d bridge my_bridge
```

Now, if you list the docker networks, you will see a new network.

```
docker network ls

NETWORK ID          NAME                DRIVER
xxxxxxxxxxxx        bridge              bridge
xxxxxxxxxxxx        my_bridge           bridge
xxxxxxxxxxxx        none                null
xxxxxxxxxxxx        host                host
```

This new network can be attached to the containers, when you run these containers.

```
docker run -d --net=my_bridge --name db training/postgres
```

This way, you can run multiple containers on a single host platform where one container is attached to the default network and 
the other is attached to the my_bridge network.

These containers are completely isolated with their private networks and cannot talk to each other.

![image](https://user-images.githubusercontent.com/43399466/217748680-8beefd0a-8181-4752-a098-a905ebed5d2a.png)


However, you can at any point of time, attach the first container to my_bridge network and enable communication

```
docker network connect my_bridge web
```

![image](https://user-images.githubusercontent.com/43399466/217748726-7bb347d0-3736-4f89-bdff-31d240b15150.png)


### Host Networking

This mode allows containers to share the host system's network stack, providing direct access to the host system's network.

To attach a host network to a Docker container, you can use the --network="host" option when running a docker run command. When you use this option, the container has access to the host's network stack, and shares the host's network namespace. This means that the container will use the same IP address and network configuration as the host.

Here's an example of how to run a Docker container with the host network:

```
docker run --network="host" <image_name> <command>
```

Keep in mind that when you use the host network, the container is less isolated from the host system, and has access to all of the host's network resources. This can be a security risk, so use the host network with caution.

Additionally, not all Docker image and command combinations are compatible with the host network, so it's important to check the image documentation or run the image with the --network="bridge" option (the default network mode) first to see if there are any compatibility issues.

### Overlay Networking

This mode enables communication between containers across multiple Docker host machines, allowing containers to be connected to a single network even when they are running on different hosts.

### Macvlan Networking

This mode allows a container to appear on the network as a physical host rather than as a container.


# Docker Volumes

## Problem Statement

It is a very common requirement to persist the data in a Docker container beyond the lifetime of the container. However, the file system
of a Docker container is deleted/removed when the container dies. 

## Solution

There are 2 different ways how docker solves this problem.

1. Volumes
2. Bind Directory on a host as a Mount

### Volumes 

Volumes aims to solve the same problem by providing a way to store data on the host file system, separate from the container's file system, 
so that the data can persist even if the container is deleted and recreated.

![image](https://user-images.githubusercontent.com/43399466/218018334-286d8949-d155-4d55-80bc-24827b02f9b1.png)


Volumes can be created and managed using the docker volume command. You can create a new volume using the following command:

```
docker volume create <volume_name>
```

Once a volume is created, you can mount it to a container using the -v or --mount option when running a docker run command. 

For example:

```
docker run -it -v <volume_name>:/data <image_name> /bin/bash
```

This command will mount the volume <volume_name> to the /data directory in the container. Any data written to the /data directory
inside the container will be persisted in the volume on the host file system.

### Bind Directory on a host as a Mount

Bind mounts also aims to solve the same problem but in a complete different way.

Using this way, user can mount a directory from the host file system into a container. Bind mounts have the same behavior as volumes, but
are specified using a host path instead of a volume name. 

For example, 

```
docker run -it -v <host_path>:<container_path> <image_name> /bin/bash
```

## Key Differences between Volumes and Bind Directory on a host as a Mount

Volumes are managed, created, mounted and deleted using the Docker API. However, Volumes are more flexible than bind mounts, as 
they can be managed and backed up separately from the host file system, and can be moved between containers and hosts.

In a nutshell, Bind Directory on a host as a Mount are appropriate for simple use cases where you need to mount a directory from the host file system into
a container, while volumes are better suited for more complex use cases where you need more control over the data being persisted
in the container.


## Advanced Steps to Create and Use a Docker Volume

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
