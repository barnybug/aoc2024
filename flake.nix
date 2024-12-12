{
  description = "Adevent of Code 2024";

  inputs.pyproject-nix.url = "github:pyproject-nix/pyproject.nix";
  inputs.pyproject-nix.inputs.nixpkgs.follows = "nixpkgs";

  outputs =
    { nixpkgs, pyproject-nix, ... }:
    let
      project = pyproject-nix.lib.project.loadPyproject {
        projectRoot = ./.;
      };

      pkgs = nixpkgs.legacyPackages.x86_64-linux;
      python = pkgs.python313;

    in
    {
      devShells.x86_64-linux.default =
        let
          arg = project.renderers.withPackages { inherit python; };
          pythonEnv = python.withPackages arg;

        in
        pkgs.mkShell { packages = [ pythonEnv ]; };
    };
}
