# Use original image of python 3.10
FROM python:3.10

# Set folder code as work directory
WORKDIR /code

# Copying files
COPY pyproject.toml poetry.lock .env /code/

# Install poetry
RUN pip install poetry
# Install all dependencies
RUN poetry install

# Copy app files to work direcrort
COPY ./app /code

