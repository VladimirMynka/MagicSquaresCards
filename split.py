import os
import csv
import re

def parse_card(card_text):
    """Парсит текст карточки и извлекает мета-информацию."""
    title_match = re.search(r"# (.*)", card_text)
    info_type_match = re.search(r"### Info type\n(.*)", card_text)
    keywords_match = re.search(r"### Keywords\n(.*)", card_text)
    approves_match = re.search(r"### Approves\n(.*)", card_text)
    text_match = re.search(r"### Text\n(.*)", card_text)

    title = title_match.group(1).strip() if title_match else "No Title"
    info_type = info_type_match.group(1).strip() if info_type_match else "No Info Type"
    keywords = [kw.strip().replace('~', '') for kw in keywords_match.group(1).split(',')] if keywords_match else []
    tag = keywords[0] if keywords else "No Tag"
    approves = approves_match.group(1).strip() if approves_match else ""
    text = text_match.group(1).strip().replace("'''", "```") if text_match else ""

    return title, info_type, tag, keywords, approves, text

def save_card(card_dir, tag, card_text, info_type):
    """Сохраняет весь markdown текст карточки в файл."""
    directory = os.path.join(card_dir, info_type)
    os.makedirs(directory, exist_ok=True)
    filename = f"{tag.replace(' ', '_')}.md"
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(card_text)
    return filename

def process_messages(messages, output_dir):
    """
    Обрабатывает список сообщений, сохраняет карточки и мета-информацию.

    Args:
      messages: A list of strings, where each string contains one or more card texts.
      output_dir: The directory where card files and the CSV file will be saved.
    """
    
    os.makedirs(output_dir, exist_ok=True)
    
    csv_file_path = os.path.join(output_dir, 'cards_metadata.csv')
    
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['filename', 'title', 'info_type', 'tag', 'keywords', 'approves'])  # Заголовок CSV

        for message in messages:
           
            card_texts = message.split('```md\n')
            card_texts = [card_text for card_text in card_texts if card_text.strip()]
            
            for card_text in card_texts:
                title, info_type, tag, keywords, approves, text = parse_card(card_text)
                filename = save_card(output_dir, tag, card_text.replace("'''", "```"), info_type)
                csv_writer.writerow([filename, title, info_type, tag, ', '.join(keywords), approves])
                print(f"Processed and saved: {title}")
                
                
if __name__ == "__main__":
    messages = []
    for file in os.listdir('raw'):
        with open(os.path.join('raw', file), 'r', encoding='utf-8') as f:
            messages.append(f.read())
    process_messages(messages, 'cards')
