Pure Python IPMI Library
========================

- Updated setup.py file with name and version
- Config JFrog CLI
    - jf pip-config --repo-resolve=auth-python-virtual
        - --repo-resolve -> repository name in artifactory
    - need to run `jf pip install` if there are dependencies that we need to download   
- python3 -m pip install build --user
- python3 -m build --wheel --outdir dist/ .
    - this will create wheel file 
- run jf rt u ./dist/* auth-python-virtual/ --module=python-ipmi 
    - this will upload wheel file to python repos
- As this project, vuln shows in IDE when we setup virtual environment similar to where we will run python module in runtime
    - so I created docker container using Python and put the wheel file and scanned
    - this way python vuln will show up as part of scan result


Review [main.yml] (https://github.com/MaharshiPatel/python-ipmi/blob/master/.github/workflows/main.yml)


