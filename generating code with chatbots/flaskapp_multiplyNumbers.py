from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/multiply', methods=['GET'])
def multiply():
    """
    Handles GET requests to multiply two numbers.
    Expects query parameters 'a' and 'b'.
    Returns a JSON response with the result or an error message.
    """
    try:
        # Get query parameters
        a = request.args.get('a')
        b = request.args.get('b')

        # Validate input
        if a is None or b is None:
            return jsonify({"error": "Missing query parameters 'a' and 'b'."}), 400

        # Convert parameters to integers
        a = int(a)
        b = int(b)

        # Perform multiplication
        result = a * b
        return jsonify({"a": a, "b": b, "result": result}), 200

    except ValueError:
        return jsonify({"error": "Query parameters 'a' and 'b' must be integers."}), 400

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
