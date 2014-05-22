## Flask-Graphing

Flask is a web framework for Python. This project is a starting point for a Flask + Bootstrap project that uses Matplotlib and Numpy to generate charts and graphs.

## Installation

- Install the `requirements.txt` file to your local virtualenv. (`pip install -r requirements.txt`)
- Install the node modules. (`npm install`)
- Install bower dependencies. (`bower install`)
- Fire up the `runserver.py` script. (`python runserver.py`)
- Visit [http://localhost:6500/](http://localhost:6500/).

## Development

A Gruntfile is included, it compiles assets in the `src/` directory, and drops them in the `core/static/` directory.

## File Structure

The `core/__init__.py` file contains the main routing logic for the app. The charting has been broken out into a submodule & Flask Blueprint (see `core/plot/views.py`), and mapped to the [http://localhost:6500/plotter/](http://localhost:6500/plotter/) endpoint. Templates go in the `core/templates/` directory.