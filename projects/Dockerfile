# start from base
FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive 

MAINTAINER PIETER LEFFERS <https://github.com/pmleffers>


# 1. Define the packages required in our environment (i.e. Ubuntu). 
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  rm -rf /var/lib/apt/lists/*

USER root

RUN apt-get update
RUN apt-get install -y build-essential python3 python3-pip python3-dev wget curl git 
RUN pip3 install --upgrade pip

RUN mkdir /root/.keras src/
COPY . .

RUN pip3 install jupyter requests

WORKDIR /src/project_files

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

EXPOSE 8888
EXPOSE 8786

COPY requirements.py /src/project_files/
RUN python3 requirements.py
#CMD ["python3","module.py"]
#RUN rm /src/data/raw_data.csv
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]

##############################
####        USAGE         ####
##############################

# 1) docker build -t <new_project> .
# 2) docker run --rm -it -v ${PWD}/project_files:/src/project_files -p 8888:8888 <new_project>   


