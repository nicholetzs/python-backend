# python-backend
Project with python and other tools

# Tools:
# Virtual Lenv - A tool for creating isolated virtual python environments.
  Install: pip install virtualenv
  instal packages in a virtual environment using pip and venv: py -m venv .venv (windows)
                                                               python3 -m venv .venv (unix/macos)
  This will create a separate environment from my machine to run python :)
  To active the virtual environment: .venv\Scripts\activate (windows)
                                     source .venv/bin/activate (unix/macos) 
  The terminal is now inside the venv folder, working only with it and not with python on the computer!!

# Pylint - Pylint is a powerful tool for ensuring the quality of your Python code.
  install: pip install pylint
  (read the documentation)
  To create a config for modification: pylint --generate-rcfile > .pylintrc
  
  One way to commit is for pylint to identify files that don't comply with Pylint standards🔗https://pre-commit.com/#intro
  A framework for managing and maintaining multi-language pre-commit hooks, It will tie to Git to perform actions (hooks).
  To install: pip install pre-commit
  create a file named .pre-commit-config.yaml
  paste: 
  repos:
  - repo: local
    hooks:
      - id: pylint
        name: pylint
        entry: pylint
        language: system
        types: [python]
        args:
          [
            "-rn", # Only display messages
            "-sn", # Don't display the source
            "--rcfile=.pylintrc", # Link to your config file
            "--load-plugins=pylint.extensions.docparams", # Load an extension
          ]

  run pre-commit install to set up the git hook scripts

# Manager versions of the tools: 
  .venv/Scripts/pip freeze > requirements.txt (windows)
  .venv/bin/pip freeze > requirements.txt (unix/macos) 

  That's the step by step for initial Settings


