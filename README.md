# My First Repo!

Learning and practicing version control!

## Setup

Clone the repo to download it from Github.

Navigate to the repo using the command line.

```sh
cd ~/Documents/first_OPAN_3244_repo
```

Create a virtual environment:

```sh
conda create -n my-first-env-fall-2025 python=3.11
```

Activate the virtual environment:

```sh
conda activate my-first-env-fall-2025
```

Install package dependencies:

```sh
pip install -r requirements.txt
```



## Usage

Example script:

```sh
python app/my_script.py
```

Game of rock, paper, scissors:

```sh
python app/rps.py

# alternative "modular style" command:
python -m app.rps
```


Stocks dashboard:

```sh
python -m app.stocks
```

## Testing

Run tests:
```sh
pytest
```