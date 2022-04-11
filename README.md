## Garuda_PMS Development
### Getting Started
* Install the latest version of Python 3.9.x and `pip` as well
* Install the packages using `pip install -r requirements.txt`
* Install `mysql-server` in your dev machine.
	* Setup a credential for your mysql setup, and modify the `SQLALCHEMY_DATABASE_URI` variable in `config.py` accordingly
	* In mysql shell, create the db using `create database garuda_pms;`
	* Perform a `flask db upgrade` to import the necessary schematic into the mysql server
	* Finally, run the application using `flask run`