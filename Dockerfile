FROM python:3.9.13-bullseye

RUN apt-get -y update && apt-get install -y libtiff-tools

WORKDIR /synapsegenie-htan-registry

RUN wget https://downloads.openmicroscopy.org/bio-formats/6.9.1/artifacts/bftools.zip
RUN unzip bftools.zip

COPY . .
RUN pip install .
