FROM alpine:3.8
RUN addgroup local && \
    adduser -D -G local local
RUN apk add --no-cache python3
USER local
COPY roll.py /tmp/
ENTRYPOINT ["python3", "/tmp/roll.py"]
CMD ["--help"]
