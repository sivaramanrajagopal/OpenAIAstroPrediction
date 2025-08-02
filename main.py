import sys
import os

# Change to the correct directory where the Python files are located
os.chdir(os.path.join(os.path.dirname(__file__), 'astro-backend', 'astro-backend'))

# Add the current directory to Python path
sys.path.insert(0, os.getcwd())

# Import and run the FastAPI app
from astro_backend_main import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
