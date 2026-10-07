const fs = require('fs');

const content = fs.readFileSync('C:/Users/HP/.gemini/antigravity/brain/d95b2fb5-1df7-4dce-bb6c-1550ab65130d/.system_generated/steps/23/output.txt', 'utf8');
const lines = content.split('\n');

const searchNodes = ['551:18883', '551:19338', '551:19824', '551:20582', '550:16480', '551:18007', '540:24674', '540:12029', '540:12101', '540:12119'];

searchNodes.forEach(nodeId => {
  const lineIdx = lines.findIndex(l => l.includes(`id="${nodeId}"`));
  if (lineIdx !== -1) {
    console.log(`\n=== NODE ${nodeId} at line ${lineIdx+1} ===`);
    // Print 15 lines before to see parent frame and headers
    for (let j = Math.max(0, lineIdx - 15); j <= lineIdx; j++) {
      console.log(lines[j]);
    }
  }
});
