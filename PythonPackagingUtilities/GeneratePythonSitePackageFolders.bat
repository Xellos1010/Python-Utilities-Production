md PackageName
md tests


echo >"PackageName\__init__.py"

pause 
(
echo import setuptools
echo with open^(^"README.md^", ^"r^"^) as fh:
echo    long_description ^= fh.read^(^)
echo setuptools.setup^(
echo    name^=^"example-pkg-YOUR-USERNAME-HERE^", # Replace with your own username
echo    version^=^"0.0.1^",
echo    author^=^"Example Author^",
echo    author_email^=^"author@example.com^",
echo    description^=^"A small example package^",
echo    long_description^=long_description,
echo    long_description_content_type^=^"text/markdown^",
echo    url^=^"https://github.com/pypa/sampleproject^", # Change Github
echo    packages^=setuptools.find_packages^(^),
echo    classifiers^=^[
echo        ^"Programming Language :: Python :: 2^", # Replace with Python Interpretter
echo        ^"License :: OSI Approved :: MIT License^",
echo        ^"Operating System :: OS Independent^",
echo    ^],
echo    python_requires^=^'^>^=2.7^', # Replace with Python Interpretter 
echo ^)
)>"setup.py"

pause

(
echo # Example Package
echo This is a simple example package. You can use
echo ^[Github-flavored Markdown^]^(https:^/^/guides.github.com^/features^/mastering-markdown^/^)
echo to write your content.
)>README.md

{
echo Copyright ^(c^) 2018 The Python Packaging Authority
echo Permission is hereby granted, free of charge, to any person obtaining a copy
echo of this software and associated documentation files ^(the ^"Software^"^), to deal
echo in the Software without restriction, including without limitation the rights
echo to use, copy, modify, merge, publish, distribute, sublicense, and^/or sell
echo copies of the Software, and to permit persons to whom the Software is
echo furnished to do so, subject to the following conditions:
echo The above copyright notice and this permission notice shall be included in all
echo copies or substantial portions of the Software.
echo THE SOFTWARE IS PROVIDED ^"AS IS^", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
echo IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
echo FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
echo AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
echo LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
echo OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
echo SOFTWARE.
)>LICENSE

pip27 install --user --upgrade setuptools wheel
setup.py sdist bdist_wheel

pause