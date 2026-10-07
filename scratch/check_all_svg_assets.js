const fs = require('fs');
const path = require('path');
const dir = './images/Sprance images/UI';

fs.readdirSync(dir).filter(f => f.endsWith('.svg')).forEach(file => {
  const content = fs.readFileSync(path.join(dir, file), 'utf8');
  const hasBase64 = content.includes('data:image/');
  const hrefs = content.match(/href="([^"]+)"/g) || [];
  const nonDataHrefs = hrefs.filter(h => !h.includes('data:') && !h.startsWith('href="#'));
  console.log(file, 'hasBase64:', hasBase64, 'nonDataHrefs count:', nonDataHrefs.length, nonDataHrefs.slice(0, 3));
});
