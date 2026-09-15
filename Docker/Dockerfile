# 1. Start with an official, lightweight Linux image that already has Python 3.11 installed
FROM python:3.11-slim

# 2. Set the working folder inside the container where our app files will live
WORKDIR /app

# 3. Copy our requirements file from our local computer into the container
COPY requirements.txt .

# 4. Run the Linux command to install the Python libraries listed in that file
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our application code (app.py) into the container
COPY . .

# 6. Open port 5000 so web traffic can reach our app
EXPOSE 5000

# 7. The final command to execute whenever the container starts up
CMD ["python", "app.py"]