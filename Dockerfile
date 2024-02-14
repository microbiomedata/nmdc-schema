# Use Python 3.9 because that's the Python version listed in `pyproject.toml`.
FROM python:3.9

WORKDIR /nmdc-schema

# Download and install yq.
# Reference: https://github.com/mikefarah/yq#install
RUN wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/bin/yq && \
    chmod +x /usr/bin/yq

# Download and install a Java Development Kit >= 11.
#
# Note: This is a dependency of Apache Jena.
#
# Note: While developing this Dockerfile, we found that we could not get an ARM64 build of the JDK to run
#       in a container running in an amd64 environment, and vice versa. For that reason, here, we check the
#       environment type and use that information to decide which build of the JDK we will download.
#
# Reference: https://jdk.java.net/21/
#
RUN echo "Architecture: $(uname -m)"
RUN mkdir -p /downloads/tmp/
RUN if [ "$(uname -m)" = "aarch64" ]; \
    then wget -O /downloads/tmp/openjdk-21.0.2.tar.gz "https://download.java.net/java/GA/jdk21.0.2/f2283984656d49d69e91c558476027ac/13/GPL/openjdk-21.0.2_linux-aarch64_bin.tar.gz"; \
    else wget -O /downloads/tmp/openjdk-21.0.2.tar.gz "https://download.java.net/java/GA/jdk21.0.2/f2283984656d49d69e91c558476027ac/13/GPL/openjdk-21.0.2_linux-x64_bin.tar.gz"; \
    fi
RUN mkdir -p /downloads/openjdk && \
    tar -xvzf /downloads/tmp/openjdk-21.0.2.tar.gz -C /downloads/openjdk
RUN rm -rf /downloads/tmp/openjdk-21.0.2.tar.gz
ENV JAVA_HOME="/downloads/openjdk/jdk-21.0.2/"

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
# RUN poetry install

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
# launching mkdocs server had been ok on MacOS but not Ubuntu. Now this step is giving "mkdocs not installed" even in MacOS
CMD ["tail", "-f", "/dev/null"]