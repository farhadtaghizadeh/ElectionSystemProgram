from flask import redirect, request, flash, url_for, render_template
from flask_login import confirm_login

def relogin():
    if request.method == "POST":
        confirm_login()
        flash(u"Revalidation Successful")
        return redirect(request.args.get("next") or url_for("app_home"))
    return render_template("login.html")
