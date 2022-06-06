FROM python:3.8.2
RUN apt update -y && apt upgrade -y
CMD ["python3","-m", "ixelator"]
