FROM python:3.10

WORKDIR /nmdc-schema

# Install jq.
RUN apt-get update && \
    apt-get install -y jq

# Download and install yq.
# Reference: https://github.com/mikefarah/yq#install
RUN wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/bin/yq && \
    chmod +x /usr/bin/yq

# Install Poetry, a package manager for Python (an alternative to pip).
RUN pip install "poetry>=2.3.0"

# Install the project's Python dependencies.
ADD ./poetry.lock    /nmdc-schema/poetry.lock
ADD ./pyproject.toml /nmdc-schema/pyproject.toml
# TODO: Re-enable this as part of https://github.com/microbiomedata/nmdc-schema/issues/1744
# RUN poetry install

# Configure the container to display a welcome message and the OS name whenever
# someone starts an interactive shell session (i.e. "connects to the shell").
RUN echo "OS_NAME=\$(cat /etc/os-release | sed -n 's/PRETTY_NAME=\"\(.*\)\"/\\\1/p')" >> /etc/bash.bashrc
RUN echo "echo \"\""                                                                  >> /etc/bash.bashrc
RUN echo "echo \"    Welcome to this nmdc-schema development container,\""            >> /etc/bash.bashrc
RUN echo "echo \"    which is running \${OS_NAME}\"."                                 >> /etc/bash.bashrc
RUN echo "echo \"\""                                                                  >> /etc/bash.bashrc

# Run a "no-op" command that will keep the container running.
CMD ["tail", "-f", "/dev/null"]
