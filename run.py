from app import app

print app.config["DEBUG"]

app.run(debug = True)
