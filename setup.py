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
        "pyswisseph>=2.10.3.0",
        "openai==1.3.7",
        "requests==2.31.0",
        "pydantic==2.5.0",
    ],
    python_requires=">=3.9",
) 