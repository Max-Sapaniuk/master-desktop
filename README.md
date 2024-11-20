# Fake News Detection Application

This project is a simple Fake News Detection application with a graphical user interface (GUI) built using **Tkinter**. It uses a pre-trained **RoBERTa** model for text classification and can classify input messages or text extracted from URLs as either "Fake News" or "Real News."

## Project Overview

The application allows users to input text or provide a URL. If a URL is provided, the application extracts the text from the webpage and classifies it as fake or real. If a direct text message is provided, the application classifies it as fake or real directly.

The classification is powered by a fine-tuned **RoBERTa** model, trained to detect fake news, which is loaded into the app from the local directory.

## Features

- **Text Classification**: Users can input text to detect fake news.
- **URL Support**: Users can input a URL, and the application will extract text from the page and classify it.
- **Graphical User Interface (GUI)**: A user-friendly GUI built with Tkinter to interact with the model.
- **Pre-trained RoBERTa Model**: The app uses a fine-tuned RoBERTa model to classify the input text as "Fake News" or "Real News."

## Requirements

- Python 3.11
- PyTorch
- Transformers
- Tkinter
- BeautifulSoup
- Requests

You can install the necessary dependencies with the following command:

******Note**: Tkinter is usually included with Python. If it's not installed, you can install it using your system's package manager (e.g., `apt-get install python3-tk` on Ubuntu).

## Files Overview

### `main.py`

This script is the core of the application. It loads the pre-trained RoBERTa model and tokenizer, provides functions to classify messages, extract text from URLs, and create the Tkinter-based GUI for user interaction.

1. **Model Loading**: The script loads the fine-tuned RoBERTa model from the local directory `./working/fake-news-model`.
2. **Message Classification**: The `classify_message()` function classifies the input message (or extracted webpage text) as "Fake News" or "Real News" using the pre-trained model.
3. **Text Extraction from URL**: The `extract_text_from_url()` function uses BeautifulSoup to extract the text content from a provided URL.
4. **GUI Creation**: The GUI is built using Tkinter, and users can input either a text message or a URL for analysis.

### Key Functions:

- **`classify_message(message)`**: Takes a message and returns whether it is "Fake News" or "Real News."
- **`extract_text_from_url(url)`**: Extracts the text content from a given URL using BeautifulSoup and requests.
- **`create_gui()`**: Sets up the Tkinter GUI where users can interact with the app.

### GUI Features:

- **Text Input**: Allows users to input a message directly.
- **URL Input**: Allows users to provide a URL, from which text is extracted and classified.
- **Check Button**: A button that triggers the classification process.
- **Result Label**: Displays the result of the classification ("Fake News" or "Real News").

### Example Workflow:

1. **Run the Application**: Execute the following command to start the app:

   ```bash
   python main.py
   ```

2. **Enter a Message or URL**: 
   - If you enter a text message, the application will classify it as either "Fake News" or "Real News."
   - If you enter a URL, it will extract the content from the webpage and classify it.

3. **View the Results**: The result will be displayed in the app as either "Fake News" or "Real News."