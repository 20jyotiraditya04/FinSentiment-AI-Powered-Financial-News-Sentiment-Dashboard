from transformers import pipeline

# Initialize once at the top of your module
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(headlines, sentiment_summary, avg_sentiment):
    input_text = " ".join(headlines)
    input_text += f"\nOverall sentiment: {sentiment_summary.lower()} with an average score of {avg_sentiment:.2f}."
    summary = summarizer(input_text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    return summary
