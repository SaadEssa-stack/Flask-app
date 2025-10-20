from flask import Flask, request, send_file, render_template_string
import pandas as pd
import io

app = Flask(__name__)

# Page d'accueil avec formulaire d'upload
@app.route('/')
def home():
    return render_template_string('''
        <h2>Upload ton fichier Excel</h2>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="fichier" required>
            <button type="submit">Analyser</button>
        </form>
    ''')

# Route pour traiter le fichier uploadé
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['fichier']
    df = pd.read_excel(file)

    # Exemple : filtrer les montants < 1000 €
    result = df[df["Montant (€)"] < 1000]

    # Sauvegarde du résultat dans un fichier Excel en mémoire
    output = io.BytesIO()
    result.to_excel(output, index=False)
    output.seek(0)

    return send_file(
        output,
        as_attachment=True,
        download_name="montant_inferieur_a_1000.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

if __name__ == '__main__':
    app.run(debug=True)