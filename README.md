#Readme for the solution **scramble.py**:

##The solution consists of two Classes:

 - **TextBlock**:
   - It represents a text sequence
   - It has a textType variable, to determine its content
   - It has a *scramble* function as described in the original readme
   
 - **TextSplitter**:
   - It processes an input text: Splits the text into word and not word blocks
   - It has a *scrambleWords* function which realizes the needed effect described in the original readme

##Running Unit test:

The tests were written using the *doctest* module. Running the **scramble.py** script evaluates the test units of the two classes.

Current tests are written in the source code, but optionally all the tests can be run using the **scramble.test** file. 

#Original readme for task *Scramble letters exercise*:

Can you read the following paragraph?

"Aoccdrnig to rscheearch at Cmabrigde Uinervtisy, it deosn't mttaer in waht oredr the ltteers in a wrod are, the olny iprmoetnt tihng is taht the frist and lsat ltteer be at the rghit pclae. The rset can be a toatl mses and you can sitll raed it wouthit a porbelm. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe." 


Let's create something similar that can scramble the words in sentences so that they remain legible. 

To simplify the problem of scrambling it would not use random order, but just reverse the inner letters of the word, while keeping the first and last ones in place.

## Examples

```
t hin g -> t nih g
w hol e -> w loh e
i mportan t -> i natropm t
p roble m -> p elbor m
```

## How

Implementation can be done in either Java, C++ or Python. It is important to provide unit tests that prove the working solution. More about unit tests [here.](http://en.wikipedia.org/wiki/Unit_testing)



You can choose any kind of framework that suits you the best. Please provide the necessary build script that compiles your solution and runs the tests with one command. (Makefile, a simple bash script, or whatever you know. The point is to be able to compile and run tests with a single command.)

The problem itself is not difficult. In this exercise, the emphasis is on showing the whole development cycle for a micro project. This means having tests, having a build system, and writing clean and readable code.

## FAQ

**Does the program need to read/write from/to the standard input/output?** <br>
No. Reading and writing from standard input and output are not needed as the unit tests describe the behavour of the program. Check out unit test examples on the web.

**I am lost. What kind of unit test framework shall I use?** <br>
Here are some unit test framework suggestions:
* C++  - Catch [Check out the tutorial](https://github.com/philsquared/Catch/blob/master/docs/tutorial.md)
* Java - JUnit
* Python - doctest

**Does it have to work for sentences, or just words only?** <br>
It has to work for sentences as well.

Have fun!




