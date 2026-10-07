const fs = require('fs');
const path = require('path');
const dir = './images/Sprance images/UI';

const files = fs.readdirSync(dir);
files.forEach(file => {
  if (file.endsWith('.svg')) {
    const content = fs.readFileSync(path.join(dir, file), 'utf8');
    const vb = content.match(/viewBox=["']([^"']+)["']/);
    const w = content.match(/width=["']([^"']+)["']/);
    const h = content.match(/height=["']([^"']+)["']/);
    console.log(`${file} -> viewBox: ${vb ? vb[1] : 'none'} | w: ${w ? w[1] : ''} | h: ${h ? h[1] : ''}`);
  }
});
