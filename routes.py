from models import *



@app.route('/identify', methods=['POST'])
def identify():
    if 'image' not in request.files:
        return jsonify({'error': 'Aucune image trouvée'}), 400

    image = request.files['image']
    # Chemin temporaire pour sauvegarder l'image
    temp_path = os.path.join('temp', image.filename)
    image.save(temp_path)

    # Prédire l'animal à partir de l'image (utilisez votre modèle TensorFlow ici)
    predicted_animal = predict_animal(model, temp_path)  # Remplacez par votre code de prédiction

    os.remove(temp_path)  # Nettoyez le fichier temporaire

    return jsonify({'animal': predicted_animal})


@app.route("/")
def index():
    return jsonify({"nom": "MBANZILA DIMBOU victory"})