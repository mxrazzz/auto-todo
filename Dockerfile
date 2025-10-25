# 🐳 Dockerfile - The Recipe for Building Your App Container
# Think of this as instructions for making a birthday cake, but for your app!

# ============================================
# STAGE 1: THE BASE (like choosing what pan to use)
# ============================================
# FROM = "Start with this as our foundation"
# We're using Python 3.11 on a slim (lightweight) Linux system
# "alpine" is even smaller, but "slim" is easier for beginners
FROM python:3.11-slim

# 🏷️ LABELS = Stickers on the container that tell you about it
LABEL maintainer="mxrazzz"
LABEL description="A simple to-do list CLI application"
LABEL version="1.0.0"

# 📁 WORKDIR = "Make a folder and work inside it"
# This is like setting up your workspace on a desk
# All future commands will run from this folder
WORKDIR /app

# ⚡ OPTIMIZATION: Install dependencies FIRST (before copying code)
# Why? Docker caches each step. If your code changes but requirements.txt doesn't,
# Docker reuses the cached layer = MUCH faster builds!

# 📋 Copy ONLY requirements.txt first
COPY requirements.txt .

# 🔧 RUN = "Execute this command while building the image"
# --no-cache-dir = Don't save pip's download cache (saves space)
# --upgrade pip = Get the latest pip version
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 📦 Copy the rest of your application code
# The "." means "copy everything from current folder"
# The second "." means "paste it in /app (our WORKDIR)"
COPY . .

# 👤 SECURITY: Don't run as root user
# Create a non-root user called 'appuser' and switch to it
# This is like not using an admin account for everyday tasks
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

# 🎯 CMD = "When someone runs this container, execute this command"
# This is the DEFAULT command (can be overridden)
# We use ["python", "main.py"] instead of "python main.py" for better signal handling
CMD ["python", "main.py"]

# 🔍 WHAT HAPPENS WHEN YOU BUILD THIS?
# 1. Downloads Python 3.11 slim image
# 2. Creates /app folder
# 3. Copies requirements.txt
# 4. Installs all Python packages
# 5. Copies your code (main.py, test_main.py, etc.)
# 6. Creates a non-root user
# 7. Sets default command to run your app

# 📦 Final image size: ~150-200 MB (instead of 1+ GB with full Python image!)
