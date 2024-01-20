#!/bin/bash

# Specify the folder path
folder_path="Data"

# Delete contents of the folder
rm -rf "$folder_path"/*

# Check if deletion was successful
if [ $? -eq 0 ]; then
    echo "Folder contents deleted successfully."
    
    # URL to make a call to
    api_url="http://m3u4u.com/m3u/69wkng3qdghvgjrpnq8g"

    # Make a call to the URL using curl
    curl  "$api_url" > "Data/playlist.m3u"

    # Check if the curl command was successful
    if [ $? -eq 0 ]; then
        echo "[---------API call successful---------]"
	echo "[-------Activating Python Env---------]"
	source "./Ingest/env/Scripts/activate"
	echo "[--------Processing m3u file----------]"
	python ./Ingest/main.py
	if [ $? -eq 0 ]; then
		echo "[---------Python Script Exec----------]"
	else 
		echo "[------------Python Failed------------]"
	fi
	deactivate 
    else
        echo "Error: API call failed."
    fi
	
else
    echo "Error: Failed to delete folder contents."
fi
