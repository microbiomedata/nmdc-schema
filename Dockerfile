# Use Python 3.9 because that's the Python version listed in `pyproject.toml`.
FROM python:3.9

WORKDIR /nmdc-schema

# Download and install pandoc.
RUN apt update && \
    apt install -y \
      pandoc

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
# References:
# - https://sparrowflights.blogspot.com/2012/12/how-to-install-jena-command-line-tools.html
# - https://archive.apache.org/dist/jena/binaries/ (older binaries)
# - https://dlcdn.apache.org/jena/binaries/ (newest binaries, but download URL changes when new version is released).
RUN wget -P /downloads/tmp "https://archive.apache.org/dist/jena/binaries/apache-jena-4.9.0.zip"
RUN mkdir -p /downloads/apache-jena && \
    unzip /downloads/tmp/apache-jena-4.9.0.zip -d /downloads/apache-jena
RUN rm -rf /downloads/tmp/apache-jena-4.9.0.zip
ENV JENAROOT="/downloads/apache-jena/apache-jena-4.9.0"
ENV PATH="$JENAROOT/bin:$PATH"

# Install Poetry, a package manager for Python (an alternative to pip).
RUN pip install poetry

# Install the project's Python dependencies.
ADD ./poetry.lock    /nmdc-schema/poetry.lock
ADD ./pyproject.toml /nmdc-schema/pyproject.toml
RUN poetry install

# Run the MkDocs dev-server and configure it to accepts HTTP requests from outside the container.
# Reference: https://github.com/mkdocs/mkdocs/issues/1239#issuecomment-354491734
CMD ["poetry", "run", "mkdocs", "serve", "--dev-addr", "0.0.0.0:8000"]
