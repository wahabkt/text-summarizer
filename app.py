from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def chatbot():
    print("Chatbot Summarizer. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        # Summarize input
        summary = summarizer(user_input, max_length=50, min_length=10, do_sample=False)
        print("Summary:", summary[0]['summary_text'])

if __name__ == "__main__":
    chatbot()
