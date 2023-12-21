# Use Python 3.9 because that's the Python version listed in `pyproject.toml`.
FROM python:3.9

WORKDIR /src

# Download and install pandoc.
RUN apt update && \
    apt install -y \
      pandoc

# Download and install yq.
# Reference: https://github.com/mikefarah/yq#install
RUN wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/bin/yq && \
    chmod +x /usr/bin/yq

# Download and install Apache Jena.
# References:
# - https://sparrowflights.blogspot.com/2012/12/how-to-install-jena-command-line-tools.html
# - https://archive.apache.org/dist/jena/binaries/ (older binaries)
# - https://dlcdn.apache.org/jena/binaries/ (newest binaries, but download URL changes when new version is released).
RUN wget -P /downloads/tmp "https://archive.apache.org/dist/jena/binaries/apache-jena-4.9.0.zip"
RUN unzip /downloads/tmp/apache-jena-4.9.0.zip -d /downloads/apache-jena
ENV JENAROOT="/downloads/apache-jena/apache-jena-4.9.0"
ENV PATH="$JENAROOT/bin:$PATH"

RUN pip install poetry

ADD . /src/
RUN poetry install

CMD ["echo", "Hello and goodbye."]