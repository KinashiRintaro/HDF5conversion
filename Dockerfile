FROM python:3.9
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get -y update              ; \
    apt-get -y install curl        ; \
    apt-get -y install wget        ; \
    apt-get -y install git         ; \
    apt-get -y install vim         ; \
    apt-get -y install hdf5-tools

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install numpy,             ; \
    install pytz                   ; \
    pip install awscli             ; \
    pip install numcodecs          ; \
    pip install h5py               ; \
    pip install pandas             ; \
    pip install pillow             ; \
    pip install h5netcdf           ; \
    pip install xarray             ; \
    pip install git+https://git@github.com/HDFGroup/h5pyd