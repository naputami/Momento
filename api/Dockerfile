FROM python:3.8


WORKDIR /app


COPY . .


RUN pip install -r requirements.txt


EXPOSE 8000


CMD ["gunicorn", "run:app", "-b", "0.0.0.0:8000"]

