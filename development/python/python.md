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
  name = f'Thread {i}'
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

## Functions and methods

* **repr(object)** - return a string containing a printable representation of an object.
* **enumerate(iterable, start=0)** - return an enumerate object.
* **type(object)** - return the type of an object.
* **super()** - return a proxy object that delegates method calls to a parent or sibling class of type.
* **dir()** - without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.
* **help([object])** - invoke the built-in help system.
* **isinstance(object, classinfo)** - returns a Boolean stating whether the object is an instance or subclass of another object.
* **globals()** - return a dictionary representing the current global symbol table.
* **locals()** - return a dictionary representing the current local symbol table.
* **id()** - return the “identity” of an object.
* **del** - delete object.
* **zip()** - join two tuples together.
* **random.shuffle()** - randomizes the items of a list in place.
* **random.choice()** - return a k sized list of elements chosen from the population with replacement.

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
