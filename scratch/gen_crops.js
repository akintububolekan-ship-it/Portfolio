const fs = require('fs');

// Let's create a PowerShell script to crop each text section cleanly
const sections = [
  { name: '01_overview', y: 250, h: 400 },
  { name: '02_process_problem_goal', y: 880, h: 500 },
  { name: '03_research_competitor', y: 1250, h: 500 },
  { name: '04_personas_text', y: 2280, h: 950 },
  { name: '05_features_wireframes', y: 3200, h: 450 },
  { name: '06_user_flow', y: 3550, h: 1050 },
  { name: '07_final_design_headers', y: 4600, h: 700 },
  { name: '08_impacts', y: 7650, h: 500 }
];

let ps = `Add-Type -AssemblyName System.Drawing;\n$img = [System.Drawing.Image]::FromFile((Resolve-Path "images\\Sprance images\\Body.png"));\n$scale = 3.8977;\n`;

sections.forEach(s => {
  const pixelY = Math.round(s.y * 3.8977);
  const pixelH = Math.round(s.h * 3.8977);
  ps += `
$crop = New-Object System.Drawing.Bitmap(1600, [int](${pixelH} * (1600 / $img.Width)));
$g = [System.Drawing.Graphics]::FromImage($crop);
$srcRect = New-Object System.Drawing.Rectangle(0, ${pixelY}, $img.Width, ${pixelH});
$destRect = New-Object System.Drawing.Rectangle(0, 0, $crop.Width, $crop.Height);
$g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel);
$crop.Save("scratch\\section_${s.name}.png", [System.Drawing.Imaging.ImageFormat]::Png);
$g.Dispose();
$crop.Dispose();
`;
});

ps += `$img.Dispose();\nWrite-Output "Sections cropped successfully";\n`;

fs.writeFileSync('./scratch/crop_sections.ps1', ps);
console.log('crop_sections.ps1 written');
