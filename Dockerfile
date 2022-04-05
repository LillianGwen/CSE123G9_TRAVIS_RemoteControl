FROM balenalib/raspberry-pi-debian:buster

# Installations
RUN apt-get -q update && apt-get install -yq \
    python3-dev python3-rpi.gpio\
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Move code into the container
COPY src /src
WORKDIR /src

# This can be replaced with just starting our app once it's working
CMD bash