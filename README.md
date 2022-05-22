# clichessdrill
practice chess drills in a command line interface

## Installation
from PyPI:

```pip install clichessdrill```

or from source:

```poetry install```

## Play
To run and play one round:

```chessdrill```

To play any number of drills in a row, use the `-n` option. For example:
```
chessdrill -n 10
```
If no training file is specified during the call, a standard built in drill plan 
will be used.

#### Custom drill training plans
In addition, the user has the option to use their own custom training plan. To play 
and execute a custom drill plan saved as a json file use the `-f` option to 
point to the path of the training file:

```
chessdrill -n 20 -f my/training/file.json
```
The layout of the drill plan is a representation of the decision tree. As an example:
```json
{
  "name": "my drill plan",
  "play": {
    "white": {
      "c4": {
        "e5": {
          "e4": {
            "Nf6": {
              "Nc3": {}
            },
            "c5": {
              "d3": {}
            }
          }
        },
        "e6": {
          "Nc3": {}
          }
        },
        "Nf6": {
          "Nc3": {}
          }
        },
        "b6": {
          "d4": {}
        }
      }
    },
    "black": {
      "e4": {
        "c6": {}
      },
      "d4": {
        "d5": {
          "Bf4": {
            "e6": {
              "Nf3": {
                "Nf6": {}
              }
            }
          }
        }
      }
    }
  }
}
```
The subsections for the respective game color represent the decision branches according to which the user should 
respond while playing either of the sides. The decision trees can be arbitrarily deep and leaves should terminate 
with empty brackets `{}`
### Example Game Play
![game play 1](https://raw.githubusercontent.com/danielschweigert/clichessdrill/main/docs/screenshots/game_play_1.png)
![game play 2](https://raw.githubusercontent.com/danielschweigert/clichessdrill/main/docs/screenshots/game_play_2.png)
![game play 3](https://raw.githubusercontent.com/danielschweigert/clichessdrill/main/docs/screenshots/game_play_3.png)