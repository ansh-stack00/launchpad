const fs = require('fs');


const lorem = `Lorem ipsum dolor sit amet consectetur adipiscing elit Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua`.split(' ');
const target_words = 250_000

const output_file = 'corpus.txt';

function generate_text() {
    const lines = [];

    while (lines.length < target_words) {
        const sentence = [...lorem, String(Math.floor(Math.random() * 10000))].join(' ');
        lines.push(sentence);
    }

    const text = lines.join('\n')

    fs.writeFile(output_file, text, 'utf-8', (err) => {
        if (err) throw err;
        console.log(`Generated ${output_file} with ${target_words} lines`);
    });
}


generate_text()