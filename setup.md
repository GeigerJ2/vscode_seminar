1. VS Code: https://code.visualstudio.com/
2. Python (virtual environment or anaconda):
    - Personally, I use and recommend Anaconda: https://www.anaconda.com/
    - Ideally, create and activate a new environment for the seminar: conda create --name **your_env_name**; conda activate **your_env_name**
    - For Python package installations:
      - **On Linux** - Use the commands on the provided Anaconda webpages
      - **On Windows** - Use the graphical Anaconda application: https://www.youtube.com/watch?v=7_o_kjG1Sfs
3. Python packages (and their use during the seminar):
    - **ipykernel** - To run jupyter notebook: https://anaconda.org/anaconda/ipykernel
      - To make the kernel available in jupyter notebook: python -m ipykernel install --user --name=**your_env_name**
    <!-- - TODO: verify that I need to actually install the conda env for jupyter, or it is done via the jupyter/python extension -->
    - **git** - Demonstration of git functionalities provided by VS Code: https://anaconda.org/anaconda/git
    - **ase** - Example package to demonstrate advanced navigation of large code bases: https://anaconda.org/conda-forge/ase
    - **black** - Automatic Python code formatting: https://anaconda.org/conda-forge/black
4. For the seminar recommended VS Code extensions (extension packs for convenience):
    - **Python extension pack** - Easy linking of conda env, Python Intellisense, etc.: https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack
    - **Bash extension pack** - IDE features for bash: https://marketplace.visualstudio.com/items?itemName=lizebang.bash-extension-pack
    - **Jupyter** - Running Jupyter Notebooks in VS Code: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
5. Some other useful VS Code extensions:
    - **Search with cursor** - Shortcut to search selected text on Google: https://marketplace.visualstudio.com/items?itemName=hasefumi23.search-with-cursor
    - **Kite** - AI-powered code completion: https://marketplace.visualstudio.com/items?itemName=kiteco.kite
    - **Error Lens** - Improved language diagnostics and error reporting: https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens
    - **Git File History** - Seamless browsing of different file versions in git history: https://marketplace.visualstudio.com/items?itemName=pomber.git-file-history
    - **GitLens** - Extensive additional git annotations: https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens
    - **Todo Tree** - Workspace-wide TODOs: https://marketplace.visualstudio.com/items?itemName=bat67.latex-extension-pack
    - **CodeViz Stat** - Statistings on code base: https://marketplace.visualstudio.com/items?itemName=vizzuhq.code-viz-stat
    - **LaTeX extension pack** - https://marketplace.visualstudio.com/items?itemName=bat67.latex-extension-pack