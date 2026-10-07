const fs = require('fs');

['Frame 564.svg', 'Frame 1000005348.svg'].forEach(file => {
  const content = fs.readFileSync('./images/Sprance images/UI/' + file, 'utf8');
  console.log(file, 'has base64 image:', content.includes('data:image/'), 'has external image:', content.includes('http'));
});
