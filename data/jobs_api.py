import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)



@blueprint.route("/api/jobs")
def get_jobs():
    db_sess = db_session.create_session()
    jobs_ = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(
                    only=("id", 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'))
                    for item in jobs_]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def find_id(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(only=("id", 'team_leader', 'job', 'work_size', 'collaborators',
                                       'start_date', 'end_date', 'is_finished'))
        }
    )

@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    elif request.json['id'] in [jobs.id for jobs in db_sess.query(Jobs).all()]:
        return jsonify(({'error': "Id already exists"}))
    job = Jobs(
        id = request.json['id'],
        job=request.json['job'],
        team_leader=request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date = request.json['start_date'],
        end_date=request.json['end_date'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})