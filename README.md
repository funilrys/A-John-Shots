# A John Shots (Hash To JSON)

> Python module/library for saving Security Hash Algorithms into JSON format.

_**Current version: 1.0.2**_

## Freatures
- Works with python2.x and python3.x
- Read a path
- Search for file if given path is a directory
- Execute **SHA1,SHA224,SHA384,SHA512 or MD5** over a file
- Get the result in JSON format on **screen** or **file**
- Exclude a file/dir which match path or a pattern

## Installation

### From Github

```bash
git clone https://github.com/funilrys/A-John-Shots.git
cd A-John-Shots
python setup.py install
```
______
# How to contribute?

To contribute, you have to **send a new [Pull Request](https://github.com/funilrys/A-John-Shots/compare)** after you **[forked](https://github.com/funilrys/A-John-Shots/pulls#fork-destination-box)** and edited the script(s).

## WARNING :warning:

### DO NOT FORGET

- To sign your commit(s) with **"Signed-off by: FirstName LastName <e.dot at service dot com>"** _**and/or**_ simply **sign your commit(s)** with **PGP** _(Please read more [here](https://github.com/blog/2144-gpg-signature-verification))_.
- All **contributions/modifications** must be done under **the `dev` or a new branch** if you plan to **send a new [Pull Request](https://github.com/funilrys/A-John-Shots/compare)**.
-  :warning::warning::warning: Every **contributions/modifications** which are under **master** _(exception for minor changes)_ **will not be merged**.

--------------------------------------------------------------------------------

# Examples

## Basic

```python
import a_john_shots

"""The following search every files under the current directory and print the
result on screen only.
"""
a_john_shots.get('.')
```

## Search for specific extensions

```python
import a_john_shots

"""The following search every files which match regex and print the
result on screen only."""
regex = r'\.py'
a_john_shots.get('.',search=regex)
```

## Output on screen and file

```python
import a_john_shots

"""The following search every files which match regex, print the
result on screen and save the results under ajohnshots.json."""
regex = r'\.py'
a_john_shots.get('.',search=regex,output=False,output_destination='ajohnshots.json')
```

## Output on file only

```python
import a_john_shots

"""The following search every files which match regex and save the results under ajohnshots.json."""
regex = r'\.py'
a_john_shots.get('.',search=regex,output=True,output_destination='ajohnshots.json')
```

## Change algorithm
Possibility: `'all'`,`'md5'`,`'sha1'`,`'sha224'`,`'sha384'`,`'sha512'`
```python
import a_john_shots

"""The following search every files which match regex,execute all algorithms against all files and save the results under ajohnshots.json."""
regex = r'\.py'
a_john_shots.get('.',search=regex,output=True,algorithm='all',output_destination='ajohnshots.json')
```
