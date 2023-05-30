FROM python:3
WORKDIR /usr/src/app
COPY . ./
RUN apt-get update
RUN pip install -r requirements.txt
CMD streamlit run main.py