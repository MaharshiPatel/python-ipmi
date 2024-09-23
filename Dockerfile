FROM alpine:3.18.6
FROM python:3.6

RUN pip install requests beautifulsoup4 python-dotenv

CMD ["python", "./setup.py"] 
