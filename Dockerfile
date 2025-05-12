FROM python:3.9

RUN pip install pandas

WORKDIR /app
COPY scripts scripts

RUN cd scripts

#RUN python scripts/pipeline.py




ENTRYPOINT [ "python" , "scripts/pipeline.py" ]