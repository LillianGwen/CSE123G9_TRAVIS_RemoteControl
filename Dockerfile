#CSE123 Group 9:
#The T.R.A.V.I.S. Project
#Ann Sophie Abrahamsson, Nathan Banner, Lillian Gwendolyn, Katy Johnson, Aidan Martens, Heath Robinson, Kanybek Tashtankulov
#04/17/2022

FROM balenalib/raspberrypi3-64-debian-python:3.7-bookworm
ENV UDEV=1

RUN install_packages wget build-essential\
    python3-gi\
    bison libasound2-dev libsystemd-dev systemd swig\
    lirc lirc-compat-remotes\
    espeak

# Copy necessary config files
COPY /conf/config.txt /boot/
COPY /conf/py_reqs.txt /src/
COPY /conf/lirc_options.conf /etc/lirc
COPY /conf/Samsung_AA59-00382A.lircd.conf /etc/lirc/lircd.conf.d

# Run pip installatios
RUN pip install -r /src/py_reqs.txt --src /src

# Download and extract sphinx parts
RUN mkdir -p /src/sphinx
WORKDIR /src/sphinx
RUN wget -q https://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha/sphinxbase-5prealpha.tar.gz/download -O - \
    | tar -xz
RUN wget -q https://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha/pocketsphinx-5prealpha.tar.gz/download -O - \
    | tar -xz

# Compile and install sphinxbase
WORKDIR /src/sphinx/sphinxbase-5prealpha
RUN ./configure --enable-fixed \
    && make \
    && make install

# Compile and install pocketsphinx
WORKDIR /src/sphinx/pocketsphinx-5prealpha
RUN ./configure \
    && make \
    && make install

# Compile and install portaudio
WORKDIR /src
RUN wget -q http://files.portaudio.com/archives/pa_stable_v190700_20210406.tgz -O - \
   | tar -xz
WORKDIR /src/portaudio
RUN ./configure \
    && make \
    && make install

# Cleanup
WORKDIR /src
RUN rm -rf sphinx portaudio

# Move code into the container
COPY /src /src
# WORKDIR /src

# Needed so that sphinxbase and pocketsphinx can be recognized as installed
ENV PYTHONPATH /usr/local/lib/python3.7/site-packages

# Neeeded for lirc 
# RUN mkdir /var/run/lirc

# This can be replaced with just starting our app once it's working
# CMD ["lircd", "--device", "/dev/lircd", "&", "python3", "main.py"]
CMD lircd --driver=default --device=/dev/lirc0 && python3 main.py
