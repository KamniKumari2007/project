from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML Template
form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Resume Builder</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        input, textarea { width: 100%; padding: 10px; margin: 8px 0; }
        button { padding: 10px 20px; }
    </style>
</head>
<body>
    <h2>Resume Builder</h2>
    <form method="POST">
        <label>Name:</label>
        <input type="text" name="name" required>

        <label>Email:</label>
        <input type="text" name="email" required>

        <label>Phone:</label>
        <input type="text" name="phone" required>

        <label>Education:</label>
        <textarea name="education" required></textarea>

        <label>Skills:</label>
        <textarea name="skills" required></textarea>

        <label>Projects:</label>
        <textarea name="projects" required></textarea>

        <button type="submit">Generate Resume</button>
    </form>
</body>
</html>
"""

# Resume Output Template
resume_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Resume</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        h1 { text-transform: uppercase; }
        h2 { margin-top: 30px; }
    </style>
</head>
<body>

    <h1>{{ name }}</h1>
    <p>Email: {{ email }}</p>
    <p>Phone: {{ phone }}</p>

    <h2>Education</h2>
    <p>{{ education }}</p>

    <h2>Skills</h2>
    <p>{{ skills }}</p>

    <h2>Projects</h2>
    <p>{{ projects }}</p>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def resume_builder():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'education': request.form['education'],
            'skills': request.form['skills'],
            'projects': request.form['projects'],
        }
        return render_template_string(resume_template, **data)
    return render_template_string(form_template)

if __name__ == '__main__':
    app.run(debug=True)
