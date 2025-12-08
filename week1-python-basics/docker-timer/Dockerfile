# Official lightweight Python image
FROM python:3.11-slim

# Copy your legendary timer into the container
COPY timer.py /app/timer.py

# Set working directory
WORKDIR /app

# Run your timer when container starts
ENTRYPOINT ["python", "timer.py"]
CMD ["90"]