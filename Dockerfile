# Use the official MySQL image as the base
FROM mysql:8

# Copy the database initialization script
# This script will create the necessary database and handle the import of your data
COPY ./data/init_db.sh /docker-entrypoint-initdb.d/

# Make sure our script is executable
RUN chmod +x /docker-entrypoint-initdb.d/init_db.sh

# No need to specify CMD because we're using the base image's command
