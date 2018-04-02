from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length


class Sample_Details_Form(FlaskForm):
    species = StringField(('Species'), validators=[DataRequired()])
    tissue_types = StringField(('Tissue Type(s)'), validators=[DataRequired()])
    wet_samples = StringField(('Number of Wet Samples Submitted'))
    cassettes = StringField(('Number of Wet Cassettes Submitted'))
    paraffin_blocks = StringField(('Number of Paraffin Blocks Submitted'))
    fixative_used = StringField(('Fixative Used'), validators=[DataRequired()])
    time_in_fixative = StringField(('Length of time in fixation'))
    current_storage = StringField(('Solution samples currently stored in'), validators=[DataRequired()])
    time_in_current_storage = StringField(('Length of time in current storage solution'))

class Histology_Details_Form(FlaskForm):
    decal = BooleanField(('Do samples require decalcification?'), validators=[DataRequired()])
    orientation = TextAreaField(('Please describe sample orientation (cross-section, longitudinal, saggital, coronal, etc)'))
    slide_per_sample = IntegerField(('Number of H&E slides per sample'), validators=[DataRequired()]))
    sections_per_slide = IntegerField(('Number of sections per sample'))
    section_thickness = IntegerField(('Section Thickness (5 microns is recommended)'))
    number_of_H_E = IntegerField(('How many sections per slide?'))
    special_stain_name = StringField(('Special Stain requested'))
    number_of_specials = IntegerField(('Number of special stains per sample'))
    turn_around_time = IntegerField(('Turn around time request (1,2,3 or 10 days)'))
    slide_scanning = BooleanField(('Slide scanning requested?'))
    submit = SubmitField(('Place Order'))
