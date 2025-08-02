import subprocess
import sys
import os

# Activate the virtual environment and run the server
subprocess.run([
    '/opt/venv/bin/python', 
    '-m', 'uvicorn', 
    'astro_backend_main:app', 
    '--host', '0.0.0.0', 
    '--port', '8000'
], cwd='/app/astro-backend/astro-backend')
