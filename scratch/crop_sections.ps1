Add-Type -AssemblyName System.Drawing;
$img = [System.Drawing.Image]::FromFile((Resolve-Path "images\Sprance images\Body.png"));
$scale = 3.8977;

$crop = New-Object System.Drawing.Bitmap(1600, [int](1559 * (1600 / $img.Width)));
$g = [System.Drawing.Graphics]::FromImage($crop);
$srcRect = New-Object System.Drawing.Rectangle(0, 974, $img.Width, 1559);
$destRect = New-Object System.Drawing.Rectangle(0, 0, $crop.Width, $crop.Height);
$g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel);
$crop.Save("scratch\section_01_overview.png", [System.Drawing.Imaging.ImageFormat]::Png);
$g.Dispose();
$crop.Dispose();

$crop = New-Object System.Drawing.Bitmap(1600, [int](1949 * (1600 / $img.Width)));
$g = [System.Drawing.Graphics]::FromImage($crop);
$srcRect = New-Object System.Drawing.Rectangle(0, 3430, $img.Width, 1949);
$destRect = New-Object System.Drawing.Rectangle(0, 0, $crop.Width, $crop.Height);
$g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel);
$crop.Save("scratch\section_02_process_problem_goal.png", [System.Drawing.Imaging.ImageFormat]::Png);
$g.Dispose();
$crop.Dispose();

$crop = New-Object System.Drawing.Bitmap(1600, [int](1949 * (1600 / $img.Width)));
$g = [System.Drawing.Graphics]::FromImage($crop);
$srcRect = New-Object System.Drawing.Rectangle(0, 4872, $img.Width, 1949);
$destRect = New-Object System.Drawing.Rectangle(0, 0, $crop.Width, $crop.Height);
$g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel);
$crop.Save("scratch\section_03_research_competitor.png", [System.Drawing.Imaging.ImageFormat]::Png);
$g.Dispose();
$crop.Dispose();

$crop = New-Object System.Drawing.Bitmap(1600, [int](3703 * (1600 / $img.Width)));
$g = [System.Drawing.Graphics]::FromImage($crop);
$srcRect = New-Object System.Drawing.Rectangle(0, 8887, $img.Width, 3703);
$destRect = New-Object System.Drawing.Rectangle(0, 0, $crop.Width, $crop.Height);
$g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel);
$crop.Save("scratch\section_04_personas_text.png", [System.Drawing.Imaging.ImageFormat]::Png);
$g.Dispose();
$crop.Dispose();

$crop = New-Object System.Drawing.Bitmap(1600, [int](1754 * (1600 / $img.Width)));
$g = [System.Drawing.Graphics]::FromImage($crop);
$srcRect = New-Object System.Drawing.Rectangle(0, 12473, $img.Width, 1754);
$destRect = New-Object System.Drawing.Rectangle(0, 0, $crop.Width, $crop.Height);
$g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel);
$crop.Save("scratch\section_05_features_wireframes.png", [System.Drawing.Imaging.ImageFormat]::Png);
$g.Dispose();
$crop.Dispose();

$crop = New-Object System.Drawing.Bitmap(1600, [int](4093 * (1600 / $img.Width)));
$g = [System.Drawing.Graphics]::FromImage($crop);
$srcRect = New-Object System.Drawing.Rectangle(0, 13837, $img.Width, 4093);
$destRect = New-Object System.Drawing.Rectangle(0, 0, $crop.Width, $crop.Height);
$g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel);
$crop.Save("scratch\section_06_user_flow.png", [System.Drawing.Imaging.ImageFormat]::Png);
$g.Dispose();
$crop.Dispose();

$crop = New-Object System.Drawing.Bitmap(1600, [int](2728 * (1600 / $img.Width)));
$g = [System.Drawing.Graphics]::FromImage($crop);
$srcRect = New-Object System.Drawing.Rectangle(0, 17929, $img.Width, 2728);
$destRect = New-Object System.Drawing.Rectangle(0, 0, $crop.Width, $crop.Height);
$g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel);
$crop.Save("scratch\section_07_final_design_headers.png", [System.Drawing.Imaging.ImageFormat]::Png);
$g.Dispose();
$crop.Dispose();

$crop = New-Object System.Drawing.Bitmap(1600, [int](1949 * (1600 / $img.Width)));
$g = [System.Drawing.Graphics]::FromImage($crop);
$srcRect = New-Object System.Drawing.Rectangle(0, 29817, $img.Width, 1949);
$destRect = New-Object System.Drawing.Rectangle(0, 0, $crop.Width, $crop.Height);
$g.DrawImage($img, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel);
$crop.Save("scratch\section_08_impacts.png", [System.Drawing.Imaging.ImageFormat]::Png);
$g.Dispose();
$crop.Dispose();
$img.Dispose();
Write-Output "Sections cropped successfully";
