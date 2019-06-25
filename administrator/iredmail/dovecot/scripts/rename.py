#! /usr/bin/env python3
import sys
import os
import logging
import argparse
import csv
import shutil
import subprocess


def main():
    path = f'/var/vmail/vmail1/{args.domain}/'
    try:
        with open(args.file) as csv_file:
            logging.debug(f'Read file: {args.file}')
            user_reader = csv.DictReader(csv_file)
            for row in user_reader:
                logging.debug(f'E-mail from file {row}')
                new_email = row['new_email'].replace('@' + args.domain, "")
                old_email = row['old_email'].replace('@' + args.domain, "")
                logging.debug(f'\n{old_email}\n{new_email}\n{path}')
                try:
                    os.rename(path + old_email, path + new_email)
                except OSError:
                    logging.debug(f'Directory not empty {new_email}')
                    try:
                        subprocess.check_output(['cp', '-rf', path + old_email + '/Maildir', path + new_email])
                    except subprocess.CalledProcessError:
                        logging.debug(f'Directory not found {old_email}')
                        continue
                    try:
                        subprocess.check_output(['mv', path + old_email, '/var/vmail/vmail1/delete'])
                    except subprocess.CalledProcessError:
                        logging.debug(f'Directory not empty /var/vmail/vmail1/delete/{old_email}')





                '''
                try:
                    shutil.rmtree(path + old_email)
                except FileNotFoundError:
                    continue
                '''


    except FileNotFoundError:
        logging.info(f'Cannot open the file: {args.file}')
        sys.exit(0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(process)d %(name)s %(levelname)s %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')

    parser = argparse.ArgumentParser(description='Rename e-mail', formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument('--file', type=str, help='file with new and old e-mail')
    parser.add_argument('--domain', type=str, help='e-mail domain')

    args = parser.parse_args()

    sys.exit(main())
