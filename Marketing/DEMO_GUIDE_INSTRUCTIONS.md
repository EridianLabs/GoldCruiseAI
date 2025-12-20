# Demo Guide PDF Conversion Instructions

## File Created
`Marketing/Demo_Guide.html` - A professionally styled 8-page demo guide ready for PDF conversion.

## How to Convert to PDF

### Method 1: Browser Print-to-PDF (Easiest)
1. Open `Demo_Guide.html` in Chrome, Firefox, or Edge
2. Press `Ctrl+P` (Windows) or `Cmd+P` (Mac)
3. Select "Save as PDF" as the destination
4. In print settings:
   - **Paper size:** A4
   - **Margins:** Default or None
   - **Background graphics:** ✅ Enable (important!)
   - **Scale:** 100%
5. Click "Save" and choose location

### Method 2: Online HTML to PDF Converter
1. Upload `Demo_Guide.html` to an online converter:
   - https://www.ilovepdf.com/html-to-pdf
   - https://www.freepdfconvert.com/html-to-pdf
   - https://html2pdf.com/
2. Download the converted PDF

### Method 3: Command Line (If you have tools installed)
```bash
# Using wkhtmltopdf (if installed)
wkhtmltopdf --page-size A4 --margin-top 2cm --margin-bottom 2cm --margin-left 2cm --margin-right 2cm Demo_Guide.html Demo_Guide.pdf

# Using weasyprint (if installed)
weasyprint Demo_Guide.html Demo_Guide.pdf
```

## What's Included

The demo guide contains:
- ✅ Professional cover page
- ✅ System requirements
- ✅ Step-by-step installation guide
- ✅ Configuration instructions
- ✅ Key parameters explanation
- ✅ Activation & testing guide
- ✅ Best practices
- ✅ Support & resources

## Design Features

- 🎨 Green/gold theme matching website
- 📄 Print-optimized A4 format
- 🖼️ Professional layout with proper spacing
- 📊 Visual elements (boxes, tables, badges)
- ✅ Step-by-step numbered instructions
- ⚠️ Warning and info boxes
- 📈 Metrics display boxes

## Customization

To customize the guide:
1. Edit `Demo_Guide.html` directly
2. Modify colors in the `<style>` section
3. Update content in the HTML body
4. Re-convert to PDF

## Notes

- The guide is designed for A4 paper size
- All colors are print-friendly
- Page breaks are optimized for printing
- Background colors will print if "Background graphics" is enabled

