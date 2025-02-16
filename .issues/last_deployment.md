```powershell
PS C:\Projects\team-5-laurie2> git push heroku main -f
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 16 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (7/7), 783 bytes | 783.00 KiB/s, done.
Total 7 (delta 4), reused 0 (delta 0), pack-reused 0
remote: Updated 7188 paths from 266339e
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Building on the Heroku-24 stack
remote: -----> Using buildpacks:
remote:        1. heroku/nodejs
remote:        2. heroku/python
remote: -----> Node.js app detected
remote:        
remote: -----> Creating runtime environment
remote:        
remote:        NPM_CONFIG_LOGLEVEL=error
remote:        NODE_VERBOSE=false
remote:        NODE_ENV=production
remote:        NODE_MODULES_CACHE=true
remote:
remote: -----> Installing binaries
remote:        engines.node (package.json):   18.x
remote:        engines.npm (package.json):    unspecified (use default)
remote:
remote:        Resolving node version 18.x...
remote:        Downloading and installing node 18.20.6...
remote:        Using default npm version: 10.8.2
remote:        
remote: -----> Restoring cache
remote:        Loading 1 from cacheDirectories (package.json):
remote:        - frontend/node_modules
remote:        
remote: -----> Installing dependencies
remote:        Installing node modules
remote:        
remote:        added 140 packages, and audited 141 packages in 2s
remote:
remote:        24 packages are looking for funding
remote:          run `npm fund` for details
remote:
remote:        found 0 vulnerabilities
remote:        npm notice
remote:        npm notice New major version of npm available! 10.8.2 -> 11.1.0
remote:        npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.1.0    
remote:        npm notice To update run: npm install -g npm@11.1.0
remote:        npm notice
remote:        
remote: -----> Build
remote:        Detected both "build" and "heroku-postbuild" scripts
remote:        Running heroku-postbuild
remote:        
remote:        > team5-api@1.0.0 heroku-postbuild
remote:        > cd frontend && npm install && npm run build
remote:
remote:        
remote:        up to date, audited 249 packages in 1s
remote:
remote:        49 packages are looking for funding
remote:          run `npm fund` for details
remote:
remote:        found 0 vulnerabilities
remote:        
remote:        > frontend@0.0.0 build
remote:        > npm run build:client
remote:
remote:        
remote:        > frontend@0.0.0 build:client
remote:        > esbuild src/main.jsx --bundle --outfile=dist/assets/js/main.js --loader:.js=jsx --loader:.jsx=jsx --loader:.css=css --format=esm --sourcemap --minify
remote:
remote: ▲ [WARNING] Use "src/pages/registration/SignIn.jsx" instead of "src/pages/registration/signIn.jsx" to avoid issues with case-sensitive file systems [different-path-case]
remote:
remote:     src/App.jsx:7:19:
remote:       7 │ import SignIn from "./pages/registration/signIn";
remote:         ╵                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
remote:
remote: ▲ [WARNING] Use "src/styles/button.module.css" instead of "src/styles/Button.module.css" to avoid issues with case-sensitive file systems [different-path-case]
remote:
remote:     src/pages/registration/signIn.jsx:8:22:
remote:       8 │ import btnStyles from "../../styles/Button.module.css";
remote:         ╵                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
remote:
remote: 2 warnings
remote:
remote:   dist/assets/js/main.js       264.8kb
remote:   dist/assets/js/main.css        4.3kb
remote:   dist/assets/js/main.js.map     1.2mb
remote:   dist/assets/js/main.css.map   11.9kb
remote:
remote: ⚡ Done in 57ms
remote:        
remote: -----> Caching build
remote:        Saving 1 cacheDirectories (package.json):
remote:        - frontend/node_modules
remote:        
remote: -----> Pruning devDependencies
remote:        
remote:        up to date, audited 141 packages in 570ms
remote:
remote:        24 packages are looking for funding
remote:          run `npm fund` for details
remote:
remote:        found 0 vulnerabilities
remote:        
remote: -----> Build succeeded!
remote: -----> Python app detected
remote: -----> Using Python 3.12.9 specified in runtime.txt
remote:
remote:  !     Warning: The runtime.txt file is deprecated.
remote:  !
remote:  !     The runtime.txt file is deprecated since it has been replaced
remote:  !     by the more widely supported .python-version file.
remote:  !
remote:  !     Please delete your runtime.txt file and create a new file named:
remote:  !     .python-version
remote:  !
remote:  !     Make sure to include the '.' at the start of the filename.
remote:  !
remote:  !     In the new file, specify your app's Python version without
remote:  !     quotes or a 'python-' prefix. For example:
remote:  !     3.12
remote:  !
remote:  !     We strongly recommend that you use the major version form
remote:  !     instead of pinning to an exact version, since it will allow
remote:  !     your app to receive Python security updates.
remote:  !
remote:  !     In the future support for runtime.txt will be removed and
remote:  !     this warning will be made an error.
remote:
remote: -----> Restoring cache
remote: -----> Using cached install of Python 3.12.9
remote: -----> Installing pip 24.3.1, setuptools 70.3.0 and wheel 0.45.1
remote: -----> Installing SQLite3
remote: -----> Installing dependencies using 'pip install -r requirements.txt'
remote: -----> Skipping Django collectstatic since the env var DISABLE_COLLECTSTATIC is set.
remote: -----> Discovering process types
remote:        Procfile declares types -> web, web-backend
remote:
remote: -----> Compressing...
remote:        Done: 122.5M
remote: -----> Launching...
remote:        Released v76
remote:        https://team5-api-eu-5d24fa110c36.herokuapp.com/ deployed to Heroku      
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/team5-api-eu.git
   52c9e38..2f5ccb8  main -> main
```