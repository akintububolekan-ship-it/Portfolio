const fs = require('fs');

const content = fs.readFileSync('C:/Users/HP/.gemini/antigravity/brain/d95b2fb5-1df7-4dce-bb6c-1550ab65130d/.system_generated/steps/23/output.txt', 'utf8');
const lines = content.split('\n');

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (line.includes('1000005183') || line.includes('1000005221')) {
    console.log(`Line ${i+1}: ${line.trim()}`);
  }
}
