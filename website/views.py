from flask import Blueprint, render_template, request, redirect, url_for
from .models import Project
from . import db

views = Blueprint('views', __name__)

@views.route('/list_project', methods=['GET', 'POST'])
def list_project():
    if request.method == 'POST':
         
        name = request.form.get('project_name')
        repo = request.form.get('repo_url')
        langs = request.form.get('languages')
        roles = request.form.get('roles_needed')
        desc = request.form.get('description')

        new_project = Project(
            project_name=name, 
            repo_url=repo, 
            languages=langs, 
            roles_needed=roles, 
            description=desc
        )

        db.session.add(new_project)
        db.session.commit()

        print(f"project {name} saved into database")

        return redirect(url_for('views.list_project'))
    
    return render_template("List_Your_Project.html")


@views.route('/project/<int:project_id>')
def project_page(project_id):

    project = Project.query.get_or_404(project_id)
    
    return render_template("Project_Page.html", project=project)