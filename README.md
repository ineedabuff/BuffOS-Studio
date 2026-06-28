# BuffOS Studio

## Install

    git clone https://github.com/ineedabuff/BuffOS-Studio.git
    cd BuffOS-Studio
    ./install.sh

## Use

    source .venv/bin/activate
    PYTHONPATH=installer python -m app.cli.main doctor
    PYTHONPATH=installer python -m app.cli.main setup
    PYTHONPATH=installer python -m app.cli.main wizard
