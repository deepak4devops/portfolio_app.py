from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# HTML Templates inside Python (for simplicity)
index_html = """
<!DOCTYPE html>
<html>
<head>
    <title>My Portfolio</title>
    <style>
        body { font-family: Arial; padding: 40px; background: #f0f0f0; }
        h1, h2 { color: #2c3e50; }
        a { text-decoration: none; color: #2980b9; }
    </style>
</head>
<body>
    <h1>Hello, I'm [Your Name]</h1>
    <p>Welcome to my portfolio website built using Flask.</p>

    <h2>About Me</h2>
    <p>I’m a developer skilled in Python, Flask, and web development.</p>

    <h2>Projects</h2>
    <ul>
        <li>Project 1 - Description</li>
        <li>Project 2 - Description</li>
    </ul>

    <a href="{{ url_for('contact') }}">Contact Me</a>
</body>
</html>
"""

contact_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Contact</title>
    <style>
        body { font-family: Arial; padding: 40px; background: #f9f9f9; }
        form { width: 300px; }
        input, textarea { width: 100%; padding: 10px; margin-bottom: 10px; }
        button { padding: 10px 20px; background-color: #3498db; color: white; border: none; }
    </style>
</head>
<body>
    <h1>Contact Me</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Your Name" required><br>
        <input type="email" name="email" placeholder="Your Email" required><br>
        <textarea name="message" placeholder="Your Message" required></textarea><br>
        <button type="submit">Send</button>
    </form>
</body>
</html>
"""

thank_you_html = """
<!DOCTYPE html>
<html>
<head><title>Thanks</title></head>
<body>
    <h2>Thank you for your message!</h2>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(index_html)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Simulate handling the message
        print(f"[CONTACT] From: {name}, Email: {email}, Message: {message}")

        return redirect(url_for('thank_you'))

    return render_template_string(contact_html)

@app.route('/thank-you')
def thank_you():
    return render_template_string(thank_you_html)

if __name__ == '__main__':
    app.run(debug=True)
