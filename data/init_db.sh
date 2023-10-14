#!/bin/bash

echo "Creating database: cookpad_data"
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "CREATE DATABASE IF NOT EXISTS cookpad_data CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

echo "Importing data into cookpad_data"
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" cookpad_data < /data/cookpad_data.sql
