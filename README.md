# AI Attention Visualizer

AI Attention Visualizer is a web application that helps users understand how Transformer-based language models focus on different words in a sentence. The project visualizes attention weights using heatmaps, making it easier to explore and interpret the behavior of modern Natural Language Processing (NLP) models.

## Live demo

https://aiattentionvisualizer-qtdsorhgpmsdheobguxfy9.streamlit.app/


## Features

* Visualize attention scores from Transformer models
* Generate attention heatmaps
* Interactive and user-friendly interface
* Real-time text analysis
* Supports custom text input
* Helps understand model decision-making
* Useful for learning Transformer architectures and attention mechanisms

## Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* NumPy
* Matplotlib
* Seaborn

## Project Structure

```text
AI_Attention_Visualizer/
│
├── app.py
├── requirements.txt
├── README.md
├── assets/
│   ├── homepage.png
│   └── attention_heatmap.png
│
└── utils/
    └── attention_utils.py
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/Hemalatha217/AI_Attention_Visualizer.git
cd AI_Attention_Visualizer
```

### Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run app.py
```

After running the command, open the local URL displayed in the terminal.

## How It Works

1. Enter a sentence or text input.
2. The Transformer model processes the text.
3. Attention weights are extracted from the model.
4. A heatmap is generated to visualize attention patterns.
5. Users can analyze how different words influence each other within the model.

## Screenshots
<img width="599" height="172" alt="Screenshot 2026-09-30 141534" src="https://github.com/user-attachments/assets/f7340052-6e28-428f-93d7-8ff9686fe8c5" />

<img width="197" height="200" alt="image" src="https://github.com/user-attachments/assets/6d490194-0a5f-4f43-9a58-992d6cf91db6" />



### Home Page

```markdown
![Home Page](assets/homepage.png)
```

### Attention Visualization

```markdown
![Attention Heatmap](assets/attention_heatmap.png)
```

## Applications

* NLP Education
* Transformer Model Analysis
* Explainable AI (XAI)
* Deep Learning Visualization
* Research and Learning

## Learning Outcomes

* Understand self-attention mechanisms
* Explore Transformer architectures
* Interpret model behavior visually
* Learn explainable AI concepts
* Analyze relationships between words in text

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to GitHub.

```bash
git push origin feature-name
```

5. Open a Pull Request.

## License

This project is available under the MIT License.

## Author

Hemalatha K

GitHub: https://github.com/Hemalatha217
