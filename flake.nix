{
  description = "Advent of Code 2024";

  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-24.11";
  inputs.pyproject-nix.url = "github:pyproject-nix/pyproject.nix";
  inputs.pyproject-nix.inputs.nixpkgs.follows = "nixpkgs";

  outputs =
    { nixpkgs, pyproject-nix, ... }:
    let
      project = pyproject-nix.lib.project.loadPyproject {
        projectRoot = ./.;
      };

      systems = [
        "aarch64-darwin"
        "x86_64-linux"
      ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
    in
    {
      devShells = forAllSystems(system: {
        default =
        let
          pkgs = nixpkgs.legacyPackages.${system};
          python = pkgs.python313;
          arg = project.renderers.withPackages { inherit python; };
          pythonEnv = python.withPackages arg;

        in
        pkgs.mkShell { packages = [ pythonEnv ]; };
      });
    };
}
