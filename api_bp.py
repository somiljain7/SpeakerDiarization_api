from flask import Blueprint
from api_python import get_wav_file_main_extract
api_bp =Blueprint('api_bp',"forms")
api_bp.route('/getrttm',methods=['POST'])(get_wav_file_main_extract)
