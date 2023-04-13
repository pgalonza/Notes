import sys
import jwt
from pprint import pprint


def main():
    token = input("Token: ")
    jwt_structure = jwt.decode(token, algorithms=["RS256"], options={"verify_signature": False})
    pprint(jwt_structure)


if __name__ == "__main__":
    sys.exit(main())