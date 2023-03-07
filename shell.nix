{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = with pkgs.python310Packages; [
    # Data Science Basics
    ipython
    jupyter
    pandas
    numpy
    matplotlib

    # Database Tools
    sqlalchemy
    neo4j

    # Data Query tools
    # pm4py
    # gnuhealth
   # Testing and CLI


    pytest

    # FHIR
    (buildPythonPackage rec {
      pname = "fhir.resources";
      version = "6.5.0";
      src = fetchPypi {
        inherit pname version;
        sha256 = "1d02ff2547e5b6323543c8ce9916e0c9e5536847b3b2171acb1f51a86efba16e";
      };
      doCheck = false;
      propagatedBuildInputs = [
          pytest-runner
          pydantic
      ]; })

    #DICOM
    pydicom

    garminconnect

    # CLI
    rich

    # Modules outside of nixpkgs
    (buildPythonPackage rec {
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
      ]; })




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
