# File: animals_web_generator.py
import data_fetcher

def generate_animal_cards(data):
    """Generates HTML card snippets for each animal."""
    if not data:
        return "<h2>The animal doesn't exist or couldn't be found.</h2>"

    cards_html = ""
    for animal in data:
        type_field = f"<strong>Type:</strong> {animal['taxonomy'].get('type', 'N/A')}<br>"
        diet_field = f"<strong>Diet:</strong> {animal['characteristics'].get('diet', 'N/A')}<br>"
        locations = " and ".join(animal.get('locations', ['N/A']))
        location_field = f"<strong>Locations:</strong> {locations}"
        cards_html += f"""
        <li class="cards__item">
            <div class="card__title">{animal['name']}</div>
            <p class="card__text">
                {type_field}{diet_field}{location_field}
            </p>
        </li>
        """
    return cards_html

def write_html(cards_html, output_file='animals.html', template_file='animals_template.html'):
    """Writes the final HTML file using the template and generated cards."""
    try:
        with open(template_file, 'r') as template:
            template_content = template.read()

        final_html = template_content.replace('__REPLACE_ANIMALS_INFO__', cards_html)

        with open(output_file, 'w') as output:
            output.write(final_html)
        print(f"Website was successfully generated: {output_file}")
    except FileNotFoundError as e:
        print(f"Error: {e}")

def main():
    animal_name = input("Enter the name of an animal: ").strip()
    try:
        data = data_fetcher.fetch_data(animal_name)
        animal_cards = generate_animal_cards(data)
        write_html(animal_cards)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
