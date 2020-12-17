# Python

Docstrings
```
"""Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value
"""
```
```
__doc__
```

Enter interactive mode after executing the script or the command
```
python -i file_name.py
```

Searches sys.path for the named module and runs the corresponding .py file as a script.
```
python -m module_name
```

Named arguments
```
**kwargs
```

Non-keyworded variable-length argument
```
*args
```

Type annotations
```
variable_name: str
```
```
def function() -> str:
```

Integer syntax
```
10_000
```

Float syntax
```
.5
```

Yes or no
```
input('Are you sure? (y/n): ').lower().strip()[:1]
```

Threading and queue
```
Class CThread(threading.Thread):

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

List comprehension
```
a = [i+10 for i in range(10)]
```

```
for index, value in range(10):
    a[index] = value + 10
```

Dictionaries comprehension
```
a = [i:i+10 for i in range(10)]
```

Generators
```
a = (i+10 for i in range(10))
```

```
def func(number):
    for i in range(number):
        yield i + 10

a = func(10)
print(a.__next__())
print(next(a))

for i in a:
    print(i)
```

Explicitly Define parameters in function
```
def function_name(parameter_name,*, parameter_name)
```

Recursive search with nesting
```
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

With
```
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

Exception
```
try:
    result = 5 / 0
except ZeroDivisionError as message:
    print(message.args)
else:
    print()
finally:
    print()
```

## Modules and packets

* **argparse** - parser for command-line options, arguments and sub-commands.
* **json** - JSON encoder and decoder.
* **logging** - logging facility for Python.
* **re** - regular expression operations.
* **csv** - CSV file reading and writing.
* **ldap3** - LDAP.
* **mysql.connector** - connecting to MySQL using Connector/Python.
* **requests** - elegant and simple HTTP library for Python, built for human beings.
* **configparser** - configuration file parser.
* **xml.etree.ElementTree** - implements a simple and efficient API for parsing and creating XML data.
* **platform** - access to underlying platform’s identifying data.
* **threading** - thread-based parallelism.
* **queue** - synchronized queue class.
* **mailbox** - manipulate mailboxes in various formats.
* **paramiko** - making SSH2 connections (client or server).
* **subprocess** - subprocess managemen.
* **multiprocessing** - process-based parallelism.
* **threading** - thread-based parallelism.
* **concurrent.futures** - launching parallel tasks.
* **asyncio** - asynchronous I/O.
* **netmiko** - multi-vendor library to simplify Paramiko SSH connections to network devices.
* **pprint** - data pretty printer.
* **bracket_expansion** - generator for bracket-expansion function.
* **jinja2** - jinja is a sandboxed template engine written in pure Python.
* **pyyaml** - the next generation YAML parser and emitter for Python.
* **ncclient** - library for NETCONF clients.
* **getpass** - portable password input.
* **dis** - python bytecode disassembler.
* **shutil** - provides many functions of high-level operations on files and collections of files.
* **os** - provides a portable way of using operating system dependent functionality.
* **os.path** - implements some useful functions on pathnames.
* **platform** - probe the underlying platform’s hardware, operating system, and interpreter version information.
* **lxml** - most feature-rich and easy-to-use library for processing XML and HTML in the Python language.
* **importlib** - implementation of import.
* **pyinstaller** - bundles a Python application and all its dependencies into a single package.

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

## Statements

* **nonlocal** - work with variables inside nested functions, where the variable should not belong to the inner function.
* **global** - is a declaration which holds for the entire current code block.
* **assert** - assert statements are a convenient way to insert debugging assertions into a program.

## LDAP

Import
```
from ldap3 import Server, Connection, SUBTREE, MODIFY_ADD, MODIFY_REPLACE, MODIFY_ADD, MODIFY_DELETE
```

Creating connection
```
server = Server("ip_address")
connection = Connection(server, user="user_name", password="user_password")
connection.bind()
connection.unbind()
```

Searching entries
```
connection.search('search_base',
                    'search_filter',
                    SUBTREE,
                    attributes=['attributes_to_returned'])
conn.entries[0].returned_attributes
```

Replaceing attribute value
```
dn = json.loads(connection.entries[0].entry_to_json())['dn']
connection.modify(dn, {'user_attribute': [(MODIFY_REPLACE, [new_value])]})
```

Adding attribute value
```
dn = json.loads(connection.entries[0].entry_to_json())['dn']
connection.modify(dn, {'user_attribute': [(MODIFY_ADD, [new_value])]})
```

Deleting attribute value
```
dn = json.loads(connection.entries[0].entry_to_json())['dn']
connection.modify(dn, {'user_attribute': [(MODIFY_DELETE, [delete_value])]})
```

## Logging

Import
```
import logging
```

Initialization logging format
```
logging.basicConfig(level=logging.logging_level, filename="path_to_log_file",
                      format='%(asctime)s %(process)d %(name)s %(levelname)s %(funcName)s %(message)s',
                      datefmt='%d-%b-%y %H:%M:%S')
```

Writing log
```
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
```
stream=std.stdout
```

## Command-line parser

Import
```
import argparse
```

Initialization
```
parser = argparse.ArgumentParser(description='', formatter_class=argparse.MetavarTypeHelpFormatter)
parser.add_argument('--example', dest='example', type=str, help='', default='')
parser.add_argument('--example2', dest='example2', type=bool, help='', action='store_true')
args = parser.parse_args()
```

Get argument
```
args.example
```

## CSV

Import
```
import csv
```

Read the file
```
with open('file_name', 'r') as csv_file:
csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        row['column_name']
```

Write to a file
```
with open('file_name', 'w', newline='', encoding='windows-1251) as csv_file:
    fieldnames = ['column_name']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'column_name': value})
```

## MySQL

Import
```
import mysql.connector
```

Creating connection
```
mysql_connection = mariadb.connect(user='mysql_user', password='mysql_password', database='mysql_database', host='mysql_ip')
cursor = mysql_connection.cursor()
cursor.close()
```
Executing sql-command
```
cursor.execute("sql_query")
rows = cursor.fetchall()
rows[0].['column_name']
```

## Configuration file

Import
```
import configparser
```

Initialization
```
config = configparser.ConfigParser()
```

Reading configuration file
```
config.read('configuration_file_name')
config.get('section_name', 'option_name', fallback=False)
```

Configuration file structure
```
[DEFAULT]
option_name = value

[section_name]
option_name = value
```

## XML

Import
```
xml.etree.ElementTree
```

Creating xml
```
root = ElementTree.Element('root_element')
sub_element = ElementTree.SubElement(root, 'sub_element')
sub_element.text = "sub_element_value"
ElementTree.dump(root)
```

Writing xml to file
```
tree = ElementTree.ElementTree(root)
tree.write('file_name', encoding="utf-8")
```

## Queue

Import
```
from queue import Queue
```

Initializing a queue
```
queue = Queue()
```

Adding of element to queue
```
queue.put('element')
```

Get and removing element from queue
```
queue.get()
```

Indicate that a formerly enqueued task is complete
```
queue.task_done()
```

Blocks until all items in the queue have been gotten and processed.
```
queue.join()
```

## Threading

Import
```
import threading
```

Creating a thread pool
```
for i in range(5):
    name = f'Thread {i}'
    thread = CThread(name)
    thread.daemon = True
    thread.start()
```

Threading class
```
Class CThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(self.name)
```

## Paramiko

Import
```
import paramiko
```

SSH key from string
```
ssh_key_object = io.StringIO(ssh_key)
ssh_rsa_key = paramiko.RSAKey.from_private_key(ssh_key_object, password_for_key)
```

SSH key from file
```
ssh_rsa_key = paramiko.RSAKey.from_private_key_file(path_to_key, password_for_key)
```

Creating connection
```
client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect(hostname='ip_address', port='port_number', username='user_name', password='user_password', pkey='key_file')
client.close()
```

Create SFTP session
```
sftp = client.open_sftp()
sftp.close()
```

Executing command
```
stdin, stdout, stderr = client.exec_command("command")
stdout.read().decode()
stderr.read().decode()
stdout.chennel.recv_exit_status()
```

Open key in UTF-8 BOM
```
with open(key_file, encoding='utf-8-sig') as key_object:
    ssh_rsa_key = paramiko.RSAKey.from_private_key(key_object, password_for_key)
```

## YAML

Import
```
import yaml
```

Read yaml file
```
with open('file_name') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
```

## Jinja2

Import
```
from jinja2 import Environment, FileSystemLoader
```

Create the environment
* trim_blocks - first newline after a block is removed.
* lstrip_blocks - leading spaces and tabs are stripped from the start of a line to a block.
```
ENV = Environment(loader=FileSystemLoader('.'), trim_blocks=True, lstrip_blocks=True)
ENV = Environment(loader=FileSystemLoader('.'))
```

Add filter
```
ENV.filters['function_name'] = function_name
```

Load a template from the loader
```
template = ENV.get_template("template_name")
```

Render the template
```
template.render(some_context=data)
```

## Requests

Import
```
import json
import requests
```

Headers
```
headers = {
        'Authorization': 'OAuth ',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
```

Params
```
params = {
        'fields': '',
    }
```

Body
```
data = {
        'fields': {'': ''}
    }
```

URL address
```
url = "https://site_name/"
```

HTTP get request
```
response = requests.get(url, headers=headers, params=params)
```

HTTP authorization
```
http_auth = requests.auth.HTTPBasicAuth('login', 'password')
response = requests.get(url, auth=http_auth)
```

HTTP post request
```
response = requests.post(url=url, headers=headers, params=params, data=json.dump(data))
```

Get response
```
response.json()
json.loads(response.text)
response.text
response.text.encode('utf8')
json.dumps(response.json(), indent=2)
json.loads(response.text)['antivirus_status']
```

Get status code
```
response.status_code
```

Get headers
```
response.headers
```

Get encoding
```
response.encoding
```

Upload file
```
file = open(path_to_file, 'rb')

response = request.post(url=url, headers=headers, params=params, data=data, files=file)
```

Download file
```
response = request.post(url = url, stream = True)
with open(path_to_file, 'wb') as file:
    file.write(response.content)
```
```
with open(path_to_file, 'wb') as file:
    for chunk in file.iter_content(chunk_size=128):
        file.write(chunk)
```

## Netmiko

Import
```
from netmiko import ConnectHandler
```

Creating connection
```
device = ConnectHandler(host='ip_address', username='user_name', password='user_password', device_type='linux', secret='')
```

Show device prompt
```
device.find_prompt()
```

Become root
```
device.enable(cmd='sudo -i', pattern='[sudo]')
```

Send command
```
device.send_command_expect()
device.send_command_timing()
device.send_command()
```

## OS

Import
```
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

## Class

* **hasattr()** - returns true if an object has the given named attribute and false if it does not.
* **setattr()** - sets the value of the attribute of an object.
* **getattr()** - returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.
* **delattr()** - deletes an attribute from the object.
* **super()** - return a proxy object that delegates method calls to a parent or sibling class of type.
* **__mro__** - This attribute is a tuple of classes that are considered when looking for base classes during method resolution.
* **mro()** - This method can be overridden by a metaclass to customize the method resolution order for its instances.

## Nexus

Import
```
import requests
```

Upload raw
```
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
```
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
```
import tarfile
```

Create tar arhive
```
tar_file = tarfile.open(path_to_arhive. mode='w')
tar_file.add(path_to_file, arcname=path_to_file_in_arhive)
tar_file.close()
```

Extract all files
```
tar_file = tarfile.open(path_to_arhive, mode='r')
tar_file.extractall(path=path_to_directory)
tar_file.close()
```

## GitLab CI

Import
```
import requests
import json
```

Create pipeline
```
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
```
'|{}:<30|'.format(variable)
```

Right aligned
```
'|{}:>30|'.format(variable)
```

Centered
```
'|{}:^30|'.format(variable)
```

Centered
```
'|{}:*^30|'.format(variable)
```

## File

* io.SEEK_SET - start of the stream
* io.SEEK_CUR - current stream position
* io.SEEK_END - end of the stream
* truncate(size=None)- resize the stream to the given size in bytes
* flush()- flush the write buffers of the stream if applicable
