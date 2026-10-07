const fs = require('fs');
const svg = fs.readFileSync('images/UI/Frame 1000005197.svg', 'utf8');

const paints = svg.match(/<linearGradient id="paint[0-9]+_linear_424_12172"[\s\S]*?<\/linearGradient>/g) || [];
paints.forEach(p => console.log(p));
