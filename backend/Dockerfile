FROM python:3.8

WORKDIR /opt/backend


COPY backend/requirements.txt /opt/backend/

RUN pip3 install -r requirements.txt

COPY backend /opt/backend/



CMD ["python3", "main.py", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000