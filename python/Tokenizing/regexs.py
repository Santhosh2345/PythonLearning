import re

# 1. Take a messy sentence with mixed casing, extra whitespace, and punctuation. Normalize it with .strip().lower(), then tokenize it with .split().
text = "   HELLO!!!   My name is Santhosh...  I LOVE   Python & AI,  but I'm STILL learning!!!   "
normalize_text = text.strip().lower()
text_list = normalize_text.split()
print(f'Normalized text: {text_list}')

# 2. Write a stopword list (at least 8-10 words) and filter a sentence's tokens against it using a list comprehension.
stopwords = ["is", "was", "the", "this", "a", "an", "on", "that", "am", "are", "i", "my", "and", "or", "i'm", "but", "to", "in", "of", "for", "with", "at", "by", "from"]
tokens = [word for word in text_list if word not in stopwords]
print(f'Tokens after removing stopwords: {tokens}')

# 3. Use re.findall() to extract all numbers from a sentence containing several (like "I have 3 cats, 2 dogs, and 15 fish").
text = "I have 3 cats, 2 dogs, and 15 fish"
numbers_in_text = re.findall(r"\d+", text)
print(f'Numbers in text: {numbers_in_text}')

# 4. Use re.sub() to mask all email addresses in a block of text with "[EMAIL]".
text = "Primary email: sk@gmail.com, Secondary email: john@yahoo.com"
masked_email = re.sub(r"\S+@\S+", "[EMAIL]", text)
print(f'Masked email: {masked_email}')

log_lines = [
    "2024-01-15 ERROR: Login failed- for alex@test.com from IP 192.168.1.10",
    "2024-01-15 INFO: (User) priya@test.com logged in successfully",
    "2024-01-16 ERROR: Timeout! connecting to 10.0.0.5 for user sam@test.com"
]

final_clean_token = []
no_dup_final_clean_token = []

for log_line in log_lines:
# 1. For each log line, extract the email address and IP address (if present) using regex
    email_address = re.search(r"\S+@\S+", log_line)
    email_address = email_address.group() if email_address else None

    ip_address = re.search(r"\d{3}.\d{3}.\d{1}.\d{2}", log_line)
    ip_address = ip_address.group() if ip_address else None
    print(f'Email address: {email_address}, IP address: {ip_address}')

# 2. Build a "sanitized" version of each log line with emails replaced by "[EMAIL]" and IPs replaced by "[IP]"
    email_masked = re.sub(r"\S+@\S+", "[EMAIL]", log_line)
    print(f'Masked log line: {email_masked}')

    ip_masked = re.sub(r"\d{3}.\d{3}.\d{1}.\d{2}", "[IP]", email_masked)
    print(f'Masked IP line: {ip_masked}')

# 3. Tokenize each sanitized log line (lowercase, punctuation removed)
    tokens = re.sub(r"[^\w\s-]", "", ip_masked).lower()
    tokens = tokens.split()
    print(f'Tokens: {tokens}')

# 4. Remove stopwords from the tokens
    final_clean_token.extend([token for token in tokens if token not in stopwords])
    print()

print(f'Final clean tokens: {final_clean_token}')
for token in final_clean_token:
    if token not in no_dup_final_clean_token:
        no_dup_final_clean_token.append(token)

print(f'Final clean tokens after removing duplicates: {no_dup_final_clean_token}')