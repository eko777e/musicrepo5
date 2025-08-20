# Python 3.10 + Node.js 19 (Debian Bullseye bazalı)
FROM python:3.10-bullseye

# Sistem paketləri və Node.js 19 quraşdır
RUN apt-get update && apt-get install -y --no-install-recommends curl ffmpeg \
    && curl -fsSL https://deb.nodesource.com/setup_19.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# İş qovluğu
WORKDIR /app

# Layihəni konteynerə kopyala
COPY . /app/

# Python paketlərini yenilə və requirements.txt quraşdır
RUN python3 -m pip install --upgrade pip setuptools
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Botu işə sal
CMD ["python3", "-m", "VenomX"]
