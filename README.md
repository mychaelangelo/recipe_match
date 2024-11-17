# 🥙 Recipe Finder

A Streamlit application that analyzes images of ingredients and suggests recipes using GPT-4 Vision.

## Features

- Upload images or PDFs of ingredients
- Take pictures directly through your webcam
- Get detailed recipe suggestions based on visible ingredients
- Download results as markdown files

## Prerequisites

- Python 3.8+
- OpenAI API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/recipe-finder.git
cd recipe-finder
```

```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key either:
   - Create a `.env` file with: `OPENAI_API_KEY=your_api_key_here`
   - Or enter it directly in the application when prompted

## Usage

1. Start the application:

```bash
streamlit run app.py
```

2. Open your web browser to the displayed URL (typically `http://localhost:8501`)

3. Choose your input method:
   - Upload an image/PDF of ingredients
   - Take a picture using your phone

4. Click "Process Image" to get recipe suggestions

## Output

The app will provide:
- Detailed ingredient analysis
- Recipe suggestions
- Cooking instructions
- Food safety notes
- Option to download results as markdown

## Environment Variables

| Variable | Description | Required |
|----------|-------------|-----------|
| OPENAI_API_KEY | Your OpenAI API key | Yes |

## Notes

- Supported file formats: PDF, PNG, JPEG, JPG
- Image analysis uses GPT-4o


