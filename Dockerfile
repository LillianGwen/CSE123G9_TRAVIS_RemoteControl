#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#04/17/2022


FROM balenalib/raspberry-pi-debian:buster

# Installations
RUN apt-get -q update
RUN apt-get install -yq wget gcc make
RUN apt-get install -yq python3-dev python3-rpi.gpio python3-pip
RUN apt-get install -yq bison libasound2-dev swig lirc
    # && apt-get clean && rm -rf /var/lib/apt/lists/*

# Python installations
RUN pip3 install lirc

# Download and extract sphinx parts
RUN mkdir -p /src/sphinx
WORKDIR /src/sphinx
RUN wget -q https://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha/sphinxbase-5prealpha.tar.gz/download -O - \
    | tar -xz
RUN wget -q https://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha/pocketsphinx-5prealpha.tar.gz/download -O - \
    | tar -xz

# Compile sphinxbase
WORKDIR /src/sphinx/sphinxbase-5prealpha
RUN ./configure --enable-fixed >/dev/null \
    && echo "Done configuring sphinxbase" \
    && make >/dev/null \
    && echo "Done making sphinxbase" \
    && make install >/dev/null \
    && echo "Done installing sphinxbase"

# Compile pocketsphinx
WORKDIR /src/sphinx/pocketsphinx-5prealpha
RUN ./configure >/dev/null \
    && echo "Done configuring pocketsphinx" \
    && make >/dev/null \
    && echo "Done making pocketsphinx" \
    && make install >/dev/null \
    && echo "Done installing pocketsphinx"

# Move LIRC config
COPY /conf/config.txt /boot/
COPY /conf/hardware.conf /etc/lirc/
COPY /conf/lirc_options.conf /etc/lirc/
COPY /conf/modules /etc/

# Move code into the container
COPY /src /src
WORKDIR /src

# Needed so that sphinxbase and pocketsphinx can be recognized as installed
ENV PYTHONPATH /usr/local/lib/python3.7/site-packages

# This can be replaced with just starting our app once it's working
# CMD python3 main.py || bash
CMD bash
