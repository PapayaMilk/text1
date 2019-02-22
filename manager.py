import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

my_app = app.create_app()
manager = Manager(my_app)


if __name__ == '__main__':
    manager.run()
