const fs = require('fs');

['Frame 1000005221.svg', 'Frame 1000005221-1.svg', 'Frame 1000005221-2.svg', 'Frame 1000005221-3.svg'].forEach(file => {
  const c = fs.readFileSync('./images/Sprance images/UI/' + file, 'utf8');
  console.log(file, 'length:', c.length);
  // Extract text elements if any
  const texts = (c.match(/<text[^>]*>([\s\S]*?)<\/text>/g) || []).slice(0, 5).map(t => t.replace(/<[^>]+>/g, '').trim());
  console.log(file, 'sample texts:', texts);
});
