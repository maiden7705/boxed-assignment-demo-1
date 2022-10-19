# Pre-Installation
Make sure you have **python3**, **pip**, **git**, **docker** installed in your local environment (macOS / Linux).  
If you are running this on **windows 10 Pro (2.x+)** I'd highly recommend open/clone this project in a __[WSL2 sub-system](https://code.visualstudio.com/blogs/2019/09/03/wsl2)__.  
Also make sure in whichever OS you are running it in, the recommended way forward for docker is now through __[Docker Desktop](https://www.docker.com/products/docker-desktop/)__ instead of commandline docker engine, though even that might work, i have not backward tested it with older "cli-only" docker.  

__IMPORTANT NETWORK REQUIREMENT__: Also, make sure you **ARE NOT** running this in your private organization's / personal VPN or proxy IPs and that commandline access to pip / apt-get / yum (*whichever is your preferred installation method*) is not blocked or hindered.

# Pre-requisites
### Installing the virtual environment
    pip install virtualenv
    virtualenv --version
### Cloning the Repo
    cd ~/{your-project-directory}
    git clone  https://github.com/maiden7705/boxed-assignment-demo-1.git
    cd ~/{your-project-directory}/boxed-assignment-demo-1
### [OPTIONAL] Incase you are using vs code
    # open the vs code on WSL subsystem through your cloned folder
    code .
### make your virtual environment directory