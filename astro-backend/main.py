
import subprocess
import sys
import os

# Change to the astro-backend directory and run the FastAPI server
os.chdir('astro-backend')
subprocess.run([sys.executable, '-m', 'uvicorn', 'main:app', '--host', '0.0.0.0', '--port', '8000', '--reload'])
