#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#04/17/2022

FROM balenalib/raspberrypi3-debian-python:bullseye
ENV UDEV=yes

# Installations
# RUN apt-get -q update
# RUN apt-get install -yq wget gcc make 
# RUN apt-get install -yq python3-rpi.gpio python3-pip
# RUN apt-get install -yq bison libasound2-dev libsystemd-dev swig lirc lirc-compat-remotes
    # lirc
    # && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN install_packages wget build-essential\
    python3-gi\
    bison libasound2-dev libsystemd-dev swig\
    lirc lirc-compat-remotes

# Copy necessary config files
COPY /conf/config.txt /boot/
COPY /conf/modules /etc/
COPY /conf/py_reqs.txt /src/

# Run pip installatios
RUN pip install -r /src/py_reqs.txt --src /src

# Download and extract sphinx parts
RUN mkdir -p /src/sphinx
WORKDIR /src/sphinx
RUN wget -q https://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha/sphinxbase-5prealpha.tar.gz/download -O - \
    | tar -xz
RUN wget -q https://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha/pocketsphinx-5prealpha.tar.gz/download -O - \
    | tar -xz

# Compile sphinxbase
WORKDIR /src/sphinx/sphinxbase-5prealpha
RUN ./configure --enable-fixed \
    && make \
    && make install

# Compile pocketsphinx
WORKDIR /src/sphinx/pocketsphinx-5prealpha
RUN ./configure \
    && make \
    && make install

# Move code into the container
COPY /src /src
WORKDIR /src

# Needed so that sphinxbase and pocketsphinx can be recognized as installed
ENV PYTHONPATH /usr/local/lib/python3.7/site-packages

# Neeeded for lirc 
RUN mkdir /var/run/lirc

# This can be replaced with just starting our app once it's working
# CMD python3 main.py || bash
CMD bash -c "/etc/init.d/lircd start"
