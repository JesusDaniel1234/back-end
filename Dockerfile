FROM ubuntu:latest
LABEL authors="JDSA"

ENTRYPOINT ["top", "-b"]