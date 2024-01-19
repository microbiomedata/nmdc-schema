# Use Python 3.9 because that's the Python version listed in `pyproject.toml`.
FROM python:3.9

WORKDIR /nmdc-schema

# Download and install yq.
# Reference: https://github.com/mikefarah/yq#install
RUN wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/bin/yq && \
    chmod +x /usr/bin/yq

# Download and install a Java Development Kit >= 11.
# Note: This is a dependency of Apache Jena.
RUN wget -P /downloads/tmp "https://download.java.net/java/GA/jdk21.0.1/415e3f918a1f4062a0074a2794853d0d/12/GPL/openjdk-21.0.1_linux-aarch64_bin.tar.gz"
RUN mkdir -p /downloads/openjdk && \
    tar -xvzf /downloads/tmp/openjdk-21.0.1_linux-aarch64_bin.tar.gz -C /downloads/openjdk
RUN rm -rf /downloads/tmp/openjdk-21.0.1_linux-aarch64_bin.tar.gz
ENV JAVA_HOME="/downloads/openjdk/jdk-21.0.1/"

# Download and install Apache Jena.
#
# Note: The path, `~/apache-jena/bin`, is currently hard-coded in `project.Makefile`. So, here,
#       we create a symbolic link (i.e. filesystem shortcut) from that hard-coded path to where
#       we are storing Apache Jena, which is `/downloads/apache-jena/apache-jena-4.9.0/bin`.
#
# References:
# - https://archive.apache.org/dist/jena/binaries/ (older binaries, but download URLs remain constant)
# - https://dlcdn.apache.org/jena/binaries/        (newer binaries, but download URLs change over time)
#
RUN wget -P /downloads/tmp "https://archive.apache.org/dist/jena/binaries/apache-jena-4.9.0.zip"
RUN mkdir -p /downloads/apache-jena && \
    unzip /downloads/tmp/apache-jena-4.9.0.zip -d /downloads/apache-jena
RUN rm -rf /downloads/tmp/apache-jena-4.9.0.zip
ENV JENAROOT="/downloads/apache-jena/apache-jena-4.9.0"
ENV PATH="$JENAROOT/bin:$PATH"
RUN mkdir -p /root/apache-jena && \
    ln --symbolic "${JENAROOT}/bin" /root/apache-jena/bin

# Install Poetry, a package manager for Python (an alternative to pip).
RUN pip install poetry

# Install the project's Python dependencies.
ADD ./poetry.lock    /nmdc-schema/poetry.lock
ADD ./pyproject.toml /nmdc-schema/pyproject.toml
RUN poetry install

# Configure the container to display a welcome message and the OS name whenever
# someone starts an interactive shell session (i.e. "connects to the shell").
RUN echo "OS_NAME=\$(cat /etc/os-release | sed -n 's/PRETTY_NAME=\"\(.*\)\"/\\\1/p')" >> /etc/bash.bashrc
RUN echo "echo \"\""                                                                  >> /etc/bash.bashrc
RUN echo "echo \"    Welcome to this nmdc-schema development container,\""            >> /etc/bash.bashrc
RUN echo "echo \"    which is running \${OS_NAME}\"."                                 >> /etc/bash.bashrc
RUN echo "echo \"\""                                                                  >> /etc/bash.bashrc

# Run the MkDocs dev-server, configuring it to accept HTTP requests from outside the container.
# Reference: https://github.com/mkdocs/mkdocs/issues/1239#issuecomment-354491734
#CMD ["poetry", "run", "mkdocs", "serve", "--dev-addr", "0.0.0.0:8000"]
CMD ["tail, "-f", "/dev/null"]
