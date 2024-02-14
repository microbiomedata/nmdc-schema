# Development

## Development environment

This repository includes a container-based development environment. That environment consists of two containers:
- A custom container—running Linux—in which all the dependencies of this project are present (e.g. [OpenJDK](https://openjdk.org/), [Apache Jena](https://jena.apache.org/), [GNU make](https://www.gnu.org/software/make/manual/make.html), [yq](https://mikefarah.gitbook.io/yq/))
- A container based upon an "off-the-shelf" [container image](https://hub.docker.com/r/stain/jena-fuseki)—running [Fuseki](https://jena.apache.org/documentation/fuseki2/) (a SPARQL server)

Here's a diagram showing how a developer can access various parts of the development environment from a terminal running in the host environment (i.e. the environment _hosting_ the containers). 

```mermaid
---
title: Development environment
---
graph BT
    host_terminal["Terminal<br>(You are here)"]
    
    subgraph app_container["Container running `app` service"]
        mkdocs_server["MkDocs dev-server"]
        app_bash["bash shell"]
    end
    
    subgraph fuseki_container["Container running `fuseki` service"]
        fuseki_server["Fuseki web server"]
        fuseki_bash["bash shell"]
    end
    
    subgraph repo_file_tree["Repository file tree"]
        repo_root_dir[".<br>(Root)"]
        repo_fuseki_dir["./local/fuseki-data<br>(Fuseki data)"]
    end
    style repo_file_tree stroke-dasharray: 4
    
    %% Links:
    host_terminal -- "$ curl http://localhost:8000" --> mkdocs_server
    host_terminal -- "$ docker compose exec app bash" --> app_bash
    app_bash -- "# cd /nmdc-schema" --> repo_root_dir
    host_terminal -- "$ cd ." --> repo_root_dir
    host_terminal -- "$ curl http://localhost:3030" --> fuseki_server
    host_terminal -- "$ docker compose exec fuseki bash" --> fuseki_bash
    fuseki_bash -- "# cd /fuseki" --> repo_fuseki_dir["Fuseki data<br>directory"]
    repo_root_dir -. "cd local/fuseki-data" .-> repo_fuseki_dir
```

> Note: The containers can access the **host environment** using the [special hostname](https://docs.docker.com/desktop/networking/#i-want-to-connect-from-a-container-to-a-service-on-the-host), 
> `host.docker.internal`. In other words, anything you can access via `localhost` from within the host environment—for
> example, a MongoDB server or an SSH tunnel—you can access via `host.docker.internal` from within either of the
> containers.

### Usage

Here's how you can instantiate the development environment on your computer.

#### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/) is installed on your computer.
  - For example, version 24:
    ```shell
    $ docker --version
    Docker version 24.0.6, build ed223bc
    ```

#### Procedure

1. In the root folder of the repository, run the container.
   ```shell
   docker compose up --detach
   ```
   > The first time you run that, it will take several **minutes** to finish. During that time, 
   > Docker will be _building_ the container image for the custom container. 
   > When you run the command in the future, Docker will reuse that container image (unless you append `--build`).
   >
   > **Troubleshooting tip:** If Docker shows an error message saying "port is already allocated"; 
   > then change the command to `DOCS_PORT=1234 FUSEKI_PORT=5678 docker compose up --detach`
   > and re-run it (you can replace `1234` and `5678` with any other port numbers between `1024`-`65535`, inclusive).
   > You can try different port numbers until that error message stops appearing.
2. Connect to a bash shell running within the container running the `app` service.
   ```shell
   docker compose exec app bash
   ```
   > You can think of this as "`ssh`-ing" into a Linux system. In this case, the Linux system is a Docker container running on your computer, and you are using something other than `ssh` to communicate with it.
3. (Optional) Explore that container!
   ```shell
   $ whoami
   $ hostname
   $ uname -a
   # ...
   $ yq --version
   $ jena --version
   $ make --version
   $ python --version
   $ poetry --version
   $ ls /nmdc-schema
   ```
   > The root directory of the repository is mounted at `/nmdc-schema` within that container.
   > Changes you make in that directory on your computer will show up in `/nmdc-schema` within that container,
   > and vice versa. 
4. (Optional) Generate the MkDocs docs.
   ```shell
   $ make gendoc
   ```
5. (Optional) Visit the MkDocs dev-server.
   - In your web browser, visit http://localhost:8000
     > Note: If you customized `DOCS_PORT` earlier, use that port number instead of `8000` here.
6. Use the container running the `app` service, as your `nmdc-schema` development environment.
   ```shell
   $ poetry install
   $ make squeaky-clean
   $ poetry shell
   # etc.
   ```
7. (Optional) Visit the Fuseki web server.
   - In your web browser, visit http://localhost:3030
     > Note: If you customized `FUSEKI_PORT` earlier, use that port number instead of `3030` here.
8. (Optional) Done working on this project (e.g. for the day)? Stop the containers.
   ```shell
   docker compose down
   ```
