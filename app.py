from flask import Flask, request, jsonify
from controllers.getResponses import getResponses
from controllers.createEmbeddings import createEmbeddings
from controllers.deleteEmbeddings import deleteCollection


app = Flask(__name__)

@app.route("/getResponses", methods=["GET"])
def get_responses():
    query = request.args.get('query')
    responses = getResponses(query)
    response = {
        "query":query,
        "responses": responses
    }
    return jsonify(response)


@app.route("/createEmbeddings", methods=["POST"])
def create_embeddings():
    createEmbeddings()
    return "Embeddings created", 201


@app.route('/deleteEmbeddings', methods=['DELETE'])
def delete_embeddings():
    deleteCollection("collection")
    return 'Embeddings deleted', 204


if __name__ == '__main__':
    app.run(debug=True)