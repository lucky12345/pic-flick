from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

@app.route("/")
def home():
	return redirect(url_for('login'))
	
@app.route("/signup", methods=["GET", "POST"])
def signup():
	if request.method == "POST":
		# Save user info to database
		name = request.form["name"]
		email = request.form["email"]
		pwd = request.form["pwd"]
		confirm_pwd = request.form["confirm_pwd"]
		
		if name != "" and email != "" and pwd != "" and pwd == confirm_pwd:
			# SELECT * FROM users WHERE email LIKE ? LIMIT 1
			# INSERT INTO users (name, email, pwd) VALUES (?, ?, md5(?));
			pass
	else:
		# Show sign-up page
		return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		# Starting session for user
		email = request.form["email"]
		pwd = request.form["pwd"]
		
		if email != "" and pwd != "":
			# SELECT id FROM users WHERE email LIKE ? AND pwd LIKE md5(?) LIMIT 1;
			pass
	else:
		# Show sign-up page
		return render_template("login.html")

@app.route("/logout", methods=["POST"])
def logout():
	if request.method == "POST":
		# Destroy user session

@app.route("/profile", methods=["GET", "POST", "DELETE"])
def profile():
	# SELECT * FROM users WHERE id=?
	if request.method == "POST":
		# Update user information
		name = request.form["name"]
		email = request.form["email"]
		
		if name != "" and email != "":
			# SELECT * FROM users WHERE email LIKE ? LIMIT 1
			# UPDATE users SET name=?, email=? WHERE id=?;
			pass
	elif request.method == "DELETE":
		# Delete user information (and images)
		# DELETE FROM images WHERE user_id=?;
		# DELETE FROM users WHERE id=?;
	else:
		# Show profile information
		return render_template("profile.html")

# i.e. www.picflick.com/profile/password
@app.route("/profile/password", methods=["POST"])
def password():
	if request.method == "POST":
		# Update user password
		pwd = request.form["pwd"]
		confirm_pwd = request.form["confirm_pwd"]
		
		if pwd != "" and pwd != confirm_pwd:
			# UPDATE users SET pwd=md5(?) WHERE id=?;
			pass

# i.e. www.picflick.com/upload
@app.route("/upload", methods=["GET", "POST"])
def upload():
	if request.method == "POST":
		# Upload image to server
		# INSERT INTO images (user_id, file_name, month_created, year_created) VALUES (?, ?, ?, ?);
	else:
		render_template("upload.html")

# i.e. www.picflick.com/gallery/5
@app.route("/gallery/<user_id>")
def gallery(user_id):
	# Show image gallery
	# SELECT * FROM images WHERE user_id=?

# i.e. www.picflick.com/gallery/5/image/42
@app.route("/gallery/<user_id>/image/<image_id>", methods=["GET", "DELETE"])
def image(user_id, image_id):
	if request.method == "DELETE":
		# Delete an image
		# DELETE FROM images WHERE id=?;
	else:
		# Show the specific image
		# SELECT * FROM images WHERE id=?

if __name__ == "__main__":
	app.run(debug=True)
