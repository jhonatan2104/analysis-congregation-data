import subprocess


def pip_install(name, upgrade=False):
    if(upgrade == True):
        subprocess.call(['pip3', 'install', '--upgrade', name])
    else:
        subprocess.call(['pip3', 'install', name])


def install():
    pip_install("gspread")
    pip_install("oauth2client", upgrade=True)
    pip_install("PyOpenSSL")
    pip_install("pandas")
    pip_install("openpyxl")
