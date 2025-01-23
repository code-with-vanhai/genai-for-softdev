from flask import Flask, jsonify, request, Response
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/api/hello', methods=['GET'])
def hello_world():
    """
    Handles GET request to return a JSON response with "Hello, World!"
    """
    if request.method == 'GET':
        app.logger.info("GET /api/hello called successfully.")
        return jsonify({"message": "Hello, World!"}), 200

@app.errorhandler(404)
def not_found(error):
    """
    Handles invalid routes by returning a 404 error response
    """
    app.logger.warning(f"404 Error: {request.path} not found.")
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """
    Handles unsupported HTTP methods
    """
    app.logger.warning(f"405 Error: Method not allowed for {request.url}")
    return jsonify({"error": "Method not allowed"}), 405

@app.errorhandler(500)
def internal_server_error(error):
    """
    Handles server errors gracefully
    """
    app.logger.error("500 Error: Internal Server Error.")
    return jsonify({"error": "Internal server error"}), 500

@app.after_request
def set_response_headers(response):
    """
    Set security headers and standard response headers
    """
    response.headers['Content-Type'] = 'application/json'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=63072000; includeSubDomains'
    return response

@app.route('/api/hello', methods=['POST', 'PUT', 'DELETE'])
def method_not_supported():
    """
    Handles unsupported HTTP methods explicitly for /api/hello
    """
    return jsonify({"error": "Method not allowed"}), 405

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to monitor the app status
    """
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=True)
