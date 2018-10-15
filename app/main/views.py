from flask import render_template
from . import main
@main.route('/')
def index():
    """View root function that returns index"""
    title =  'Home | welcome to pitches'
    return render_template('index.html', title = title)
@main.route('/pitch/new',methods=["GET","POST"])
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title = form.title.data, body = form.body.data)
        db.session.add(pitch)
        db.session.commit()
        flash('Nice pitching!')
        return redirect (url_for('main.new_pitch'))
    title = "Show us what you've got"
    pitches = Pitch.query.all()

    return render_template('pitch.html', title=title, form=form, pitch_list=pitches)

@main.route('/comment/new', methods = ["GET", "POST"])
@login_required
def new_comment():
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(comment=comment_form.comment.data)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted succesfully')
        return redirect(url_for('main.new_comment'))
    comments = Comment.query.all()
    return render_template('form.html', comment_form=comment_form, comment_list=comments)
