from IPython import embed
import requests
import re
import xml.etree.ElementTree as ET
import subprocess
import os


def main_extract(wav_file, json_xml):
    try:
        subprocess.run(["sh", "./sd_kaldi.sh", wav_file])
        rttm_path = (
            "/home/coder/Pictures/sd_demo/exp/displace_eval_fbank_diarization_vbhmm_spectral/per_file_rttm/"
            + wav_file.split("/")[-1].split(".")[0]
            + ".rttm"
        )
        print(rttm_path)
        if json_xml == "json":
            output = {}
            output["RTTM_PATH"] = rttm_path
            print(output)
            return output
        elif json_xml == "xml":
            data = ET.Element("root")
            s_elem1 = ET.SubElement(data, "rttm_path")
            s_elem1.text = rttm_path
            b_xml = ET.tostring(data)
            return b_xml
    except Exception as e:
        print(e)

