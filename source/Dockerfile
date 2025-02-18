#########################################################################################################################
# TODO: REPLACE THE CONTENT OF THIS FILE WITH YOUR OWN.
#########################################################################################################################

# Use the official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /chall

# Installing Flask
RUN pip install Flask

# Create the example chall (chall.py)
RUN echo "from flask import Flask\n\
chall = Flask(__name__)\n\
\n\
@chall.route('/')\n\
def hello():\n\
    return 'Hello @Hack 2025!'\n\
\n\
if __name__ == '__main__':\n\
    chall.run(host='0.0.0.0')" > chall.py

# Set environment vars
ENV FLASK_APP=chall.py
ENV FLASK_RUN_PORT=2025

# Expose the port that the chall will run on
EXPOSE 2025

# Run the chall
CMD ["flask", "run", "--host=0.0.0.0"]
