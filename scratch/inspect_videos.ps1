$shell = New-Object -ComObject Shell.Application

function Show-FolderVideos($path) {
    Write-Host "=== $path ==="
    if (-not (Test-Path $path)) { return }
    $folder = $shell.Namespace($path)
    Get-ChildItem -Path $path -Filter *.mp4 | ForEach-Object {
        $item = $folder.ParseName($_.Name)
        $dur = $folder.GetDetailsOf($item, 27)
        $res = $folder.GetDetailsOf($item, 316)
        $size = [math]::Round($_.Length / 1MB, 2)
        Write-Host "  $($_.Name) | Size: ${size} MB | Duration: $dur | Resolution: $res"
    }
}

Show-FolderVideos "C:\Users\HP\Downloads\Portfolio\images\Caterpilllar images"
Show-FolderVideos "C:\Users\HP\Downloads\Portfolio\images"
Show-FolderVideos "C:\Users\HP\Videos"
Show-FolderVideos "C:\Users\HP\Downloads\AEUX_0.8.2\AEUX_0.8.2\Figma\Public work display\Adobe After Effects Auto-Save"
Show-FolderVideos "C:\Users\HP\Downloads\AEUX_0.8.2\AEUX_0.8.2\Figma\Public work display"
