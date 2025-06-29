from transformers import pipeline

# Initialize the summarizer (do this once at module level for efficiency)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_trend_risk_insights(headlines):
    """
    Use an LLM to extract top risks, bullish/bearish drivers, and noteworthy events from headlines.
    Returns a summary as bullet points.
    """
    input_text = "\n".join(headlines)
    prompt = (
        "Extract the top risks, bullish and bearish drivers, and noteworthy events from the following financial news headlines. "
        "Summarize them as concise bullet points."
    )
    full_input = prompt + "\n" + input_text
    summary = summarizer(full_input, max_length=200, min_length=50, do_sample=False)[0]['summary_text']
    return summary
