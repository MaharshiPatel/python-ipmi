FROM python:3.12.6

COPY ./* python-ipmi/

RUN pip install requests beautifulsoup4 python-dotenv

CMD ["python", "./setup.py"] 
