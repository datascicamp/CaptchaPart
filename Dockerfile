# Source Image
FROM python:3.7
# Author
MAINTAINER Leon "leontian1024@gmail.com"
# Set working director
WORKDIR /var/app/webServerDir
# Add source code from os into container
Add . /var/app/webServerDir
# Add Linux font Tool
RUN apt-get update
RUN apt install fontconfig -y
# Import packages
RUN pip install Flask
RUN pip install Flask-wtf
RUN pip install flask_bootstrap
RUN pip install pillow
RUN pip install psycopg2-binary
RUN pip install python-dotenv
RUN pip install flask_sqlalchemy
RUN pip install flask_migrate
RUN pip install requests
# Expose port
EXPOSE 5000
# Run command
ENTRYPOINT ["python","./webServer.py"]

