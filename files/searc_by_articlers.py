import json

# Load the JSON files with UTF-8 encoding
with open('constitution_of_india.json', 'r', encoding='utf-8') as f:
    full_articles = json.load(f)

with open('simplified_.json', 'r', encoding='utf-8') as f:
    simplified_articles = json.load(f)

# Create dictionaries for quick lookup
full_articles_dict = {str(article['article']): article for article in full_articles}
simplified_articles_dict = {article['article']: article for article in simplified_articles}

def get_article_info(article_num):
    """
    Retrieve and print the article description and simplified form based on the article number.
    """
    article_num_str = str(article_num)
    
    # Fetch the full description
    full_article = full_articles_dict.get(article_num_str, {})
    full_description = full_article.get('description', 'Description not found')
    
    # Fetch the simplified description
    simplified_article = simplified_articles_dict.get(article_num_str, {})
    simplified_description = simplified_article.get('description', 'Simplified description not found')
    
    # Print the results
    print(f"Article num: {article_num_str}")
    print(f"Description: {full_description}")
    print(f"Simplification: {simplified_description}")
    
    # Print clauses if available
    if 'clauses' in simplified_article:
        print("Clauses:")
        for clause in simplified_article['clauses']:
            print(f"  - {clause['article']}: {clause['description']}")
    print()

# Example usage:
# Get information for articles 53 and 1
article_numbers = [1]
for num in article_numbers:
    get_article_info(num)
