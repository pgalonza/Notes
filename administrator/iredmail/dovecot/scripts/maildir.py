#! /usr/bin/env python3.6
import argparse
import mailbox
import sys
import os
import re
import threading
import logging
from queue import Queue
from email.header import decode_header

_mails = []


class Mail(threading.Thread):

    def __init__(self, queue, name):
        logging.debug('The class initialization')
        threading.Thread.__init__(self)
        self.queue = queue
        self.name = name

    def run(self):
        while True:
            task = self.queue.get()
            logging.debug(f'{self.name} get the task and start: {task}')
            self.read_mail(task)
            logging.debug(f'{self.name} task is completed')
            self.queue.task_done()

    @staticmethod
    def read_mail(user):
        try:
            logging.info(f'Open the maildir {user}')
            mail_box = mailbox.Maildir(f'{user}/Maildir/')
            logging.info(f'Read {len(mail_box)} mails')
            for key, message in mail_box.iteritems():
                logging.debug(f'Check null subject in {key}')
                if message['subject']:
                    logging.debug(f"Decode the title: {message['subject']}")
                    title, charset = decode_header(message['subject'])[0]
                    logging.debug(f"Check null charset in : {charset} {title}")
                    if not charset:
                        logging.debug(f"Check bytes type in : {title}")
                        if bytes == type(title):
                            logging.debug("Decode the bytes")
                            title = title.decode()
                            logging.debug(f"Search the string {args.title} in {title}")
                            if args.title in title:
                                print('Found: ', user, title)
                                logging.info(f"The letter was found!\n User: {user}\nTitle: {title}")
                                _mails.append([key, user, title.decode(charset), mail_box])
                        else:
                            logging.debug(f"Search the string {args.title} in {title}")
                            if args.title in title:
                                print('Found: ', user, title)
                                logging.info(f"The letter was found!\n User: {user}\nTitle: {title}")
                                _mails.append([key, user, title, mail_box])
                    else:
                        try:
                            logging.debug(f"Decode the: {charset}")
                            title = title.decode(charset)
                            logging.debug(f"Search the string {args.title} in {title}")
                            if args.title in title:
                                print('Found: ', user, title)
                                logging.info(f"The letter was found!\n User: {user}\nTitle: {title}")
                                _mails.append([key, user, title, mail_box])
                            pass
                        except UnicodeDecodeError:
                            print(f"Can`t decode masseage: {title} with charset: {charset}")
                            logging.info(f"Can`t decode masseage: {title} with charset: {charset}")
        except FileNotFoundError:
            print(f"The mail box was empty: {user}")
            logging.info(f"The mail box was empty: {user}")


def main():
    logging.debug('Create the queue')
    queue = Queue()

    logging.debug(f'Start the thread(s): {args.thread}')
    for i in range(args.thread):
        name = f'Thread {i}'
        thread = Mail(queue, name)
        thread.daemon = True
        logging.debug(f'Start: {name}')
        thread.start()

    if args.emails:
        for email in args.emails:
            logging.info(f'Parse the e-mail: {email}')
            result = re.search(r'^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$', email)
            logging.info(f'\nUser: {result.group(1)}\nDomain: {result.group(2)}')
            path = f'{args.path}/{result.group(2)}/{result.group(1)}'
            logging.info(f'Add the path to queue: {path}')
            queue.put(path)
    elif args.domains:
        for domain in args.domains:
            logging.info(f'List the users directory of {domain}')
            users = os.listdir(domain)
            logging.info('Filter the directorys')
            users = list(filter(lambda x: not re.search(r'\.tar\.gz', x), users))
            for user in users:
                path = f'{args.path}/{domain}/{user}'
                logging.debug(f'Add the path to queue: {path}')
                queue.put(path)
    else:
        logging.info('List the domains directory')
        domains = os.listdir(args.path)
        logging.info('Filter the directorys')
        domains = list(filter(lambda x: re.search(r'\.local', x), domains))

        for domain in domains:
            logging.info(f'List the users directory of {domain}')
            users = os.listdir(f'{args.path}/{domain}')
            logging.info('Filter the directorys')
            users = list(filter(lambda x: not re.search(r'\.tar\.gz', x), users))
            for user in users:
                path = f'{args.path}/{domain}/{user}'
                logging.debug(f'Add the path to queue: {path}')
                queue.put(path)

    logging.debug('Freeze the general thread and wait child threads')
    queue.join()
    logging.debug('Unfreeze the general thread and show mails to delete')
    if _mails:
        print("Delete mails?")
        for mail in _mails:
            logging.debug(f'Path: {mail[1]}\nTitle: {mail[2]}')
            print('>>>', mail[1], mail[2])
        logging.info('Whait the choice')
        choice = input('Are you sure? (y/n): ').lower().strip()[:1]
        logging.debug(f'The choice is {choice}')
        if choice == "n":
            logging.info('Exit')
            sys.exit(1)
        elif choice == 'y':
            logging.info('Delete the mails')
            for mail in _mails:
                mail[3].remove(mail[0])
                logging.info(f'Delete: {mail[1]} {mail[2]} OK!')
            print('Successfully!')
    else:
        print(f'The emails with {args.title} not found')
        logging.info(f'The emails with {args.title} not found')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search mail for remove', formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--path', type=str, help='Path to vmail directory', default='/var/vmail/vmail1')
    parser.add_argument('--thread', type=int, help='Number of threads', default=1)
    parser.add_argument('--title', type=str, help='Search by title', required=True)
    parser.add_argument('--emails', type=str, help='Users', nargs='*', default=False)
    parser.add_argument('--domains', type=str, help='Domains', nargs='*', default=False)
    parser.add_argument('--log', type=str, help='Path to log file', default='/var/log/scripts')
    parser.add_argument('--debug', type=str, help='Debug level', default='info', choices=('info', 'debug'))

    args = parser.parse_args()

    debug_match = {'info': logging.INFO, 'debug': logging.DEBUG}
    logging.basicConfig(level=debug_match.get(args.debug), filename=f"{args.log}/maildir-remover.log",
                        format='%(asctime)s %(process)d %(name)s %(levelname)s %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    sys.exit(main())
