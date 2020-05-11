from app import create_app,db
from app.models import User,Role,Post
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role, Post = Post )
if __name__ == '__main__':
    manager.run()