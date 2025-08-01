from setuptools import setup, find_packages

setup(
    name="vedic-astrology-api",
    version="1.0.0",
    description="Vedic Astrology API with planetary calculations and AI-powered interpretations",
    packages=find_packages(),
    install_requires=[
        "python-dotenv==1.0.0",
        "fastapi==0.116.1",
        "uvicorn==0.27.1",
        "swisseph==0.0.0.dev1",
        "openai==0.28.1",
        "requests==2.31.0",
        "pydantic==2.5.0",
    ],
    python_requires=">=3.9",
) 