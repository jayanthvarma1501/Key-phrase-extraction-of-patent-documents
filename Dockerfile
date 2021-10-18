FROM continuumio/anaconda3:4.4.0
COPY . .
WORKDIR .
RUN pip install -r requirements.txt
CMD python main.py