# Use a lightweight Python base image
FROM python:3.10-slim

WORKDIR /chall

ENV FLAG_KEY="f54fc577f6fb94c7175b74c4a5e42064"
ENV RUN_PORT=1337

# Copy challenge files into the container
COPY ./chall/dual_ec_prng_server.py .

# Install dependencies
RUN pip install --no-cache-dir pycryptodome

# Create a non-root user for security
RUN addgroup --system ctf && adduser --system --ingroup ctf ctf
USER ctf

# Expose the challenge port
EXPOSE 1337

# Set an environment variable for the flag key at runtime
CMD ["python3", "dual_ec_prng_server.py"]
