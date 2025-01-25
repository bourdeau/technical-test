Technical Test
----

## Setup
```
poetry install
```
## Run
```
poetry run python spark/main.py --operation SUM --paths "https://gist.githubusercontent.com/bourdeau/c215096bb45e1b3a4ce1a827bb091f2e/raw/037a1c1c4bb948c642027d778dfd2906c0160838/gistfile1.txt, /home/ph/www/s
park/test-line.txt"
```

## Tests

```
make test
```

**Note:** change the file path in the command, this is my home

## Notes

- I didn't follow the exact instructions (which is not good). I considered the format could be guessed
and that we could mix file sources (http & file) in the same command.
- A lot of things could be done better, like removing all the static methods, using generators
instead of lists in case of large data set, etc


## Instructions
```
The goal of this exercise is to write a tool that will aggregate and transform
data from various data sources. You are free to write this program in any
language you like.

The goal of this exercise is to peek at your affinity with program architecture
and at your coding habits; rather than judging your raw puzzle-solving skills.

Therefore, a well-tested, well-documented, and clearly architectured version
of a subset of the requirements is better than an untested implementation of
the whole specification.

# Specification

## Abstract

Write a command-line tool that takes as input:

- an arbitrary number of data sources defined below
- the name of one operation among those defined in this specification

Your program will read data from all the data sources, apply an operation to
that data, and output the result of the operation.

The output should be output in table format, as defined below.

## Data sources

A data source is defined as:
- Either an URL to an HTTP resource, or the path to a local file
- An input format among the data formats defined below.

Your program only handles two-dimensional tables of integers.

## Formats

The data formats supported are:
- The table format
- The line format

Note that the examples below mention JSON, but you are not required to
implement it.

### The table format

The table format stores a 2-dimensional table of numbers in a text file. The
data is arranged by row; rows are separated with line breaks, while items are
separated with spaces.


In the output, please use multiple spaces to align numbers, like in the
examples below.

### The line format

The line format is a way to store a 2-dimensional table of numbers on a single
line of text.  The data is represented as a space-separated list of numbers.

- the first number is the number of rows of data present in the file
- the rest of the numbers are the contents of the rows of data

### Data examples

The following data in JSON format:
  [[1,23,345],[567,678,789]]
is written like this in line format:
  2 1 23 345 567 678 789
and like this in table format:
  1  23 345
  567 678 789

The following data in JSON format:
  [[1,2],[3,4],[5,678]]
is written like this in line format:
  3 1 2 3 4 5 678
and like this in table format:
  1   2
  3   4
  5 678

The following file in line format is invalid and should trigger an error, as
it's impossible to arrange 4 items in 3 rows of the same length:
  3 123 234 345 678

The following file in table format is invalid and should trigger an error, as not all rows are the same length:
  1 2 3
  4 5 6
  7 8

## Operations

There are three supported operations:

- APPEND
- COMBINE
- SUM

### APPEND

This operation is only supported if all data sources have the same number of columns.

This operation copies every row from every input into the output.

For example, given the following input:
    1 2 3
    4 5 6
And the following input:
     7  8  9
    10 11 12
    13 14 15
The APPEND operation will give the follwing output:
     1  2  3
     4  5  6
     7  8  9
    10 11 12
    13 14 15

### COMBINE

This operation is only supported if all data sources have the same number of rows.

This operation works row-wise among the input sources, and concatenates every corresponding rows.

For example, given the following input:
    1 2 3
    4 5 6
And the following input:
    7  8
    9 10
The COMBINE operation will produce the following output:
    1 2 3 7  8
    4 5 6 9 10

    [[1, 2, 3], [4, 5, 6]]
    [[7, 8], [9, 10]]

    [[1, 2, 3, 7, 8], [4, 5, 6, 9, 10]]

### SUM

This operation is only supported if all data sources have the same number of
rows and the same number of columns

This operation sums the numbers that are at the same place in the grid.

For example, given the following input:
    1 2 3
    4 5 6
And the following input:
     7  8  9
    10 11 12
The SUM operation will give the follwing output:
     8 10 12
    14 16 18

```
