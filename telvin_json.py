from subprocess import run, PIPE, CalledProcessError

def run_npm_init():
    try:
        proc = run(["npm", "init", "-y"], stdout=PIPE)
        print("npm init completed successfully!")
        output = proc.stdout.decode()  # capture output into a string
        print(f"output: {output}")
        
        proc = run(["touch", "server.js"], stdout=PIPE)
        output = proc.stdout.decode()  
        print("server.js created successfully!")
        run(["npm", "i", "nodemon"])
        print("nodemon installed successfully!")
    except CalledProcessError as e:
        print("Error occurred:", e)
        print(e.returncode)

run_npm_init()