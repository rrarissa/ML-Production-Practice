# ML-Production-Practice
The purpose of the project is to transform a ML predictive project from jupyternotebook environment to productioon environment. We focus on model implementation, CI/CD and microservices. 

# Code Architecture 
```
├── Makefile                # Build and management commands
├── poetry.lock             # Dependency lock file
├── pyproject.toml          # Project configuration file
└── src/                    # Source code directory
    ├── config/             # Configuration files
    │   └── config.py       # Configuration settings
    ├── logs/               # Logs directory
    ├── model/              # Core model logic
    │   ├── model_service.py   # Model service script
    │   ├── models/         # Pre-trained or saved models
    │   │   └── rf_v1       # Random Forest model version 1
    │   └── pipelines/      # Data pipelines for the model
    │       ├── collection.py # Data collection pipeline
    │       ├── model.py      # Model training and evaluation pipeline
    │       └── preparation.py# Data preprocessing pipeline
    ├── rent_apartments.csv   # Sample dataset
    └── runner.py             # Main entry point for running the application
```

# Library  
## Poetry 
Our project uses poetry to specify and manage dependencies.  In Poetry, adding, removing, or updating dependencies is streamlined with simple commands (poetry add, poetry remove, etc.), and the pyproject.toml file is updated automatically. For a complex project, poetry can ensure identical environments across different systems.


## Pydantic 
parameterization, instead of hard coding the model and path, we use configuration file 

## Loguru
Loguru is a third-party logging library for Python that simplifies logging.
It has functions of debug, info, warning, error and critical. 

## Flake8 
Flake8 is a Python linting tool that checks code for compliance with style and quality standards
## Makefile
A Makefile is a special file used by the make build automation tool to define a set of tasks that can be executed to automate repetitive processes such as compiling code, building executables, or managing dependencie.

# GitHub Actions CI/CD


# wemake-services
