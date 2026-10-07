const fs = require('fs');
const path = require('path');
const dir = './images/Sprance images/UI';

['Frame 1000005221.svg', 'Frame 1000005221-1.svg', 'Frame 1000005221-2.svg', 'Frame 1000005221-3.svg'].forEach(f => {
  const c = fs.readFileSync(path.join(dir, f), 'utf8');
  // Check for any id or image href or class names
  const ids = (c.match(/id="([^"]+)"/g) || []).slice(0, 10);
  const images = (c.match(/xlink:href="([^"]+)"/g) || c.match(/href="data:image\/([^;]+);/g) || []).slice(0, 5);
  console.log(f, 'IDs:', ids, 'Image types:', images);
});
