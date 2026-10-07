const fs = require('fs');

['Frame 1000005221.svg', 'Frame 1000005221-1.svg', 'Frame 1000005221-2.svg', 'Frame 1000005221-3.svg'].forEach(file => {
  const content = fs.readFileSync('./images/Sprance images/UI/' + file, 'utf8');
  // Check occurrences of something unique or inspect size
  console.log(file, 'has "Leaderboard":', content.includes('Leaderboard'), 'has "Settings":', content.includes('Settings'), 'has "Meet":', content.includes('Meet'));
});
