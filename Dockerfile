FROM python:3.10

COPY ./* python-ipmi/

RUN pip install requests beautifulsoup4 python-dotenv

CMD ["python", "./setup.py"] 
