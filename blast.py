import argparse
import os
import subprocess

def parse_args():
    parser = argparse.ArgumentParser(description='Blast the usb sticks with the site and boxes')
    parser.add_argument('--boxes-path', help='The path to the boxes.', required=True)
    parser.add_argument('--site-path', help='The path to the built selinux site', required=True)
    parser.add_argument('--usb-path', help='The path to the usb directory', required=True)
    return parser.parse_args()


def blast_usb(args):
    for item in os.listdir(path=args.usb_path):
        boxes_drive = os.path.abspath(os.path.join(args.usb_path, item))
        if args.boxes_path.startswith(boxes_drive):
            continue

        rsync_site_string = "rsync -avzh {site} {boxes_drive}{os_sep}selinuxgame.org".format(
            site=os.path.abspath(args.site_path) + os.sep,
            boxes_drive=boxes_drive,
            os_sep=os.sep
        )
        subprocess.run(rsync_site_string, shell=True, check=True)

        rsync_boxes_string = "rsync -avzh {boxes_path} {boxes_drive}{os_sep}vagrant".format(
            boxes_path=args.boxes_path,
            boxes_drive=boxes_drive,
            os_sep=os.sep
        )
        subprocess.run(rsync_boxes_string, shell=True, check=True)


def main():
    args = parse_args()
    blast_usb(args)


if __name__ == "__main__":
    main()
