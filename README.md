# Resume Generator

`resume_generator.py` is a Python script that generates a customizable PDF resume using the FPDF library. You can specify font size, font color, and background color as input arguments to tailor the resume to your needs.

## Prerequisites

Ensure you have the following installed on your system:

1. Python 3.x
2. Required libraries:
   - `fpdf`
   - `argparse` (part of the Python standard library)

You can install the `fpdf` library using pip if it is not already installed:
```bash
pip install fpdf
```

## File Structure

- `resume_generator.py`: The Python script to generate the PDF resume.
- `custom_resume.pdf`: The output PDF file generated by the script.

## Command-Line Arguments

The script accepts the following command-line arguments:

| Argument              | Description                        
|-----------------------|---------------------------------------
| `--font-size`         | Font size for the text (integer).
| `--font-color`        | Font color in hexadecimal format.
| `--background-color`  | Background color in hexadecimal format.

## Usage

To run the script and generate a resume, use the following command (specify arguments as per need):

```bash
python resume_generator.py --font-size 20 --font-color "#000000" --background-color "#FFFFFF"
```

### Output
The script will generate a PDF file named `custom_resume.pdf` in the same directory as the script.

## Features

- **Customizable Design:**
  - Adjust font size to control the appearance of text.
  - Choose font and background colors using hex codes.
- **Predefined Sections:**
  - Name
  - Contact Information
  - Education
  - Technical Skills
  - Experience
  - Projects

## Code Structure

### Core Components

1. **`ResumePDF` Class:**
   - Handles PDF generation and layout.
   - Includes methods for adding sections, headings, bullet points, and customization options.

2. **`parse_args()` Function:**
   - Parses command-line arguments for customization.

3. **`generate_resume()` Function:**
   - Creates the PDF and saves it as `custom_resume.pdf`.

### Key Methods

- `header()`: Adds the resume's header, including the name and background color.
- `body()`: Adds the main content, including various sections.
- `add_bullet_points(points)`: Adds bullet points under a section.
- `underline_heading(title)`: Adds a heading with an underline.
- `hex_to_rgb(hex_color)`: Converts a hex color code to an RGB tuple.
