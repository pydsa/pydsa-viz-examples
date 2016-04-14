# pydsa-viz-examples
PyDSA Visualization Examples

**Team**: Code-ologists

**Team Members**: Kanika Murarka [kanikaa1234](https://github.com/kanikaa1234)
		  		    Anika Murarka [anikamurarka](https://github.com/anikamurarka)

**Set up environment**

Create and activate virtual environment.
```bash
$ pip install -r requirements.txt
```

**Set-up environment variables**
After activating your virtual environment export the following variables:

```bash
export SECRET_KEY="alskj2mn34m@$%asd#45ASD"
export DATABASE_URL="sqlite:///db.sqlite3"
export DEBUG=True
```


**Algorithm Implemented**: 

1. Bubble Sort implementation using `python` and `matplotlib`

```bash
$ cd Code-ologists
$ python bubble_sort.py 
```

2. Visualization of Bubble Sort as a web app using `Django` and `JavaScript`

```bash
$ cd Code-ologists
$ ./startserver.sh
```

The server is up and running at [localhost:8000](http://0.0.0.0:8000)

Some features :- 
+ Whenever you RELOAD the page, you will see distinct colors.
+ Every iteration is played as an animation.
+ Hover on the bars to see the number that is sorted.
+ You can make different sorting objects and visualize Bubble Sort on it.

