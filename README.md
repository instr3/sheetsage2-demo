# SheetSage2 Demo Page

This is a static demo page for showcasing melody transcription results from SheetSage models.

## Features

- **Interactive Audio Player**: Each demo includes a crossfade player that allows you to blend between the original audio and the transcription result.
- **Multiple Models**: Compare results from three different models:
  - SheetSage1
  - SheetSage2 Vocal
  - SheetSage2 FullBand
- **Responsive Design**: Works on desktop and mobile devices.
- **No Server Required**: Pure static HTML/CSS/JavaScript that can be hosted on GitHub Pages.

## File Structure

```
sheetsage2-demo/
├── index.html                    # Main demo page
├── audio/
│   ├── input/                    # Original audio files
│   │   ├── 000.mp3
│   │   ├── 001.mp3
│   │   └── ...
│   ├── sheetsage1/              # SheetSage1 transcription results
│   │   ├── 000.mp3
│   │   └── ...
│   ├── sheetsage2_vocal/        # SheetSage2 Vocal transcription results
│   │   ├── 000.mp3
│   │   └── ...
│   └── sheetsage2_fullband/     # SheetSage2 FullBand transcription results
│       ├── 000.mp3
│       └── ...
├── render_demo.py               # Script to render MIDI to MP3
└── reference_page/              # Reference implementation (not deployed)
```

## Usage

### Local Testing

Simply open `index.html` in your web browser:

```bash
# Windows
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

Or use a local web server for better compatibility:

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js (if you have http-server installed)
npx http-server -p 8000
```

Then navigate to `http://localhost:8000` in your browser.

### Deploying to GitHub Pages

1. Create a new GitHub repository or use an existing one.

2. Push your files to the repository:
   ```bash
   git init
   git add index.html audio/
   git commit -m "Add SheetSage2 demo page"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

3. Enable GitHub Pages:
   - Go to your repository settings
   - Navigate to "Pages" section
   - Under "Source", select "main" branch and "/" (root) folder
   - Click "Save"

4. Your demo will be available at:
   ```
   https://YOUR_USERNAME.github.io/YOUR_REPO/
   ```

## Adding New Demos

To add new audio demos:

1. Place the original audio file in `audio/input/`
2. Generate transcriptions using your models
3. Run `render_demo.py` to convert MIDI to MP3 (or manually place MP3 files)
4. Add the filename to the `audioFiles` array in `index.html` (around line 322)

Example:
```javascript
const audioFiles = [
    '000.mp3',
    '001.mp3',
    'your-new-file.mp3',  // Add your new file here
    // ...
];
```

## Customization

### Changing the Title and Description

Edit the `<h1>` and `.description` elements in the `#header` section of `index.html`.

### Modifying Models

Edit the `models` array in the JavaScript section:

```javascript
const models = [
    { id: 'model_id', label: 'Display Name', folder: 'audio_folder_name' },
    // Add or modify models here
];
```

### Styling

All styles are embedded in the `<style>` section of `index.html`. You can customize:
- Colors
- Fonts
- Layout
- Button styles
- And more!

## Browser Compatibility

- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Mobile browsers: ✅ Full support

## Dependencies

- [Tone.js](https://tonejs.github.io/) (v14.8.49) - For audio playback and crossfading
  - Loaded from CDN, no installation required

## Troubleshooting

### Audio files not loading

- Make sure the file paths are correct
- Check that all audio files are in the correct folders
- Verify file names match exactly (including case sensitivity on Linux/macOS)
- If some models don't have outputs yet, they will show "Failed to load" message

### Crossfade not working

- Ensure both the original and transcription audio files are present
- Check browser console for errors
- Make sure Tone.js is loaded (check network tab in developer tools)

### GitHub Pages not updating

- GitHub Pages can take a few minutes to update after pushing changes
- Try force-refresh your browser (Ctrl+F5 or Cmd+Shift+R)
- Check the "Actions" tab in your repository for build status

## License

This demo page is based on the SheetSage project. Please refer to the original project for licensing information.

## Credits

- Audio player implementation adapted from [Chris Donahue's SheetSage demo](https://chrisdonahue.com/sheetsage/)
- Uses [Tone.js](https://tonejs.github.io/) for audio processing

