# Python

## Strings
Methods for work with strings

## Linked Lists

## Hash Tables

## Tests

### Pytest
Pytest - utility to run tests. Tests files and functions should begin from 'test_'.
Pytest can capture STDOUT and STDERR with capsys:

from greet import welcome

def test_myoutput(capsys):
    welcome("hello", "world")
    out, err = capsys.readouterr()
    assert out == "STDOUT: hello\n"
    assert err == "STDERR: world\n"

    welcome("next")
    out, err = capsys.readouterr()
    assert out == "STDOUT: next\n"
    assert err == ""

### Fixture
@pytest.fixture using to init class and reuse it in other fucntions/

## Files

| Open Mode                  | r | r+ | w | w+ | a | a+ | x | x+ |
|----------------------------|---|----|---|----|---|----|---|----|
| read                       | + | +  |   | +  |   | +  |   | +  |
| write                      |   | +  | + | +  | + | +  | + | +  |
| create a new file          |   |    | + | +  | + | +  | + | +  |
| open an existing file      |   |    | + | +  | + | +  |   |    |
| file content deleting      |   |    | + | +  |   |    |   |    |
| cursor at the beggin       | + | +  | + | +  |   |    | + | +  |
| cursor at the end          |   |    |   |    | + | +  |   |    |
| writing after seek         |   | +  | + | +  |   |    | + | +  |



# Golang

** Slices

** Concurrency

*** Goroutines

### Channels

### Workers

## Generics


# GIT

## Cherry-Pick
git cherry pick enables arbitrary Git commits to be picked by reference and appended to the current working HEAD.

## Merge
The existing branches are not changed in any way.
Integrates changes from one branch into another, creating a merge commit. It preserves branch histories but can result in a more complex history with merge bubbles. 

## Rebase
Reapplies changes from one branch on top of another, resulting in a linear commit history. It can make the history cleaner but may require conflict resolution.

## Config

### Change name, email

git config --global user.name "Max"
git config --global user.email "max@kube.gg"

### Auto Set Upstream
Git version >= 2.37.1
git config --global push.autoSetupRemote true

# Linux

## Tar
--no-mac-metadata // don't include *_files to archive
