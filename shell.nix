{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = with pkgs.python310Packages; [
    # Data Science Basics
    ipython
    jupyter
    pandas
    numpy

    # Database Tools
    sqlalchemy
    neo4j

    # Data Query tools
    # pm4py
    # gnuhealth
   # Testing and CLI
    pytest

    # CLI
    rich
  ];

in pkgs.mkShell {
  buildInputs = with pkgs; [
    pythonEnv
    redis
    neo4j
    docker
    # keep this line if you use bash
    pkgs.bashInteractive
  ];
}
