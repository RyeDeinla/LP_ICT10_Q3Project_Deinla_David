from pyscript import document

def sign_up(event):

    # Username Variable
    username = document.getElementById("username").value
   
    # Password Variable
    password = document.getElementById("password").value

    result = document.getElementById("result")

    # Eligibility of Input
    errors = []

    if len(username) < 7:
        errors.append("Username must contain at least 7 characters.")

    if len(password) < 10:
        errors.append("Password must be at least 10 characters long.")

    if not any(c.isalpha() for c in password):
        errors.append("Password must contain at least one letter.")

    if not any(c.isdigit() for c in password):
        errors.append("Password must contain at least one number.")

    if errors:
        result.innerHTML = "<br>".join(f"<p class='text-danger'>{e}</p>" for e in errors)
    else:
        result.innerHTML = "<p class='text-success'>Account created successfully!</p>"