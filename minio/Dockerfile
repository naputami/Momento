FROM minio/minio:latest

RUN mkdir /data

EXPOSE 9000
EXPOSE 9001

CMD ["minio", "server", "/data", "--console-address", ":9001"]