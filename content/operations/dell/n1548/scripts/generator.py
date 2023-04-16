import sys
import yaml
import argparse
from jinja2 import Environment, FileSystemLoader, TemplateNotFound


def main():
    ENV = Environment(loader=FileSystemLoader('.'))
    
    try:
        template = ENV.get_template(args.template)
    except TemplateNotFound:
        print('No such template:', args.template)
        sys.exit(0)

    try:
        with open(args.data) as file:
            configuration = yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        print('No such file:', args.data)
        sys.exit(0)

    print(template.render(commutator=configuration))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='', formatter_class=argparse.MetavarTypeHelpFormatter)
    parser.add_argument('--template', type=str, help='template name', default='template.j2')
    parser.add_argument('--data', type=str, help='path to configuration file', default='data.yaml')
    args = parser.parse_args()
    sys.exit(main())
