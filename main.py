import sys
import os

# Add the astro-backend/astro-backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'astro-backend', 'astro-backend'))

# Import and run the FastAPI app
from main import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
