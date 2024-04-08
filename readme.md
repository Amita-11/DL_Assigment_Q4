# GAN Image Generator

This project implements a Generative Adversarial Network (GAN) using TensorFlow,Keras and Flask to generate images based on an uploaded image.

## Overview

The project consists of the following components:

1. **Python Script**: The main script (`app.py`) defines a Flask web application with routes for uploading an image, generating new images using a pre-trained GAN model, and displaying the generated images.

2. **Pre-trained Model**: A pre-trained GAN model (`generator_model.keras`) is loaded and used to generate new images based on the uploaded image.

3. **HTML Template**: An HTML template (`index.html`) is rendered to display the uploaded and generated images.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Amita-11/DL_Assigment_Q4.git
   ```

2. Navigate to the project directory:

   ```
   cd DL_Assigment_Q4
   ```

3. Install dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```
   python app.py
   ```

5. Open your web browser and go to `http://localhost:5000` to access the application.

## Usage

1. Upload an image using the provided form.

2. Click the "Generate" button to generate new images based on the uploaded image.

3. View the original and generated images on the web page.

## Customization

You can customize the GAN model architecture, training parameters, and web interface according to your requirements by modifying the Python script and HTML template.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project is inspired by the concept of Generative Adversarial Networks (GANs) and utilizes the TensorFlow library for implementation.
- Special thanks to the developers of Flask for providing a simple and powerful web framework for Python.
