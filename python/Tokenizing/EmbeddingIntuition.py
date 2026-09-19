from sentence_transformers import SentenceTransformer, util
import re

# Install sentence-transformers, load the model, and embed 3-4 sentences of your own choosing. 
# Print the shape of one embedding to confirm it's a long vector of numbers.
text = [
    "Python is GREAT!!!",
    "I ate biryani yesterday",
    "AI can HELP us solve real-world problems..." 
]

text_token = []
for sentence in text:
    clean_sentence = re.sub(r'[^\w\s]',"", sentence)
    text_token.append(clean_sentence)
print(f'Tokens: {text_token}')

model = SentenceTransformer('all-MiniLM-L6-V2')
embeddings = model.encode(text_token)

print(f'Text embedding: {embeddings.shape}')

# Pick two sentences that mean similar things but use completely different words, 
# and compute their cosine similarity. Then compare against a third, 
# unrelated sentence — confirm the similarity score is meaningfully lower.
text2 = [
    "This Diamond and Golds are beautifull", 
    "Perspective of the earth is wonder"
]
unrelated_text = "Hola!, I am going to build home and buy car"

input_text = model.encode(text2)
unrelated_texts = model.encode(unrelated_text)

similarity_score = util.cos_sim(unrelated_texts, input_text)[0]
similarity_low = similarity_score.argmin()
print(f'Low similarity of query in text2: {similarity_low}')

print(f'Similarity of the text: {text2[similarity_low]}')
print()


# 3. Build the semantic search example above using your own list of 5-6 "notes" 
# (could be real notes from your QA work, or made up), 
# and try 2-3 different search queries against them.
notes = [
    "Login fails when the user enters an incorrect password.",
    "The checkout page takes more than 5 seconds to load.",
    "API returns 401 when authentication token is missing.",
    "Users cannot reset their password using the forgot password link.",
    "Payment fails when the card has insufficient balance.",
    "The application crashes when a large file is uploaded.",
    "API returns 500 when authentication token is missing."
]
queries = [
    "Why can't users log in?",
    "Problems with payment",
    "API authentication error"
]

embedded_notes = model.encode(notes)
embedded_queries = model.encode(queries)

for query, embedded_query in zip(queries, embedded_queries):
    scores = util.cos_sim(embedded_query, embedded_notes)[0]
    print(f'Scores: {scores}')

    best_match = scores.argmax()
    print(f'Best match: {best_match}')

    print("Query: ", query)
    print("Best match:", notes[best_match])
    print("Score:", scores[best_match].item())
    print()