const fs = require('fs');

const content = fs.readFileSync('C:/Users/HP/.gemini/antigravity/brain/d95b2fb5-1df7-4dce-bb6c-1550ab65130d/.system_generated/steps/23/output.txt', 'utf8');

// Let's find direct children of Frame 1000005340 (id="540:11993")
// Indentation for Frame 1000005340 is 6 spaces: "      <frame id=\"540:11993\""
// Direct children will have 8 spaces indentation: "        <..."
const lines = content.split('\n');
let insideMain = false;

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  if (line.includes('id="540:11993"')) {
    insideMain = true;
    console.log('MAIN START:', line.trim());
    continue;
  }
  if (insideMain) {
    // Check if closing tag for 540:11993
    if (line.startsWith('      </frame>')) {
      insideMain = false;
      console.log('MAIN END');
      break;
    }
    // Direct child has exactly 8 spaces
    if (line.startsWith('        <') && !line.startsWith('          <')) {
      console.log(`Line ${i}: ${line.trim()}`);
    }
  }
}
