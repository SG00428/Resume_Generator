import argparse
from fpdf import FPDF

class ResumePDF(FPDF):
    def __init__(self, font_size, font_color, background_color):
        super().__init__()
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color

    def header(self):
        self.set_fill_color(*self.hex_to_rgb(self.background_color)) # converting given hex code to rgb for bg color
        self.rect(0, 0, self.w, self.h, 'F')  # for filling entire page

        self.set_font("Arial", style="B", size=self.font_size + 7)  # larger font for name
        self.set_text_color(*self.hex_to_rgb(self.font_color))
        self.cell(0, 10, "Sneha Gautam", align="C", ln=True)   # name

    def body(self):
        self.set_font("Arial", size=self.font_size) 
        self.set_text_color(*self.hex_to_rgb(self.font_color))

        # contact
        self.cell(0, 5, "sneha.gautam@iitgn.ac.in", ln=True, align="C")
        self.cell(0, 5, "Github: https://github.com/SG00428", ln=True, align="C")
        self.ln(5)
        # education
        self.underline_heading("Education")
        self.cell(0, 5, "B.Tech. in Computer Science and Engineering, IIT Gandhinagar (2022-Present), CPI: 6.82", ln=True, align="L")
        self.cell(0, 5, "Class XII: Physics, Chemistry, Maths, S.D. Global School, Ghaziabad (2021-2022), Marks: 96.8%", ln=True, align="L")
        self.cell(0, 5, "Class X: S.D. Global School, Ghaziabad (2019-2020), Marks: 96.8%", ln=True, align="L")
        self.ln(5)

        # technical skills
        self.underline_heading("Technical Skills")
        self.cell(0, 5, "Programming Languages: C, C++, Python, Verilog", ln=True, align="L")
        self.cell(0, 5, "Tools: Autodesk Inventor, Matlab, Arduino IDE, Google Colab, Git, Vivado", ln=True, align="L")
        self.cell(0, 5, "Libraries: NumPy, Pandas, Seaborn, Matplotlib, SciPy, Scikit-Learn, PyTorch, TensorBoard", ln=True, align="L")
        self.ln(5)

        # experience
        self.underline_heading("Experience")   # headings are underlined
        self.cell(0, 8, "Machine Learning Intern | Orinson Technologies Pvt. Ltd. (Sep '24 - Oct '24)", ln=True, align="L")
        self.add_bullet_points([     # bullet points for details
            "Applied ML techniques for data preprocessing, model evaluation, and optimization.",
            "Built a web app using Flask for predictions.",
        ])
        self.cell(0, 8, "STEM Intern | SoulAI (Dec '24 - Present)", ln=True, align="L")
        self.add_bullet_points([
            "Focused on Reinforcement Learning with Human Feedback to optimize AI model.",
            "Contributed to various tasks related to AI model optimization and fine-tuning.",
        ])
        self.ln(5)   

        # projects
        self.underline_heading("Projects")
        self.cell(0, 8, "Machine Learning Projects Hub, IIT Gandhinagar (Jan '24 - April '24)", ln=True, align="L")
        self.add_bullet_points([
            "Below are the some tasks performed utilizing various Machine Learning algorithms.",
            "Human Activity Recognition, Image Reconstruction, rudimentary Next Character Predictor."
        ])
        self.cell(0, 8, "Automated Verilog Code Generator, IIT Gandhinagar (Jan '24 - April '24)", ln=True, align="L")
        self.add_bullet_points([
            "Designed and developed a python based website taking user input as number of bits and type of multiplier or adder.",
            "Rolling out the intended output as verilog code.",
        ])
        self.cell(0, 8, "Machine Learning Pipelines with Azure ML Studio (Aug '24)", ln=True, align="L")
        self.add_bullet_points([
            "Built ML pipelines to predict income based on age, education, occupation, etc.",
            "Used Azure ML Studio to streamline the process and improve model deployment.",
        ])
        self.cell(0, 8, "Algorithmic Game Solvers in C/C++ (Aug '23 - nov '23)", ln=True, align="L")
        self.add_bullet_points([
            "Developed solvers for classic algorithmic games like Tic-Tac-Toe, Up-it-Up, 2*2 Rubik's Cube, Sim, Connect4.",
            "Implemented advanced graph based algorithms and heuristics search algorithms.",
        ])
        self.cell(0, 8, "Natural Language Processing (Aug '24 - Nov '24)", ln=True, align="L")
        self.add_bullet_points([
            "Web-scraped 15 GB of Urdu text data, cleaned data by removing inappropriate words, and deduplicated the dataset.",
            "Tokenized the dataset using various tokenizer and selected the best absed on fertility score.",
            "Trained the AI models on the dataset and generated response from the prompts"
        ])
        self.ln(5)

    def add_bullet_points(self, points):  # this adds bullet points
        for point in points:
            self.cell(0, 5, f"  * {point}", ln=True, align="L")


    def underline_heading(self, title):   # for adding underline
        self.set_font("Arial", style="B", size=self.font_size + 6)  # Larger font size for heading
        self.cell(0, 5, title, ln=True, align="L")
        self.line(self.get_x(), self.get_y(), self.get_x() + self.get_string_width(title), self.get_y())

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def parse_args():   # for command-line arguments
    parser = argparse.ArgumentParser(description="Generate a customizable resume PDF.")
    parser.add_argument("--font-size", type=int, default=16, help="Font size for the text.")  # default font size: 16
    parser.add_argument("--font-color", type=str, default="#000000", help="Font color (hex code).") # default font color
    parser.add_argument("--background-color", type=str, default="#FFFFFF", help="Background color (hex code).") # default bg colour
    return parser.parse_args()

def generate_resume(font_size, font_color, background_color): # takes input as parameters and pass to ResumePDF class
    pdf = ResumePDF(font_size, font_color, background_color)
    pdf.add_page()
    pdf.body()
    output_filename = "custom_resume.pdf"
    pdf.output(output_filename)
    print(f"Resume generated: {output_filename}")

if __name__ == "__main__":
    args = parse_args()
    generate_resume(args.font_size, args.font_color, args.background_color)



        # # Section: Experience
        # self.underline_heading("Experience")
        # self.cell(0, 5, "Machine Learning Intern | Orinson Technologies Pvt. Ltd. (Sep '24 - Oct '24)", ln=True, align="L")
        # self.cell(0, 5, "Tasks: Applied ML techniques, data preprocessing, model evaluation, and optimization. Also, built a web app using Flask for predictions.", ln=True, align="L")
        # self.cell(0, 5, "STEM Intern | SoulAI (Dec '24 - Present)", ln=True, align="L")
        # self.cell(0, 5, "Tasks: Focused on Reinforcement Learning with Human Feedback to optimize AI model.", ln=True, align="L")
        # self.ln(5)

        # # Section: Projects
        # self.underline_heading("Projects")
        # self.cell(0, 5, "Machine Learning Projects Hub, IIT Gandhinagar (Jan '24 - April '24)", ln=True, align="L")
        # self.cell(0, 5, "Designed ML projects for Human Activity Recognition, Image Reconstruction, etc.", ln=True, align="L")
        # self.cell(0, 5, "Automated Verilog Code Generator, IIT Gandhinagar (Jan '24 - April '24)", ln=True, align="L")
        # self.cell(0, 5, "Developed a Python-based website to generate Verilog code for adders and multipliers.", ln=True, align="L")
        # self.cell(0, 5, "Machine Learning Pipelines with Azure ML Studio (Aug '24)", ln=True, align="L")
        # self.cell(0, 5, "Built ML pipelines to predict income based on age, education, occupation, etc.", ln=True, align="L")
        # self.cell(0, 5, "Algorithmic Game Solvers in C/C++", ln=True, align="L")
        # self.cell(0, 5, "Natural Language Processing", ln=True, align="L")
        # self.ln(5)