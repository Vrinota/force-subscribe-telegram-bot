FROM python:3.10-slim

# Set correct timezone and sync time manually
ENV TZ=Etc/UTC

RUN apt-get update && \
    apt-get install -y tzdata ntpdate && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    ntpdate -u pool.ntp.org

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Start the bot
CMD ["python3", "bot.py"]
