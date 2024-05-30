# Tandem read tracker
### Introduction
This application is designed to track a reader's progress through the Throne of Glass Tandem Read. The front end, built with <b>React</b>, communicates with a <b>Flask</b> backend, which interfaces with an <b>SQLite</b> database. This architecture ensures efficient data handling and a seamless user experience. The application supports user-generated comments for each reading section, enabling users to document their emotional journey and optimise their reading experience. Additionally, the system provides visual suggestions for upcoming sections, enhancing user engagement and motivation.

### Throne of Glass tandem read
In Sarah J. Maas's Throne of Glass series, the "Tandem Read" is a fan-recommended approach where readers simultaneously read the fifth book, Empire of Storms, and the sixth book, Tower of Dawn. These books' events occur concurrently, with Empire of Storms focusing on Aelin Galathynius and her allies, and Tower of Dawn on Chaol Westfall's journey. Following a chapter-by-chapter guide, readers can synchronise the timelines, enhancing their understanding of the interconnected narratives and enriching the overall storytelling experience.

### Run this in dev mode
- Serve Flask locally on localhost 5000

    <code>flask run --debug</code>

- Serve React frontend locally

    <code>cd tog_tracker</code>

    <code>pnpm run dev</code>
