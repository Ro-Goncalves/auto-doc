import streamlit.web.cli as stcli
import sys, os
from dotenv import load_dotenv


def main():
    load_dotenv()   
    sys.argv = ["streamlit", "run", "auto_doc/auto_doc_app.py"]    
    stcli.main()

if __name__ == "__main__":
    main()