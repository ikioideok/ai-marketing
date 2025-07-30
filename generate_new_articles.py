
import os
import re
import glob
from datetime import datetime

def extract_article_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else os.path.basename(file_path)

    date_match = re.search(r'<time datetime="(\d{4}-\d{2}-\d{2})">', content)
    date_str = date_match.group(1) if date_match else '1970-01-01' # Default date if not found
    
    # Try to find image from hero-featured-card or new-article-card
    img_match = re.search(r'<img src="(.*?)" alt=".*?"', content)
    image_url = img_match.group(1) if img_match else 'https://via.placeholder.com/300x160?text=No+Image' # Default image

    category_match = re.search(r'<span class="card-category">(.*?)</span>', content)
    if not category_match:
        category_match = re.search(r'<div class="category-label">(.*?)</div>', content)
    category = category_match.group(1) if category_match else '未分類'

    # Adjust URL for articles within pages/categories
    relative_path = os.path.relpath(file_path, start=os.path.dirname(os.path.dirname(file_path)))
    
    return {
        'path': relative_path,
        'title': title,
        'date': datetime.strptime(date_str, '%Y-%m-%d'),
        'image_url': image_url,
        'category': category
    }

def generate_article_card_html(article):
    # Adjust image URL if it's a relative path from the article file
    # This is a simplification; a more robust solution would resolve relative paths
    # based on the article's location relative to index.html
    if article['image_url'].startswith('http'):
        final_image_url = article['image_url']
    else:
        # Assuming images are in the root directory for simplicity, or adjust as needed
        final_image_url = article['image_url'].replace('../../', '') # Remove common relative path prefixes

    return f'''
                    <div class="new-article-card">
                        <a href="{article['path']}">
                            <img src="{final_image_url}" alt="{article['title']}">
                            <div class="card-content">
                                <div class="card-meta">
                                    <span class="card-category">{article['category']}</span>
                                    <time datetime="{article['date'].strftime('%Y-%m-%d')}">{article['date'].strftime('%Y.%m.%d')}</time>
                                </div>
                                <h4>{article['title']}</h4>
                            </div>
                        </a>
                    </div>'''

def main():
    project_root = "/Users/mizumayuuki/オウンドメディア/"
    articles_dir = os.path.join(project_root, 'articles')
    pages_categories_dir = os.path.join(project_root, 'pages', 'categories')
    index_html_path = os.path.join(project_root, 'index.html')

    all_article_files = []
    all_article_files.extend(glob.glob(os.path.join(articles_dir, '*.html')))
    all_article_files.extend(glob.glob(os.path.join(pages_categories_dir, '**', '*.html'), recursive=True))

    articles_data = []
    for file_path in all_article_files:
        try:
            data = extract_article_data(file_path)
            articles_data.append(data)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue

    # Sort articles by date in descending order
    articles_data.sort(key=lambda x: x['date'], reverse=True)

    # Generate HTML for the new articles section
    new_articles_html_cards = ""
    # Limit to a reasonable number, e.g., 10 or 20, for the scroller
    for article in articles_data[:30]: # Display up to 30 latest articles
        new_articles_html_cards += generate_article_card_html(article)

    # Read index.html content
    with open(index_html_path, 'r', encoding='utf-8') as f:
        index_content = f.read()

    # Define the section to replace
    start_marker = '<div class="new-articles-container">'
    end_marker = '</div>' # This assumes the closing div is unique enough

    # Find the content between markers
    start_index = index_content.find(start_marker)
    end_index = index_content.find(end_marker, start_index + len(start_marker))

    if start_index != -1 and end_index != -1:
        # Extract the part to be replaced
        old_articles_section = index_content[start_index + len(start_marker):end_index]
        
        # Replace the old content with the new generated cards
        updated_index_content = index_content.replace(old_articles_section, new_articles_html_cards)

        # Write the updated content back to index.html
        with open(index_html_path, 'w', encoding='utf-8') as f:
            f.write(updated_index_content)
        print("NEW ARTICLES section in index.html updated successfully.")
    else:
        print("Could not find the NEW ARTICLES section markers in index.html. Please check the HTML structure.")

if __name__ == "__main__":
    main()
