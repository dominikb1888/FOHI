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

    # Modules outside of nixpkgs
    (
    buildPythonPackage rec {
      pname = "rdftools";
      version = "0.2.0a";
      src = fetchPypi {
        inherit pname version;
        sha256 = "0c398154c86de1e29fe3916dd26397ebbd7101c05672459b13124e6bc4e674b1";
      };
      doCheck = false;
      propagatedBuildInputs = [
        python-i18n
        rdflib
        pyyaml
      ];
    }
    )

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
