#### SPEAKER DIARIZATION
- GOAL: to create an API endpoint, which returns RTTM FILE while taking path of audio file 

- 	POST URL:		http://127.0.0.1:5000/api/v1/getrttm

- File Structure:
	1. 		flask-api.py --> MAIN FLASK FILE
	2. 		api_bp.py --> blueprint for routing and etc
	3. 		api_python.py --> script for dealing with request json 
	4.		get_wav_file_details.py --> calling of api endpoints

- By - SOMIL JAIN
