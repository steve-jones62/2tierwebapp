from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# List to store collected data
data_list = []

@app.route('/')
def index():
    """Render the main webpage with the form and table."""
    return render_template('index.html', data=data_list)

@app.route('/submit', methods=['POST'])
def submit():
    """
    Handle form submission, process the data,
    and update the data list.
    """
    name = request.form.get('name')
    age = request.form.get('age')
    city = request.form.get('city')

    if not name or not age or not city:
        return jsonify({'error': 'All fields are required!'}), 400

    # Check if the name already exists in the data list
    for entry in data_list:
        if entry['Name'] == name:
            entry['Count'] += 1
            return jsonify({'success': True, 'data': data_list})

    # Add new data to the list
    data_list.append({'Name': name, 'Age': age, 'City': city, 'Count': 1})
    return jsonify({'success': True, 'data': data_list})


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)