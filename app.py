from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import io

app = Flask(__name__)

# Load the pre-trained generator model
loaded_generator = tf.keras.models.load_model("generator_model.keras")

# Define the latent dimension
LATENT_DIM = 100

def preprocess_image(image):
    image = image.resize((64, 64))
    image = np.array(image)
    image = (image.astype(np.float32) / 255.0 - 0.5) * 2.0
    image = np.expand_dims(image, axis=0)
    return image

def generate_images(image):
    # Preprocess the image
    processed_image = preprocess_image(image)

    # Generate 5 images using the pre-trained generator
    latent_vectors = tf.random.normal(shape=(5, LATENT_DIM))
    generated_images = loaded_generator.predict(latent_vectors)

    # Plot original and generated images
    plt.figure(figsize=(18, 12))
    plt.subplot(2, 5, 1)
    plt.title("Original Image")
    plt.imshow(image)
    plt.axis("off")
    for i in range(5):
        plt.subplot(2, 5, i + 2)
        plt.title("Generated Image {}".format(i + 1))
        plt.imshow((generated_images[i] + 1) / 2)
        plt.axis("off")
    plt.savefig("static/generated_images.jpg")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded image file
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            # Read the image file
            image = Image.open(uploaded_file)
            # Generate images using the pre-trained model
            generate_images(image)
            return render_template("index.html", generated_image_path="/static/generated_images.jpg")

    return render_template("index.html", generated_image_path=None)

if __name__ == "__main__":
    app.run(debug=True)
