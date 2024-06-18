FROM python:3.10.12-alpine
# uses this for creating a isolated environment

WORKDIR /12-factor-app
# working dir in that environemt
COPY requirements.txt /12-factor-app/
# copying the requirements from our local directory to isolated directory
RUN pip install -r requirements.txt --no-cache-dir
# running the command to install the dependencies
COPY . /12-factor-app
# copying the current working directory content to the isolated directory
CMD python3 app.py
#to run the application