import openai

# Set your API key here
openai.api_key = 'your-api-key'

def generate_topic(topic, tone='informative', length=280):
    
    prompt = f"Create a topic about '{topic}' in a {tone} tone. Ensure it is engaging and under {length} characters."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant skilled at writing topic."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=60,  # Adjust as needed to ensure the topic fits the character limit
        n=1,
        stop=None,
        temperature=0.7  # Adjust for creativity
    )
    topic = response.choices[0].message['content'].strip()
    return topic

# Example usage
topic = "climate change"
tone = "informative"
result = generate_tweet(topic, tone)
print(result)
