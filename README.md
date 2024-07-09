# AutoCommitProjectSkeleton
This is a project template. Meant to be forked and then develop based on the forked project

## Usage
1. Fork this repo
2. Develop your script, e.g. `script.py`
3. Change `./.github/workflows/autocommit.yml`  
   In section `Modify last update`
   ```{yaml}
   run: |
          d=`date '+%Y-%m-%dT%H:%M:%SZ'`
          echo $d > LAST_UPDATED
   ```  
   You could add commands such as
   ``` {yaml}
          pip install -r requirements.txt
          python rsscloud.py
   ```
   And now for every scheduled execution, these two commands would be executed and the execution result(generated files) will be uploaded to the GitHub and saved as timely commit
