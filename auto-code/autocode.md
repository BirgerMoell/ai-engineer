## Auto-code
https://github.com/AntonOsika/gpt-engineer

Choose either stable or development.

For stable release:

python -m pip install gpt-engineer
For development:

git clone https://github.com/AntonOsika/gpt-engineer.git
cd gpt-engineer
python -m pip install -e .
(or: make install && source venv/bin/activate for a venv)
API Key

Choose one of:

Export env variable (you can add this to .bashrc so that you don't have to do it each time you start the terminal)
export OPENAI_API_KEY=[your api key]
.env file:
Create a copy of .env.template named .env
Add your OPENAI_API_KEY in .env
Custom model:
See docs, supports local model, azure, etc.
Check the Windows README for windows usage.

Usage
There are two ways to work with GPT-engineer: new code mode (the default), and improve existing code mode (the -i option).

Creating new code
Create an empty folder for your project anywhere on your computer
Create a file called prompt (no extension) inside your new folder and fill it with instructions
Run gpt-engineer <project_dir> with a relative path to your folder
For example: gpt-engineer projects/my-new-project from the gpt-engineer directory root with your new folder in projects/
Improving Existing Code
Locate a folder with code which you want to improve anywhere on your computer
Create a file called prompt (no extension) inside your new folder and fill it with instructions for how you want to improve the code
Run gpt-engineer <project_dir> -i with a relative path to your folder
For example: gpt-engineer projects/my-old-project from the gpt-engineer directory root with your folder in projects/
By running gpt-engineer you agree to our terms.

Results

Check the generated files in projects/my-new-project/workspace

Workflow

gpt-engineer --help lets you see all available options.

For example:

To improve any existing project, use the flag: -i
To give feedback to/improve a gpt-engineer generated project, use: --steps use_feedback
