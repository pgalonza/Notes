# Python

Docstrings

```text
"""Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
"""
```

```text
__doc__
```

Enter interactive mode after executing the script or the command

```bash
python -i file_name.py
```

Searches sys.path for the named module and runs the corresponding .py file as a script.

```bash
python -m module_name
```

Named arguments

```text
**kwargs
```

Non-keyworded variable-length argument

```text
*args
```

Type annotations

```text
variable_name: str
```

```python
def function() -> str:
```

Integer syntax

```text
10_000
```

Float syntax

```text
.5
```

Yes or no

```python
input('Are you sure? (y/n): ').lower().strip()[:1]
```

Explicitly Define parameters in function

```python
def function_name(parameter_name,*, parameter_name)
```

Recursive search with nesting

```python
def target_search(path, deep, *, depth = 0):
    target_dirs = list()

    if depth >= deep:
        return None

    depth += 1

    directories = os.listdir(path)

    if 'target_name' in directories:
        target_dirs.append(os.path.join(path, target_name))

    if not target_dirs:
        for directory in directories:
        next_path = os.path.join(path, directory)
    if os.path.isdir(next_path)
        result = target_search(next_path, deep, depth = depth)
    if result:
        target_dirs.extend(result)
```

Function attributes

```python
def func():
    func.x = 'x'
    func.y = 'y'

print(func.x)
```

PyLint generate configuration

```bash
python -m pylint --generate-rcfile > .pylintrc
```

Zero if value is negative

```python
max(0, <vvariable>)
```

Walrus

```python
if x := True:
    print(x)
```

F-string

```python
mode = dual
f"{mode=}"
```

Function with attribute

```python
def example():
    exammple.x = 1
    return x

example.x
```

Many conditions

```python
fullness = 100
distance = 200
health = 70

conditions = [
    fullness == 100,
    distance == 200,
    health < 80,
]

if all(conditions):
    pass

if any(conditions):
    pass
```

Merge dictionaries

```python
dict1 = {"healt": 100, "distance": 50}
dict2 = {"health": 80, "enemys": 4}
dict3 = {**dict1, **dict2}
```

Nested loops

```python
from itertools import chain

elements_list = [
    ['element1',],
    ['element1',],
    ['element1', 'element2',],
]

for element in chain.from_iterable(elements_list):
    print(element)
```

Multithreading or Multiprocessing

* I/O or Network usag - Multithreading
* GUI - Multithreading
* CPU - Multiprocessing(if multiple cores)

Mutable and Immutable data types

* List - mutable
* Dictionary - mutable
* Set - mutable
* Integer - immutable
* String - immutable
* Tuple - immutable
* Float - immutable
* Bool- immutable

TypedDict

```python
from typing import TypedDict

class SpaceShip(TypedDict, total=True):
    fullness: int
    health: int
    speed: int
    name: str
```

## Functions and methods

* **repr(object)** - return a string containing a printable representation of an object.
* **enumerate(iterable, start=0)** - return an enumerate object.
* **type(object)** - return the type of an object.
* **dir()** - without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.
* **help([object])** - invoke the built-in help system.
* **isinstance(object, classinfo)** - returns a Boolean stating whether the object is an instance or subclass of another object.
* **globals()** - return a dictionary representing the current global symbol table.
* **locals()** - return a dictionary representing the current local symbol table.
* **id()** - return the “identity” of an object.
* **del** - delete object.
* **zip()** - make an iterator that aggregates elements from each of the iterables.
* **random.shuffle()** - randomizes the items of a list in place.
* **random.choice()** - return a k sized list of elements chosen from the population with replacement.
* **platform.system()** - returns the system/OS name.
* **os.environ[]** - mapping object representing the string environment.
* **os.getenv()** - return the value of the environment variable varname if it exists, or value if it doesn’t.
* **os.putenv()** - set the environment variable named varname to the string value.
* **os.path.normpath()** - this string manipulation may change the meaning of a path that contains symbolic links. On Windows, it converts forward slashes to backward slashes.
* **os.path.join()** - join one or more path components intelligently.
* **os.path.abspath()** - return a normalized absolutized version of the pathname path.
* **io.StringIO()** - an in-memory stream for text I/O.
* **ord()** - returns an integer representing the Unicode character.
* **chr()** - returns the character that represents the specified unicode.
* **bytes()** - return a new "bytes" object, which is an immutable sequence of small integers in the range 0 <= x < 256, print as ASCII characters when displayed.
* **bin()** - convert an integer number to a binary string prefixed with “0b”.
* **hex()** - convert an integer number to a lowercase hexadecimal string prefixed with “0x”.
* **str.encode()** - return an encoded version of the string as a bytes object. Default
* **bytes.decode()** - return a string decoded from the given bytes.
* **map()** - function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
* **filter()** - method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
* **pickle** - python object serialization.
* **any** - return True if any element of the iterable is true. If the iterable is empty, return False.
* **sys.getrefcount(object)** - return the reference count of the object.
* **sys.getsizeof(object)** - return the size of an object in bytes.
* **eval()** - function runs the python code.
* **exec()** - method executes the dynamically created program.
* **compile()** - method returns a Python code object from the source.
* **os.sched_setaffinity()** - set the CPU affinity of the process identified by pid to mask.
* **functools.lru_cache()** - cache return values based on parameters.
* **functools.singledispatch()** - create function for work with different types.
* **functools.partial()** - return object which when called will behave like func.
* **functools.wraps()** - execute @functools.update_wrapper() as decorator.
* **functools.partial()** - allow us to fix a certain number of arguments of a function and generate a new function.
* **сollections.deque()** - Doubly Ended Queue.
* **сollections.namedtuple()** - named tuples.
* **сollections.Counter()** - count hashable objects.
* **collections.ChainMap()** - groups multiple dicts or other mappings together to create a single, updateable view.
* **collections.defaultdict()** - dict subclass that calls a factory function to supply missing values.
* **collections.OrderedDict()** - dict which saves the order of adding keys.

## Statements

* **nonlocal** - work with variables inside nested functions, where the variable should not belong to the inner function.
* **global** - is a declaration which holds for the entire current code block.
* **assert** - assert statements are a convenient way to insert debugging assertions into a program.

## LDAP

Import

```python
from ldap3 import Server, Connection, SUBTREE, MODIFY_ADD, MODIFY_REPLACE, MODIFY_ADD, MODIFY_DELETE
```

Creating connection

```python
server = Server("ip_address")
connection = Connection(server, user="user_name", password="user_password")
connection.bind()
connection.unbind()
```

Searching entries

```python
connection.search('search_base',
                    'search_filter',
                    SUBTREE,
                    attributes=['attributes_to_returned'])
conn.entries[0].returned_attributes
```

Replaceing attribute value

```python
dn = json.loads(connection.entries[0].entry_to_json())['dn']
connection.modify(dn, {'user_attribute': [(MODIFY_REPLACE, [new_value])]})
```

Adding attribute value

```python
dn = json.loads(connection.entries[0].entry_to_json())['dn']
connection.modify(dn, {'user_attribute': [(MODIFY_ADD, [new_value])]})
```

Deleting attribute value

```python
dn = json.loads(connection.entries[0].entry_to_json())['dn']
connection.modify(dn, {'user_attribute': [(MODIFY_DELETE, [delete_value])]})
```

## Logging

Import

```python
import logging
```

Initialization logging format

```python
logging.basicConfig(level=logging.logging_level, filename="path_to_log_file",
                      format='%(asctime)s %(process)d %(name)s %(levelname)s %(funcName)s %(message)s',
                      datefmt='%d-%b-%y %H:%M:%S')
```

Writing log

```python
logging.debug('')
logging.info('')
logging.critical('')
logging.error('')
logging.warning('')
logging.notset('')
```

Logging Levels

Level   |Numeric value
--------|-------------
CRITICAL|50
ERROR   |40
WARNING |30
INFO    |20
DEBUG   |10
NOTSET  |0

Print to stdout

```text
stream=std.stdout
```

Disable logging level

```python
logging.disable(logging.ERROR)
```

Logger configuration function

```python
def logging_configuration(logger):
    fh_formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s: %(process)d %(name)s %(funcName)s %(message)s',
                                     datefmt='%m-%d-%Y %H:%M:%S')
    fh = logging.FileHandler(filename='<log_name>.log', delay=True)
    fh.setLevel(level=logging.INFO)
    fh.setFormatter(fh_formatter)

    sh_formatter = logging.Formatter(fmt='%(asctime)s %(process)d %(name)s %(levelname)s %(funcName)s %(message)s',
                                     datefmt='%d-%b-%y %H:%M:%S')
    sh = logging.StreamHandler()
    sh.setLevel(level=logging.INFO)
    sh.setFormatter(sh_formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    logger.addHandler(sh)

loggger_interface = logging.getLogger('<logger_name>')
logging_configuration(loggger_interface)
```

## Command-line parser

Import

```python
import argparse
```

Initialization

```python
parser = argparse.ArgumentParser(description='', formatter_class=argparse.MetavarTypeHelpFormatter)
parser.add_argument('--example', dest='example', type=str, help='', default='')
parser.add_argument('--example2', dest='example2', type=bool, help='', action='store_true')
args = parser.parse_args()
```

Get argument

```text
args.example
```

## CSV

Import

```python
import csv
```

Read the file

```python
with open('file_name', 'r') as csv_file:
csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        row['column_name']
```

Write to a file

```python
with open('file_name', 'w', newline='', encoding='windows-1251) as csv_file:
    fieldnames = ['column_name']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'column_name': value})
```

## MySQL

Import

```python
import mysql.connector
```

Creating connection

```python
mysql_connection = mariadb.connect(user='mysql_user', password='mysql_password', database='mysql_database', host='mysql_ip')
cursor = mysql_connection.cursor()
cursor.close()
```

Executing sql-command

```python
cursor.execute("sql_query")
rows = cursor.fetchall()
rows[0].['column_name']
```

## Configuration file

Import

```python
import configparser
```

Initialization

```python
config = configparser.ConfigParser()
```

Reading configuration file

```python
config.read('configuration_file_name')
config.get('section_name', 'option_name', fallback=False)
```

Configuration file structure

```ini
[DEFAULT]
option_name = value

[section_name]
option_name = value
```

## XML

Import

```python
import xml.etree.ElementTree
```

Creating xml

```python
root = ElementTree.Element('root_element')
sub_element = ElementTree.SubElement(root, 'sub_element')
sub_element.text = "sub_element_value"
ElementTree.dump(root)
```

Writing xml to file

```python
tree = ElementTree.ElementTree(root)
tree.write('file_name', encoding="utf-8")
```

## Queue

Import

```python
from queue import Queue
```

Initializing a queue

```python
queue = Queue()
```

Adding of element to queue

```python
queue.put('element')
```

Get and removing element from queue

```python
queue.get()
```

Indicate that a formerly enqueued task is complete

```python
queue.task_done()
```

Blocks until all items in the queue have been gotten and processed.

```python
queue.join()
```

## Threading

Import

```python
import threading
```

Creating a thread pool

```python
for i in range(5):
    name = f'Thread {i}'
    thread = CThread(name)
    thread.daemon = True
    thread.start()
```

Threading class

```python
Class CThread(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(self.name)
```

Threading and queue

```python
class CThread(threading.Thread):

    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue

    def run(self):
        self.queue.get()
        print(self.name)
        self.queue.task_done()

queue = Queue()

for i in range(5):
    name = f 'Thread {i}'
    thread = CThread(name, queue)
    thread.daemon = True
    thread.start()

queue.put('element')
```

## Multiprocessing

Import

```python
import multiprocessing
```

Multiprocessing class

```python
Class CProcess(multiprocessing.Process):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(self.name)
```

## Paramiko

Import

```python
import paramiko
```

SSH key from string

```python
ssh_key_object = io.StringIO(ssh_key)
ssh_rsa_key = paramiko.RSAKey.from_private_key(ssh_key_object, password_for_key)
```

SSH key from file

```python
ssh_rsa_key = paramiko.RSAKey.from_private_key_file(path_to_key, password_for_key)
```

Creating connection

```python
client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect(hostname='ip_address', port='port_number', username='user_name', password='user_password', pkey='key_file')
client.close()
```

Create SFTP session

```python
sftp = client.open_sftp()
sftp.close()
```

Executing command

```python
stdin, stdout, stderr = client.exec_command("command")
stdout.read().decode()
stderr.read().decode()
stdout.chennel.recv_exit_status()
```

Open key in UTF-8 BOM

```python
with open(key_file, encoding='utf-8-sig') as key_object:
    ssh_rsa_key = paramiko.RSAKey.from_private_key(key_object, password_for_key)
```

Shell

```python
client.exec_command("command_line", shell=True)
client.exec_command(["command", 'args'], shell=False)
```

Run command as root or nologin

```python
stdin, stdout, stderr = client..exec_command("sudo -u root -s /bin/bash")
stdin.write('ls\n')
stdin.flush()
```

## YAML

Import

```python
import yaml
```

Read yaml file

```python
with open('file_name') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
```

```python
yaml.full_load(file)
```

## Jinja2

Import

```python
from jinja2 import Environment, FileSystemLoader
```

Create the environment

* trim_blocks - first newline after a block is removed.
* lstrip_blocks - leading spaces and tabs are stripped from the start of a line to a block.

```python
ENV = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
ENV = Environment(loader=FileSystemLoader('.'))
```

Add filter

```python
ENV.filters['function_name'] = function_name
```

Load a template from the loader

```python
template = ENV.get_template("template_name")
```

Render the template

```python
template.render(some_context=data)
```

## Requests

Import

```python
import json
import requests
```

Headers

```python
headers = {
        'Authorization': 'OAuth ',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
```

Params

```python
params = {
        'fields': '',
    }
```

Body

```python
data = {
        'fields': {'': ''}
    }
```

URL address

```python
url = "https://site_name/"
```

HTTP get request

```python
response = requests.get(url, headers=headers, params=params)
```

HTTP authorization

```python
http_auth = requests.auth.HTTPBasicAuth('login', 'password')
response = requests.get(url, auth=http_auth)
```

HTTP post request

```python
response = requests.post(url=url, headers=headers, params=params, data=json.dump(data))
```

Get response

```python
response.json()
json.loads(response.text)
response.text
response.text.encode('utf8')
json.dumps(response.json(), indent=2)
json.loads(response.text)['antivirus_status']
```

Get status code

```python
response.status_code
```

Get headers

```python
response.headers
```

Get encoding

```python
response.encoding
```

Upload file

```python
file = open(path_to_file, 'rb')

response = request.post(url=url, headers=headers, params=params, data=data, files=file)
```

Download file

```python
response = request.post(url = url, stream = True)
with open(path_to_file, 'wb') as file:
    file.write(response.content)
```

```python
with open(path_to_file, 'wb') as file:
    for chunk in file.iter_content(chunk_size=128):
        file.write(chunk)
```

## Netmiko

Import

```python
from netmiko import ConnectHandler
```

Creating connection

```python
device = ConnectHandler(host='ip_address', username='user_name', password='user_password', device_type='linux', secret='')
```

Show device prompt

```python
device.find_prompt()
```

Become root

```python
device.enable(cmd='sudo -i', pattern='[sudo]')
```

Send command

```python
device.send_command_expect()
device.send_command_timing()
device.send_command()
```

## OS

Import

```python
import os
```

### Path

Note

* posixpath for UNIX-style paths
* ntpath for Windows paths
* macpath for old-style MacOS paths
* os2emxpath for OS/2 EMX paths

### Sep

* **os.sep** -The character used by the operating system to separate pathname components.
* **os.altsep** - An alternative character used by the operating system to separate pathname components.
* **os.extsep** - The character which separates the base filename from the extension.
* **os.pathsep** - The character conventionally used by the operating system to separate search path components.
* **os.linesep** - The string used to separate (or, rather, terminate) lines on the current platform.
* **linesep** - The string used to separate (or, rather, terminate) lines on the current platform.

## Nexus

Import

```python
import requests
```

Upload raw

```python
url = 'http://nexus_address:8081/service/rest/v1/components'
http_auth = requests.auth.HTTPBasicAuth('login', 'password')

asset = open(path_to_file, 'rb')

params = {
    'repository': repository_name
}

payload = {
    'raw.asset1': asset
}

data = {
    'raw.directory': path_in_nexus,
    'raw.asset1.filename': file_name
}

response = request.post(url = url, auth = http_auth, params = params, data = data, files = payload)

asset.close()
```

Download row

```python
url = 'http://nexus_address:8081/service/rest/v1/search/assets'
http_auth = requests.auth.HTTPBasicAuth('login', 'password')

params = {
    'repository': repository_name
}

response = request.get(url = url, auth = http_auth, params = params)
asset_info = response['items']
asset_url = asset_info['downloadUrl']

asset_object = request.get(url = asset_url, auth = http_auth)

with open(path_to_file, 'wb') as file:
    file.write(asset_object.content)
```

## Tarfile

* tar = w, r
* tar.gzip = w:gz, r:gz

Import

```python
import tarfile
```

Create tar arhive

```python
tar_file = tarfile.open(path_to_arhive. mode='w')
tar_file.add(path_to_file, arcname=path_to_file_in_arhive)
tar_file.close()
```

Extract all files

```python
tar_file = tarfile.open(path_to_arhive, mode='r')
tar_file.extractall(path=path_to_directory)
tar_file.close()
```

## GitLab CI

Import

```python
import requests
import json
```

Create pipeline

```python
access_token = private_token

project_id = project id in GitLab

branch_name = branch name in project

variables = [{
    'key': variable_name,
    'value': variable_value,
}]

headers = {'PRIVATE-TOKEN': access_token, 'Content-Type': 'application/json'}

data = {'ref': branch_name, 'variables': variables}

url = f'https://gitlab_domain_name/api/v4/projects/{project_id}/pipeline'

response = requests.post(url=url, headers=headers, data=json.dumps(data), verify=False)

pipeline_info = response.json()

print(f'Pipeline running with parameters:\nURL: {pipeline_info["web_url"]}\nREF: {pipeline_info["ref"]}\nUSER: {pipeline_info["user"]["name"]}')
```

## Formatting

Left aligned

```python
'|{}:<30|'.format(variable)
```

Right aligned

```python
'|{}:>30|'.format(variable)
```

Centered

```python
'|{}:^30|'.format(variable)
```

Centered

```python
'|{}:*^30|'.format(variable)
```

## File

* io.SEEK_SET - start of the stream
* io.SEEK_CUR - current stream position
* io.SEEK_END - end of the stream
* truncate(size=None)- resize the stream to the given size in bytes
* flush()- flush the write buffers of the stream if applicable

In-memory binary stream

```python
file = io.BytesIO(<bytes>)
```

## Exception

Exception Handling

```python
try:
    result = 5 / 0
except ZeroDivisionError as message:
    print(message.args)
else:
    print()
finally:
    print()
```

Custom exception

```python
class ExampleError(Exception):

    def __init__(self, message, input_data=None):
        self.message = message
        self.input_data = input_data

    def __str__(self):
        return self.message
```

Raise an exception.

```python
raise ExampleError('example error')
```

Cheatsheet

```python
def get_exception_example():
    return ValueError

exception_example = ValueError

try:
    pass
except exception_example:
    raise CustomException() from None

try:
    pass
except get_exception_example() as exc:
    raise CustomException() from exc

try:
    pass
except :
    raise

try:
    pass
except Exception:
    raise SyntaxError()
```

## Functional programming

List comprehension

```python
a = [i+10 for i in range(10)]
```

```python
for index, value in range(10):
    a[index] = value + 10
```

Dictionaries comprehension

```python
a = [i:i+10 for i in range(10)]
```

Generators

```python
a = (i+10 for i in range(10))
```

```python
def func(number):
    for i in range(number):
        yield i + 10

        return / raise StopIteration()

a = func(10)
print(a.__next__())
print(next(a))

for i in a:
    print(i)
```

Iterators

```python
class Example:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        return self.i

        raise StopIteration()
```

lambda

```python
lambda x: x + 1
```

Create function

```python
class Multiplier:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x * self.n

object = Multiplier(n=2)
object(x=2)
```

High order functions

```python
def multiplier(y):
    def multiply_column(x):
        return y * x

    return multiply_column
```

Decorator

```python
def time_track(func):
    @wraps(func)
    def wrapper(*args, **kwds)
      started_at = time.time()

      result = func(*args, **kwargs)

      ended_at = time.time()
      elapsed = round(ended_at - started_at, 4)
      print(elapsed)
      return result
    return wrapper

def some_function()
    pass

time_track(some_function)

@time_track
def some_function_v2()
    pass
```

Decorator context manager

```python
from contextlib import contextmanager
import random


@contextmanager
def next_number(number):
    try:
        yield number + random.randint(0, 10)
    except Exception as exc:
        print(exc)


with next_number(1) as next_n:
    print(next_n)
```

## Date and time

Next day with ru locale

```python
current_date = datetime.datetime.now()
next_date = current_date + datetime.timedelta(days=1)
locale.setlocale(locale.LC_TIME, "ru_RU.utf8")
next_date.strftime('%a %d-%B')
```

## WebLogic Server

Import

```python
import requests
import json
```

HTTP Header

```python
http_header = {
    'Accept': 'application/json',
    'User-Agent': '<agent_name>',
    'X-Requested-By': '<agent_name>'
}
```

HTTP authorization

```python
auth = requests.ayth.HTTPBasicAuth(<user_name>, <user_password>)
```

Stop server

```python
url = http:<server_name>:8001/management/weblogic/latest/domainRuntime/serverLifeCycleRuntimes/<server_name>/forceShutdown
response = requests.post(url=url, headers=headers, auth=auth)
```

Start server

```python
url = http:<server_name>:8001/management/weblogic/latest/domainRuntime/serverLifeCycleRuntimes/<server_name>/start
response = requests.post(url=url, headers=headers, auth=auth)
```

Redeploy application

```python
application_files = {
    'model': (None, json.dumps(dict())),
    'sourcePath': open(<path_to_application>, 'rb'),
    'planPath': open(<path_to_xml>, 'rb')
}

url = http:<server_name>:8001/management/weblogic/latest/edit/appDeployments/<application_name>/redeploy
response = requests.post(url=url, headers=headers, auth=auth, files=application_files)
```

## Selenium

Import

```python
from selenium import webdriver
```

Set language

```python
profile = webdriver.FirefoxProfile()
profile.set_preference('intl.accept_languages', 'en-GB')
driver = webdriver.Firefox(firefox_profile=profile)
```

Open URL, search by string and press "Sign in"

```python
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("Python")
elem.submit()
elem1 = driver.find_element_by_link_text('Sign in')
elem1.click()
```

## WireGuard

Generate keys

```python
def generate_wireguard_keys():
    """
    Generate a WireGuard private, public key and preshared key
    Requires that the 'wg' command is available on PATH
    Returns (private_key, public_key, psk), both strings
    https://techoverflow.net/2021/05/16/how-to-generate-wireguard-key-private-public-in-python-without-dependencies/
    https://github.com/pbengert/wireguard-config-generator/blob/main/wireguard-config-generator.py
    """
    privkey = subprocess.check_output(
        "wg genkey", shell=True).decode("utf-8").strip()
    pubkey = subprocess.check_output(
        f"echo '{privkey}' | wg pubkey", shell=True).decode("utf-8").strip()
    psk = subprocess.check_output(
        "wg genkey", shell=True).decode("utf-8").strip()
    return (privkey, pubkey, psk)
```

## OpenCV

Image overlay

```python
x_offset = 0
y_offset = 0

image1 = cv2.imread('image_1.jpg')
image2 = cv2.imread('image_2.jpg')

height, width, _ = image2.shape

roi = self.image1[y_offset:height+y_offset, x_offset:width+x_offset]
img2gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(image2, image2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
image1[y_offset:height+y_offset, x_offset:width+x_offset] = dst
```

## OOP

context manager (with)

```python
class ClassName:

    def __enter__(self):
        print()
        return self

    def __exit__(self):
        print()
        return True # disable crash when exception

with ClassName(self, exc_type, exc_val, exc_tb) as class_name:
    print()
```

Getter and Setter

```python
class Person:
    def __init__(self, class_name, lvl):
        self._class_name = class_name
        self._lvl = lvl

    @classmethod
    def info(cls):
        print('info')

    @property
    def lvl(self):
        return self._lvl

    @property
    def class_name(self):
        return self._class_name

    @lvl.setter
    def lvl(self, lvl):
        self._lvl = lvl

    @class_name.setter
    def class_name(self, class_name):
        self._class_name = class_name


person = Person('druid', 80)
person.lvl = 70
print(person.lvl)
```

Abstract class and method

```python
from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def attack(self):
        """"""
```

Dataclass

```python
from dataclasses import dataclass

@dataclass(slots=False)
class Example:
    name: str
    email_id: str
    phone_number: str
    address: str
```

### Class

* **hasattr()** - returns true if an object has the given named attribute and false if it does not.
* **setattr()** - sets the value of the attribute of an object.
* **getattr()** - returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.
* **delattr()** - deletes an attribute from the object.
* **super()** - return a proxy object that delegates method calls to a parent or sibling class of type.
* **mro** - This attribute is a tuple of classes that are considered when looking for base classes during method resolution.
* **mro()** - This method can be overridden by a metaclass to customize the method resolution order for its instances.
* **repr()** - unction returns the object representation in string format.
* **str()** - method returns the string representation of the object.
* **\_\_slots\_\_** = set special attributes.

## Debugging

Profiler

```bash
python -m cProfile <python file>
```

Breakpoint

```python
import pdb
pdb.set_trace()
```

## Build package

Upgrade pip

```bash
pip install --upgrade pip
```

Create _pyproject.toml_

```toml
[build-system]
requires = ["setuptools>=60", "wheel"]
build-backend = "setuptools.build_meta"
```

Create _setup.py_

```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='<package name>',
    version='<package version>,
    description='',
    long_description='',
    long_description_content_type="text/markdown",
    author='<author name>',
    author_email='<author email>',
    maintainer='',
    maintainer_email='',
    url='<website url>',
    download_url='',
    packages=setuptools.find_packages(),
    py_modules=['<module name>',],
    classifiers= ['<describing>']
    license='Apache License 2.0',
    keywords=[],
    platforms='any',
    install_requires=[],
    python_requires='>=3.7',
    project_urls={},
)
```

Create README.md and LICENSE

Install build tools

```bash
pip install --upgrade build
pip install --upgrade wheel
pip install --upgrade setuptools
```

Build package

```bash
python -m build
```

Install twine

```bash
pip install --upgrade twine
```

Create _~/.pypirc_ for upload on gitlab

```text
[distutils]
index-servers =
    gitlab
 
[gitlab]
repository = https://<gitlab domain>/api/v4/projects/<project id>/packages/pypi
username = <token name>
password = <token>
```

Upload package

```bash
twine upload --repository gitlab dist/*
```

## Good practice

Do not add mutable default arguments to functions

```python
def example(x, y=None):
    if y is None:
        y = []
    x.append(x)
    return x
```

Private and Protected

```python

_variable_name = 'value'    # Protected
___variable_name = 'value'   # Private
```

## Emulation and Disassembling

Run code in emulation

```python
from unicorn import *
from unicorn.x86_const import *
from unicorn.arm_const import *
from unicorn.mips_const import *

CODE = b"\x41\x4a\x66\x0f\xef\xc1"

mu = Uc(UC_ARCH_X86, UC_MODE_32)
mu.mem_map(0, <size of memmory>)
mu.mem_write(0, CODE)

mu.emu_start(0, len(CODE))
```

Disassembling

```python
from capstone import *

CODE = b"\x41\x4a\x66\x0f\xef\xc1"

md = Cs(CS_ARCH_X86, CS_MODE_64)
for i in md.disasm(CODE, 0x1000):
    print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))

```
