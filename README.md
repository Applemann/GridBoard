# GridBoard


## Local setup:

#####  Fork project from github and clone it:
  
  ```
  git clone <git-repository>
  ```

  
#####  go to repository:
  ```
  cd GridBoard
  ```
  
#####  create virtualenv:
```
mkdir gridboard-dev
virtualenv gridboard-dev
source ./gridboard-dev/bin/activate

pip install -r requirements.txt
```


##### run server:
```
export FLASK_APP=server.py && flask run --host=0.0.0.0
```


## Special thanks:

 - [Flask](http://flask.pocoo.org/): Python microframework.



## Authors:

 - Martin Jablečník

