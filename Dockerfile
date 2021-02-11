FROM python:3.9-slim-buster

WORKDIR /usr/src/app

RUN pip install --upgrade pip

RUN pip3 install gspread
RUN pip3 install --upgrade oauth2client
RUN pip3 install PyOpenSSL
RUN pip3 install pandas
RUN pip3 install openpyxl
RUN pip3 install email-to

COPY . .

CMD python main.py