FROM python:3.10-slim

# Set correct timezone
ENV TZ=Etc/UTC

# Install tzdata (no time sync – Railway doesn't allow it)
RUN apt-get update && \
    apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Start the bot
CMD ["python3", "bot.py"]
