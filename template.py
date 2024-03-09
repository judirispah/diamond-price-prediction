import os
from pathlib import Path
project="ML"


list_Of_files=[

    ".github/workflows/.gitkeep",
    "src/__init__.py",
    f"src/{project}/components/__init__.py",
    f"src/{project}/components/data_ingestion.py",
    f"src/{project}/components/data_tranformation.py",
    f"src/{project}/components/model_trainer.py",
    f"src/{project}/components/model_evaluation.py",

    f"src/{project}/pipline/__init__.py",
    f"src/{project}/pipline/training_pipline.py",
    f"src/{project}/pipline/prediction_pipline.py",

    f"src/{project}/pipline/__init__.py",
    f"src/{project}/utils/__init__.py",
    f"src/{project}/pipline/common_utils.py",

    f"src/{project}/logger/__init__.py",
    f"src/{project}/exception/__init__.py",


    "tests/unit/__init__.py",
    "tests/integration/__init__.py",

    "setup.py",
    "requirements.txt",
    "requirements_dev.txt",
    "pyproject.toml",
    
    

]

for filepath in list_Of_files:
    filepath=Path(filepath)# find info about type of os
    filedir,filename=os.path.split(filepath)#seperate folder and file

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)#create folder

    if (not os.path.exists(filepath)) or(os.path.getsize(filepath)) :
        with open(filepath,"w") as f: #create file inside folder
            pass 
    else:
        print(f"{filepath} already exists")     