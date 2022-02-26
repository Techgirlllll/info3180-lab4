from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask.helpers import send_from_directory
from werkzeug.utils import secure_filename


class UploadForm(FlaskForm):
    image = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg','png'])])