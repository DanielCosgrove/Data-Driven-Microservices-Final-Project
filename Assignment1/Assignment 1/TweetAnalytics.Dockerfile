# Use an official Python runtime as a parent image 

FROM python:3-stretch 

ADD . /code 

# Set the working directory to /app 

WORKDIR /code 

# Copy the client code into the container at /app 

#COPY . /app 

# Install any needed packages specified in requirements.txt 

RUN pip install --trusted-host pypi.python.org -r requirements.txt 
RUN pip install redis -r requirements.txt

CMD ["python", "TweetAnalytics.py"] 
