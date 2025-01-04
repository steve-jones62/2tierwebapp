from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# List to store the data
data_list = []

@app.route("/")
def index():
    """
    Render the main page with the form and the table.
    """
    return render_template("index.html", data=data_list)

@app.route("/submit", methods=["POST"])
def submit_data():
    """
    Handle form submission, convert the data to JSON, and add it to the list.
    """
    global data_list
    # Get data from the form
    form_data = request.form.to_dict()
    
    # Append data to the list
    data_list.append(form_data)
    
    # Return the updated table rows as JSON
    return jsonify(data_list)

if __name__ == "__main__":
    app.run(debug=True)