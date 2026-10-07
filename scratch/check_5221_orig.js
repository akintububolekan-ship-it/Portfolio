const fs = require('fs');
const c = fs.readFileSync('./images/Sprance images/UI/Frame 1000005221.svg', 'utf8');
const m = c.match(/_(\d+_\d+)/g);
console.log('Frame 1000005221.svg matches:', [...new Set(m)].slice(0, 5));
